#!/usr/bin/env bash
# setup_labels.sh
# Create/update labels in the current GitHub repo using the gh CLI.
# Requires: gh auth login

set -euo pipefail

YAML_FILE=".github/labels.yml"
if [ ! -f "$YAML_FILE" ]; then
  echo "Missing $YAML_FILE"
  exit 1
fi

# Ensure jq and yq are available
if ! command -v yq >/dev/null 2>&1; then
  echo "This script requires yq. Install from https://mikefarah.gitbook.io/yq/"
  exit 1
fi
if ! command -v jq >/dev/null 2>&1; then
  echo "This script requires jq."
  exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  echo "This script requires GitHub CLI (gh)."
  exit 1
fi

count=$(yq '. | length' "$YAML_FILE")
for i in $(seq 0 $((count - 1))); do
  name=$(yq ".[$i].name" "$YAML_FILE")
  color=$(yq ".[$i].color" "$YAML_FILE")
  desc=$(yq ".[$i].description" "$YAML_FILE")

  # Create or update
  if gh label list --limit 200 --json name | jq -r '.[].name' | grep -Fxq "$name"; then
    echo "Updating label: $name"
    gh label edit "$name" --color "$color" --description "$desc"
  else
    echo "Creating label: $name"
    gh label create "$name" --color "$color" --description "$desc" || true
  fi
done

echo "Labels synchronized."
