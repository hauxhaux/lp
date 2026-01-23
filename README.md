# Install prereqs for creating a new theme (doesn't need to be run on new builds)

brew install pipx
pipx install plonecli

brew install uv

# running the live theming engine

cd src/plonetheme.lp/src/plonetheme/lp/theme

npm install        # only once per machine
npm run watch      # keep this running for live updates
