#!/bin/bash
set -e

BINARY_NAME="main"
INSTALL_PATH="/usr/local/bin/todo"  # change if needed

echo "Fetching latest release download URL..."

# Get JSON from GitHub API and extract URL for the asset named "main"
DOWNLOAD_URL=$(curl -s "https://api.github.com/repos/Amir-jpg-png/ToDo-CLI/releases/latest" \
  | grep "browser_download_url" \
  | grep "$BINARY_NAME" \
  | head -n 1 \
  | sed -E 's/.*"([^"]+)".*/\1/')

if [[ -z "$DOWNLOAD_URL" ]]; then
  echo "Error: Could not find download URL for $BINARY_NAME"
  exit 1
fi

echo "Downloading $BINARY_NAME from $DOWNLOAD_URL ..."
curl -L -o "$BINARY_NAME" "$DOWNLOAD_URL"

echo "Making binary executable..."
chmod +x "$BINARY_NAME"

echo "Moving binary to $INSTALL_PATH (requires sudo)..."
sudo mv "$BINARY_NAME" "$INSTALL_PATH"

echo "Done! You can now run 'todo' from the command line."
