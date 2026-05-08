#!/usr/bin/env node
// Discover and build every LP Diazo theme under themes/.
// Watch mode: sass --watch with multi-input, no postcss/cleancss (dev uses theme.css).
// Build mode: sass → postcss (autoprefixer) → cleancss (minify) per theme.

import { glob } from 'glob';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { parseArgs } from 'node:util';

const { values: args } = parseArgs({
  options: {
    watch: { type: 'boolean', default: false },
    theme: { type: 'string' },
  },
});

// Script lives at themes/scripts/build-themes.mjs; themes are siblings.
const themesDir = path.resolve(import.meta.dirname, '..');
const allEntries = await glob(`${themesDir}/*/scss/theme.scss`);
const entries = allEntries.filter((p) => {
  const themeName = path.basename(path.dirname(path.dirname(p)));
  return !themeName.startsWith('_') && (!args.theme || themeName === args.theme);
});

if (entries.length === 0) {
  console.error(
    `[build-themes] No theme entry points found${args.theme ? ` for --theme=${args.theme}` : ''}`,
  );
  process.exit(1);
}

const sassPairs = entries.map((entry) => {
  const themeDir = path.dirname(path.dirname(entry));
  const out = path.join(themeDir, 'styles', 'theme.css');
  return `${entry}:${out}`;
});

console.log(`[build-themes] ${args.watch ? 'watching' : 'building'} ${entries.length} theme(s):`);
for (const e of entries) {
  console.log(`  - ${path.basename(path.dirname(path.dirname(e)))}`);
}

const sassArgs = [
  ...(args.watch ? ['--watch'] : []),
  '--load-path=node_modules',
  '--style=expanded',
  '--source-map',
  '--embed-sources',
  '--no-error-css',
  ...sassPairs,
];

const sassChild = spawn('sass', sassArgs, { stdio: 'inherit' });

if (args.watch) {
  // In watch mode, sass owns the lifecycle. Forward its exit code.
  sassChild.on('exit', (code) => process.exit(code ?? 0));
} else {
  // In build mode, after sass completes, run postcss + cleancss per theme.
  sassChild.on('exit', async (code) => {
    if (code !== 0) {
      console.error(`[build-themes] sass exited with code ${code}`);
      process.exit(code);
    }
    try {
      for (const entry of entries) {
        const themeDir = path.dirname(path.dirname(entry));
        const themeName = path.basename(themeDir);
        const cssIn = path.join(themeDir, 'styles', 'theme.css');
        const cssMinOut = path.join(themeDir, 'styles', 'theme.min.css');

        console.log(`[build-themes] postprocessing ${themeName}`);
        await runStep('postcss', ['--use', 'autoprefixer', '--replace', cssIn]);
        await runStep('cleancss', [
          '-O1',
          '--format',
          'breakWith=lf',
          '--with-rebase',
          '--source-map',
          '--source-map-inline-sources',
          '--output',
          cssMinOut,
          cssIn,
        ]);
      }
      console.log('[build-themes] done');
    } catch (err) {
      console.error(`[build-themes] ${err.message}`);
      process.exit(1);
    }
  });
}

function runStep(cmd, cmdArgs) {
  return new Promise((resolve, reject) => {
    const child = spawn(cmd, cmdArgs, { stdio: 'inherit' });
    child.on('exit', (code) => {
      if (code === 0) resolve();
      else reject(new Error(`${cmd} exited with code ${code}`));
    });
    child.on('error', reject);
  });
}
