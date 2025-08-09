#/bin/bash

set -e 
REPO_URL="http://localhost:3002/Amir/ToDo-CLI.git"
CLONE_DIR="/tmp/todo-install"

if [ -d "$CLONE_DIR/.git" ]; then
  echo "Updating existing repository"
  git -C "$CLONE_DIR" pull
else
  echo "Cloning repository..."
  git clone "$REPO_URL" "$CLONE_DIR"
fi

chmod +x "$CLONE_DIR/todo.py"
sudo cp "$CLONE_DIR/todo.py" "/usr/local/bin/todo"

echo "Installed todo script! You can now run 'todo' from Anywhere!"
