#!/bin/bash

# termclock universal installer script

set -e  # Exit on any error

echo "Installing termclock..."

# Detect operating system
OS_TYPE="$(uname -s | tr '[:upper:]' '[:lower:]')"
echo "Detected OS: $OS_TYPE"

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
MIN_VERSION="3.6"

if [[ $(printf '%s\n' "$MIN_VERSION" "$PYTHON_VERSION" | sort -V | head -n1) == "$MIN_VERSION" ]]; then
    echo "Python version $PYTHON_VERSION detected. ✓"
else
    echo "Error: Python 3.6 or higher is required. Found version: $PYTHON_VERSION"
    exit 1
fi

# Install required Python packages based on OS
echo "Installing required Python packages..."

# Try multiple approaches for installing psutil depending on the OS
echo "Detecting package manager for Python dependencies..."

if command -v apt-get &> /dev/null; then
    # Debian/Ubuntu
    echo "Detected Debian-based system, attempting to install python3-psutil via apt..."
    if command -v sudo &> /dev/null; then
        sudo apt-get update && sudo apt-get install -y python3-psutil 2>/dev/null || {
            echo "Could not install python3-psutil via apt, trying pip..."
            python3 -m pip install psutil 2>/dev/null || {
                pip3 install psutil 2>/dev/null || {
                    echo "Warning: Could not install psutil. System info features will be disabled."
                }
            }
        }
    else
        python3 -m pip install psutil 2>/dev/null || {
            pip3 install psutil 2>/dev/null || {
                echo "Warning: Could not install psutil. System info features will be disabled."
            }
        }
    fi
elif command -v yum &> /dev/null; then
    # RHEL/CentOS/Fedora
    echo "Detected Red Hat-based system, attempting to install python3-psutil via yum..."
    if command -v sudo &> /dev/null; then
        sudo yum install -y python3-psutil 2>/dev/null || {
            echo "Could not install python3-psutil via yum, trying pip..."
            python3 -m pip install psutil 2>/dev/null || {
                pip3 install psutil 2>/dev/null || {
                    echo "Warning: Could not install psutil. System info features will be disabled."
                }
            }
        }
    else
        python3 -m pip install psutil 2>/dev/null || {
            pip3 install psutil 2>/dev/null || {
                echo "Warning: Could not install psutil. System info features will be disabled."
            }
        }
    fi
elif command -v pacman &> /dev/null; then
    # Arch Linux
    echo "Detected Arch-based system, attempting to install python-psutil via pacman..."
    if command -v sudo &> /dev/null; then
        sudo pacman -S python-psutil --noconfirm 2>/dev/null || {
            echo "Could not install python-psutil via pacman, trying pip..."
            python3 -m pip install psutil 2>/dev/null || {
                pip3 install psutil 2>/dev/null || {
                    echo "Warning: Could not install psutil. System info features will be disabled."
                }
            }
        }
    else
        python3 -m pip install psutil 2>/dev/null || {
            pip3 install psutil 2>/dev/null || {
                echo "Warning: Could not install psutil. System info features will be disabled."
            }
        }
    fi
elif command -v brew &> /dev/null; then
    # macOS
    echo "Detected macOS, attempting to install python3-psutil via brew..."
    if command -v sudo &> /dev/null; then
        brew install python3-psutil 2>/dev/null || {
            echo "Could not install python3-psutil via brew, trying pip..."
            python3 -m pip install psutil 2>/dev/null || {
                pip3 install psutil 2>/dev/null || {
                    echo "Warning: Could not install psutil. System info features will be disabled."
                }
            }
        }
    else
        python3 -m pip install psutil 2>/dev/null || {
            pip3 install psutil 2>/dev/null || {
                echo "Warning: Could not install psutil. System info features will be disabled."
            }
        }
    fi
else
    # Generic fallback
    echo "Unknown system, trying pip..."
    python3 -m pip install psutil 2>/dev/null || {
        pip3 install psutil 2>/dev/null || {
            echo "Warning: Could not install psutil. System info features will be disabled."
        }
    }
fi

# Make the main script executable
chmod +x termclock.py

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

# Check if we have write permissions
if [ -w "$INSTALL_DIR" ]; then
    cp termclock.py "$TARGET"
    chmod +x "$TARGET"
    echo "termclock installed successfully to $TARGET"
else
    # Try with sudo
    if command -v sudo &> /dev/null; then
        sudo cp termclock.py "$TARGET"
        sudo chmod +x "$TARGET"
        echo "termclock installed successfully to $TARGET"
    else
        echo "Error: Cannot copy to $INSTALL_DIR. Neither direct write access nor sudo available."
        exit 1
    fi
fi

# Copy fonts and themes directories
CONFIG_DIR="$HOME/.config/termclock"
echo "Creating configuration directory: $CONFIG_DIR"
mkdir -p "$CONFIG_DIR/fonts" "$CONFIG_DIR/themes"

# Copy font files
cp -r fonts/* "$CONFIG_DIR/fonts/" 2>/dev/null || echo "No font files to copy"
cp -r themes/* "$CONFIG_DIR/themes/" 2>/dev/null || echo "No theme files to copy"

echo ""
echo "Installation complete!"
echo "Run 'termclock' to start the animated terminal clock."
echo ""
echo "Available options:"
echo "  termclock --help          Show all options"
echo "  termclock --font block    Use different fonts: block, slim, digital, rounded, ascii, outline, star, braille, dots"
echo "  termclock --color cyan    Change color: red, green, yellow, blue, magenta, cyan, white"
echo "  termclock --24h           Use 24-hour format"
echo "  termclock --date          Show date"
echo "  termclock --info          Show system info"
echo "  termclock --no-animation  Disable animations"
echo ""
echo "Configuration file is located at ~/.termclock.conf"
echo "Press q to quit, f to cycle fonts, r to reload config"