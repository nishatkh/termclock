#!/usr/bin/env python3
"""
Setup script for termclock - A modern animated terminal clock
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """Check if Python 3.6+ is available"""
    if sys.version_info < (3, 6):
        print(f"Error: Python 3.6 or higher is required. Found version: {'.'.join(map(str, sys.version_info[:2]))}")
        return False
    return True

def install_dependencies():
    """Try to install required dependencies"""
    print("Installing required Python packages...")
    
    try:
        import psutil
        print("psutil is already installed.")
    except ImportError:
        print("psutil not found, attempting to install...")
        try:
            # Try different methods to install psutil
            subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
            print("psutil installed successfully!")
        except subprocess.CalledProcessError:
            try:
                subprocess.check_call(["pip3", "install", "psutil"])
                print("psutil installed successfully!")
            except subprocess.CalledProcessError:
                print("Warning: Could not install psutil. System info features will be disabled.")
                return False
    return True

def install_termclock():
    """Install termclock to system path"""
    # Find a suitable installation directory
    possible_dirs = [
        "/usr/local/bin",  # Standard Unix/Linux/macOS
        "/opt/bin",        # Alternative Unix location
    ]
    
    # Add user-specific directories
    home_bin = os.path.expanduser("~/bin")
    possible_dirs.insert(0, home_bin)
    
    install_dir = None
    for d in possible_dirs:
        if os.path.isdir(d) and os.access(d, os.W_OK):
            install_dir = d
            break
    
    if install_dir is None:
        # If no writable system directory found, try to use sudo
        for d in possible_dirs:
            if os.path.isdir(d):
                install_dir = d
                break
    
    if install_dir is None:
        print("Error: Could not find a suitable installation directory.")
        return False
    
    # Copy the main script
    source_script = Path("termclock.py")
    target_script = Path(install_dir) / "termclock"
    
    try:
        shutil.copy2(source_script, target_script)
        target_script.chmod(0o755)  # Make executable
        print(f"termclock installed successfully to {target_script}")
        return True
    except PermissionError:
        # Try with sudo if direct write fails
        try:
            subprocess.check_call(["sudo", "cp", str(source_script), str(target_script)])
            subprocess.check_call(["sudo", "chmod", "+x", str(target_script)])
            print(f"termclock installed successfully to {target_script} (using sudo)")
            return True
        except subprocess.CalledProcessError:
            print(f"Error: Could not install to {install_dir}. Permission denied.")
            return False
    except Exception as e:
        print(f"Error installing termclock: {e}")
        return False

def create_config_directories():
    """Create configuration directories and copy assets"""
    config_dir = Path.home() / ".config" / "termclock"
    fonts_dir = config_dir / "fonts"
    themes_dir = config_dir / "themes"
    
    try:
        fonts_dir.mkdir(parents=True, exist_ok=True)
        themes_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created configuration directory: {config_dir}")
        
        # Copy font files
        source_fonts = Path("fonts")
        if source_fonts.exists():
            for font_file in source_fonts.glob("*.font"):
                shutil.copy2(font_file, fonts_dir / font_file.name)
        
        # Copy theme files
        source_themes = Path("themes")
        if source_themes.exists():
            for theme_file in source_themes.glob("*.theme"):
                shutil.copy2(theme_file, themes_dir / theme_file.name)
                
        print("Copied fonts and themes to configuration directory.")
        return True
    except Exception as e:
        print(f"Warning: Could not create configuration directories: {e}")
        return False

def main():
    print("Installing termclock...")
    
    if not check_python_version():
        return 1
    
    if not install_dependencies():
        # Continue anyway, as psutil is optional
        pass
    
    if not install_termclock():
        return 1
    
    create_config_directories()
    
    # Create default config if it doesn't exist
    config_file = Path.home() / ".termclock.conf"
    if not config_file.exists():
        default_config = """# termclock configuration file
font=block
color=cyan
format=24h
animation=true
date=false
info=false
"""
        try:
            with open(config_file, 'w') as f:
                f.write(default_config)
            print(f"Created default config file at {config_file}")
        except Exception as e:
            print(f"Warning: Could not create default config file: {e}")
    
    print("\nInstallation complete!")
    print("Run 'termclock' to start the animated terminal clock.")
    print("")
    print("Available options:")
    print("  termclock --help          Show all options")
    print("  termclock --font block    Use different fonts: block, slim, digital, rounded, ascii, outline, star, braille, dots")
    print("  termclock --color cyan    Change color: red, green, yellow, blue, magenta, cyan, white")
    print("  termclock --24h           Use 24-hour format")
    print("  termclock --date          Show date")
    print("  termclock --info          Show system info")
    print("  termclock --no-animation  Disable animations")
    print("")
    print("Configuration file is located at ~/.termclock.conf")
    print("Press q to quit, f to cycle fonts, r to reload config")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())