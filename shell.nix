{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312Full
    pkgs.python312Packages.virtualenv  # Provides `virtualenv` to create venvs
  ];

  shellHook = ''
    # Create or activate a virtual environment
    if [ ! -d ".venv" ]; then
      python3 -m venv .venv
    fi
    source .venv/bin/activate

    # Ensure pip is up-to-date
    pip install --upgrade pip

    # Install pygame if it's not already installed
    if ! python -c "import pygame" &> /dev/null; then
      pip install pygame
    fi

    echo "Virtual environment activated with pygame installed."
  '';
}

