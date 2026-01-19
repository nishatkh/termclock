# termclock

A modern, animated terminal clock that runs fully inside your terminal. A clean, customizable, and efficient alternative to tty-clock with smooth animations and system information display.

## Features

- **Animated Display**: Smooth digit transitions and animations
- **Multiple Fonts**: Block, slim, digital, and rounded fonts
- **Customizable Colors**: Various color options for the clock
- **System Info**: CPU, RAM, disk, battery, and network usage
- **Date Display**: Shows current date
- **Configurable**: Both CLI arguments and config file support
- **Efficient**: Low CPU usage, works on SSH and TTY

## Installation

```bash
cd termclock
chmod +x install.sh
./install.sh
```

The installer will:
- Check Python version (requires Python 3.6+)
- Install required packages (psutil)
- Copy the binary to `/usr/local/bin`
- Create default configuration

## Usage

```bash
termclock                    # Run with default settings
termclock --help            # Show all options
termclock --font digital    # Use digital font
termclock --color green     # Use green color
termclock --24h             # Use 24-hour format
termclock --date            # Show date
termclock --info            # Show system info
termclock --no-animation    # Disable animations
```

## Controls

- `q` - Quit the application
- `f` - Cycle through available fonts
- `r` - Reload configuration file

## Configuration File

The configuration file is located at `~/.termclock.conf`. Example:

```ini
font=block
color=cyan
format=24h
animation=true
date=false
info=false
```

## Customization

### Fonts
- `block` - Big, bold, clear digits
- `slim` - Minimal and narrow
- `digital` - Classic LED style
- `rounded` - Soft Unicode curves
- `ascii` - Stylish ASCII art inspired
- `outline` - Outline-style characters
- `star` - Star-filled digits
- `braille` - Braille pattern style
- `dots` - Dot pattern style

### Colors
- `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`

## Uninstallation

```bash
./uninstall.sh
```

## Performance

- CPU usage typically below 2%
- Stable refresh loop
- Works on SSH and TTY terminals
- Resizes properly with terminal window

## Requirements

- Python 3.6+
- `curses` module (usually comes with Python)
- `psutil` for system information (optional but recommended)

## License

MIT License