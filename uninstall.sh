#!/bin/bash

# termclock universal uninstaller script

set -e  # Exit on any error

echo "Uninstalling termclock..."

# Detect operating system
OS_TYPE="$(uname -s | tr '[:upper:]' '[:lower:]')"
echo "Detected OS: $OS_TYPE"

# Determine appropriate installation directory based on OS
if [[ "$OS_TYPE" == *darwin* ]]; then
    # macOS
    INSTALL_DIR="/usr/local/bin"
elif [[ "$OS_TYPE" == *linux* ]]; then
    # Linux
    INSTALL_DIR="/usr/local/bin"
elif [[ "$OS_TYPE" == *bsd* ]]; then
    # BSD
    INSTALL_DIR="/usr/local/bin"
else
    # Default
    INSTALL_DIR="/usr/local/bin"
fi

TARGET="$INSTALL_DIR/termclock"

if [ -f "$TARGET" ]; then
    if [ -w "$INSTALL_DIR" ]; then
        rm "$TARGET"
        echo "Removed termclock from $INSTALL_DIR"
    else
        # Try with sudo
        if command -v sudo &> /dev/null; then
            sudo rm "$TARGET"
            echo "Removed termclock from $INSTALL_DIR"
        else
            echo "Error: Cannot remove from $INSTALL_DIR. Neither direct write access nor sudo available."
            exit 1
        fi
    fi
else
    echo "termclock not found in $INSTALL_DIR"
fi

# Remove configuration directory
CONFIG_DIR="$HOME/.config/termclock"
if [ -d "$CONFIG_DIR" ]; then
    rm -rf "$CONFIG_DIR"
    echo "Removed configuration directory: $CONFIG_DIR"
fi

# Remove config file
CONFIG_FILE="$HOME/.termclock.conf"
if [ -f "$CONFIG_FILE" ]; then
    rm "$CONFIG_FILE"
    echo "Removed config file: $CONFIG_FILE"
fi

echo ""
echo "Uninstallation complete!"
echo "termclock has been successfully uninstalled."