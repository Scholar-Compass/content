set dotenv-load := true

python := env_var_or_default('PYTHON', 'python')
pip := python + " -m pip"
mkdocs := python + " -m mkdocs"

# List available recipes
@default:
    just --list

# Install/upgrade MkDocs, its plugins, and markdown extensions
bootstrap:
    {{ pip }} install mkdocs --upgrade
    {{ pip }} install $({{ mkdocs }} get-deps) --upgrade

# Start the live-reloading docs server
serve *ARGS:
    {{ mkdocs }} serve {{ ARGS }}

# Build the docs site
build *ARGS:
    {{ mkdocs }} build {{ ARGS }}
