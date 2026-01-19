#!/usr/bin/env python3
"""
termclock - A modern, animated terminal clock
A clean, customizable alternative to tty-clock with smooth animations
and system information display.
"""

import os
import sys
import time
import curses
import argparse
from datetime import datetime
import json
import threading
from math import sin, pi
import math

class TerminalClock:
    def __init__(self):
        self.stdscr = None
        self.running = True
        self.animation_enabled = True
        self.format_24h = True
        self.show_date = False
        self.show_info = False
        self.current_font = "block"
        self.color = "cyan"
        self.bg_color = "black"
        self.font_data = {}
        self.config = {}
        
        # Animation variables
        self.last_time_shown = ""
        self.transition_progress = 0.0  # 0.0 to 1.0
        self.is_transitioning = False
        self.digit_positions = {}  # Store positions of digits for animation
        
        # Color mapping
        self.colors = {
            'black': curses.COLOR_BLACK,
            'red': curses.COLOR_RED,
            'green': curses.COLOR_GREEN,
            'yellow': curses.COLOR_YELLOW,
            'blue': curses.COLOR_BLUE,
            'magenta': curses.COLOR_MAGENTA,
            'cyan': curses.COLOR_CYAN,
            'white': curses.COLOR_WHITE
        }
        
        # Load default configuration
        self.load_default_config()
        
    def load_default_config(self):
        """Load default configuration values"""
        self.config = {
            'font': 'block',
            'color': 'cyan',
            'bg_color': 'black',
            'format': '24h',
            'animation': True,
            'date': False,
            'info': False
        }

    def load_config_file(self):
        """Load configuration from ~/.termclock.conf"""
        config_path = os.path.expanduser("~/.termclock.conf")
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            if '=' in line:
                                key, value = line.split('=', 1)
                                key = key.strip()
                                value = value.strip().strip('"\'')
                                
                                # Convert string values to appropriate types
                                if value.lower() in ['true', 'false']:
                                    value = value.lower() == 'true'
                                elif value.isdigit():
                                    value = int(value)
                                    
                                self.config[key] = value
            except Exception as e:
                print(f"Error loading config file: {e}")
                
    def save_default_config(self):
        """Save default configuration to ~/.termclock.conf if it doesn't exist"""
        config_path = os.path.expanduser("~/.termclock.conf")
        if not os.path.exists(config_path):
            default_config = """# termclock configuration file
font=block
color=cyan
format=24h
animation=true
date=false
info=false
"""
            try:
                with open(config_path, 'w') as f:
                    f.write(default_config)
                print(f"Created default config file at {config_path}")
            except Exception as e:
                print(f"Error creating default config file: {e}")

    def parse_arguments(self):
        """Parse command line arguments"""
        parser = argparse.ArgumentParser(description='A modern animated terminal clock')
        parser.add_argument('--font', help='Font to use (block, slim, digital, rounded, ascii, outline, star, braille, dots)')
        parser.add_argument('--color', help='Main color (cyan, green, yellow, red, blue, magenta, white)')
        parser.add_argument('--bg', help='Background color')
        parser.add_argument('--24h', dest='format_24h', action='store_true', help='Use 24-hour format')
        parser.add_argument('--12h', dest='format_12h', action='store_true', help='Use 12-hour format')
        parser.add_argument('--no-animation', action='store_true', help='Disable animations')
        parser.add_argument('--date', action='store_true', help='Show date')
        parser.add_argument('--info', action='store_true', help='Show system info')
        # Help is automatically provided by argparse, no need to define it manually
        
        args = parser.parse_args()
        
        # Override config with command line args
        if args.font:
            self.config['font'] = args.font
        if args.color:
            self.config['color'] = args.color
        if args.bg:
            self.config['bg_color'] = args.bg
        if args.format_12h:
            self.config['format'] = '12h'
        elif args.format_24h:
            self.config['format'] = '24h'
        if args.no_animation:
            self.config['animation'] = False
        if args.date:
            self.config['date'] = True
        if args.info:
            self.config['info'] = True
            
        # Apply config to instance variables
        self.current_font = self.config['font']
        self.color = self.config['color']
        self.bg_color = self.config['bg_color']
        self.animation_enabled = self.config['animation']
        self.show_date = self.config['date']
        self.show_info = self.config['info']
        self.format_24h = self.config['format'] == '24h'

    def load_fonts(self):
        """Load font data from font files"""
        fonts_dir = os.path.join(os.path.dirname(__file__), 'fonts')
        font_files = {
            'block': 'block.font',
            'slim': 'slim.font',
            'digital': 'digital.font',
            'rounded': 'rounded.font',
            'ascii': 'ascii.font',
            'outline': 'outline.font',
            'star': 'star.font',
            'braille': 'braille.font',
            'dots': 'dots.font'
        }
        
        for font_name, filename in font_files.items():
            filepath = os.path.join(fonts_dir, filename)
            if os.path.exists(filepath):
                try:
                    self.font_data[font_name] = self.load_font_file(filepath)
                except Exception as e:
                    print(f"Error loading font {font_name}: {e}")
                    # Load a default font if the file doesn't exist
                    self.font_data[font_name] = self.get_default_font()
            else:
                # Load a default font if the file doesn't exist
                self.font_data[font_name] = self.get_default_font()

    def get_default_font(self):
        """Return a default font if font file doesn't exist"""
        # Default block font
        return {
            '0': [
                " ███ ",
                "█   █",
                "█   █",
                "█   █",
                " ███ "
            ],
            '1': [
                "  █  ",
                " ██  ",
                "  █  ",
                "  █  ",
                " ███ "
            ],
            '2': [
                " ███ ",
                "    █",
                " ███ ",
                "█    ",
                " ███ "
            ],
            '3': [
                " ███ ",
                "    █",
                " ███ ",
                "    █",
                " ███ "
            ],
            '4': [
                "█   █",
                "█   █",
                " ███ ",
                "    █",
                "    █"
            ],
            '5': [
                " ███ ",
                "█    ",
                " ███ ",
                "    █",
                " ███ "
            ],
            '6': [
                " ███ ",
                "█    ",
                " ███ ",
                "█   █",
                " ███ "
            ],
            '7': [
                " ███ ",
                "    █",
                "   █ ",
                "  █  ",
                "  █  "
            ],
            '8': [
                " ███ ",
                "█   █",
                " ███ ",
                "█   █",
                " ███ "
            ],
            '9': [
                " ███ ",
                "█   █",
                " ███ ",
                "    █",
                " ███ "
            ],
            ':': [
                "     ",
                "  █  ",
                "     ",
                "  █  ",
                "     "
            ]
        }

    def load_font_file(self, filepath):
        """Load font from a .font file"""
        font = {}
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Parse the font file
        lines = content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line and ':' in line:
                char = line[0]  # Get the character (first char before colon)
                
                # Skip the header line
                i += 1
                
                # Read the character representation (typically 5 lines)
                char_lines = []
                for j in range(5):
                    if i + j < len(lines):
                        char_lines.append(lines[i + j])
                    else:
                        char_lines.append("")
                
                font[char] = char_lines
                i += 5  # Move to next character
            else:
                i += 1
                
        return font

    def init_curses(self):
        """Initialize curses settings"""
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        curses.curs_set(0)  # Hide cursor
        
        # Initialize color pairs
        for i, (name, color_val) in enumerate(self.colors.items(), 1):
            curses.init_pair(i, color_val, -1)
        
        # Set up color mapping for drawing
        self.main_color_pair = curses.color_pair(list(self.colors.keys()).index(self.color) + 1)
        self.default_color_pair = curses.color_pair(1)  # Default to white

    def cleanup_curses(self):
        """Clean up curses settings"""
        if self.stdscr:
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()

    def get_time_string(self):
        """Get current time as formatted string"""
        now = datetime.now()
        if self.format_24h:
            return now.strftime("%H:%M:%S")
        else:
            return now.strftime("%I:%M:%S %p")

    def get_date_string(self):
        """Get current date as formatted string"""
        now = datetime.now()
        return now.strftime("%A, %B %d, %Y")

    def get_system_info(self):
        """Get system information (CPU, RAM, Battery)"""
        try:
            import psutil
            
            # Get CPU usage
            cpu_percent = psutil.cpu_percent(interval=0.1)  # Short interval for responsiveness
            
            # Get RAM usage
            ram = psutil.virtual_memory()
            ram_percent = ram.percent
            
            # Get disk usage for root directory
            disk_usage = psutil.disk_usage('/')
            disk_percent = int((disk_usage.used / disk_usage.total) * 100)
            
            # Battery info (if available)
            battery = None
            battery_str = "Battery: N/A"
            if hasattr(psutil, "sensors_battery"):
                battery = psutil.sensors_battery()
                if battery is not None:
                    battery_percent = int(battery.percent)
                    if battery.power_plugged:
                        battery_str = f"Battery: {battery_percent}% (Charging)"
                    else:
                        battery_str = f"Battery: {battery_percent}%"
            else:
                # On some systems, battery info isn't available through sensors_battery
                # We can try another approach or just show N/A
                battery_str = "Battery: N/A"
            
            # Network I/O stats (showing total since boot)
            net_io = psutil.net_io_counters()
            network_info = f"Net: Rx+Tx {(net_io.bytes_recv + net_io.bytes_sent) // (1024*1024)}MB"
            
            return {
                'cpu': f"CPU: {cpu_percent}%",
                'ram': f"RAM: {ram_percent}%",
                'disk': f"Disk: {disk_percent}%",
                'battery': battery_str,
                'network': network_info
            }
        except ImportError:
            # psutil not installed
            return {
                'cpu': "CPU: N/A (psutil req)",
                'ram': "RAM: N/A (psutil req)",
                'disk': "Disk: N/A (psutil req)",
                'battery': "Battery: N/A (psutil req)",
                'network': "Network: N/A (psutil req)"
            }
        except Exception as e:
            # Handle any other error
            return {
                'cpu': f"CPU: Error ({str(e)})",
                'ram': "RAM: Error",
                'disk': "Disk: Error",
                'battery': "Battery: Error",
                'network': "Network: Error"
            }

    def interpolate_digits(self, old_digit, new_digit, progress):
        """Interpolate between two digits for smooth transition"""
        font = self.font_data.get(self.current_font, {})
        old_rep = font.get(old_digit, font.get('0', self.get_default_font()['0']))
        new_rep = font.get(new_digit, font.get('0', self.get_default_font()['0']))
        
        result = []
        for i in range(len(old_rep)):
            old_line = old_rep[i]
            new_line = new_rep[i]
            interpolated_line = ""
            for j in range(len(old_line)):
                # Simple fade effect - blend characters based on progress
                if progress < 0.5 and old_line[j] != ' ':
                    interpolated_line += old_line[j]
                elif progress >= 0.5 and new_line[j] != ' ':
                    interpolated_line += new_line[j]
                else:
                    # Blend gradually
                    if progress > 0.3 and new_line[j] != ' ':
                        interpolated_line += new_line[j]
                    else:
                        interpolated_line += old_line[j]
            result.append(interpolated_line)
        return result

    def draw_digit(self, y, x, digit_char, color_pair=None, alpha=1.0):
        """Draw a single digit using the loaded font"""
        if color_pair is None:
            color_pair = self.main_color_pair
            
        font = self.font_data.get(self.current_font, {})
        digit_representation = font.get(digit_char, font.get('0', self.get_default_font()['0']))
        
        # If alpha is less than 1, we're fading
        if alpha < 1.0:
            for i, line in enumerate(digit_representation):
                if y + i < curses.LINES:
                    # Apply fading effect
                    faded_line = ""
                    for ch in line:
                        if ch != ' ' and alpha > 0.3:
                            faded_line += ch
                        else:
                            faded_line += ' '
                    self.stdscr.addstr(y + i, x, faded_line, color_pair)
        else:
            for i, line in enumerate(digit_representation):
                if y + i < curses.LINES:
                    self.stdscr.addstr(y + i, x, line, color_pair)
    
    def draw_interpolated_digit(self, y, x, old_digit, new_digit, progress, color_pair=None):
        """Draw a digit that's transitioning between old and new values"""
        if color_pair is None:
            color_pair = self.main_color_pair
            
        interpolated_rep = self.interpolate_digits(old_digit, new_digit, progress)
        
        for i, line in enumerate(interpolated_rep):
            if y + i < curses.LINES:
                self.stdscr.addstr(y + i, x, line, color_pair)

    def draw_clock(self, time_str):
        """Draw the clock with the given time string"""
        # Clear screen
        self.stdscr.clear()
        
        # Calculate center position
        max_height = 5  # Height of digit representation
        time_width = 0
        for char in time_str:
            if char != ' ':
                time_width += 5  # Width of each digit
            else:
                time_width += 2  # Space width
                
        start_x = (curses.COLS - time_width) // 2
        start_y = (curses.LINES - max_height) // 2
        
        # Check if we need to animate transition
        if self.animation_enabled and self.last_time_shown and self.last_time_shown != time_str:
            self.is_transitioning = True
            self.transition_progress += 0.1  # Increase progress each frame
            if self.transition_progress >= 1.0:
                self.transition_progress = 0.0
                self.is_transitioning = False
                self.last_time_shown = time_str
        else:
            self.last_time_shown = time_str
            
        # Draw each character
        current_x = start_x
        for i, char in enumerate(time_str):
            if char == ' ':
                current_x += 2  # Add space width
            else:
                # Store position for animation
                pos_key = f"{i}_{char}"
                self.digit_positions[pos_key] = (start_y, current_x)
                
                if self.is_transitioning and i < len(self.last_time_shown):
                    old_char = self.last_time_shown[i] if i < len(self.last_time_shown) else ' '
                    self.draw_interpolated_digit(start_y, current_x, old_char, char, self.transition_progress)
                else:
                    self.draw_digit(start_y, current_x, char)
                current_x += 5  # Move to next digit position

    def draw_date(self):
        """Draw the date below the clock"""
        if not self.show_date:
            return
            
        date_str = self.get_date_string()
        x_pos = (curses.COLS - len(date_str)) // 2
        y_pos = (curses.LINES - 5) // 2 + 6  # Below the clock
        
        if y_pos < curses.LINES:
            self.stdscr.addstr(y_pos, x_pos, date_str, self.main_color_pair)

    def draw_info(self):
        """Draw system information panel"""
        if not self.show_info:
            return
            
        info = self.get_system_info()
        info_lines = [info['cpu'], info['ram'], info['disk'], info['battery'], info['network']]
        
        # Position info panel at top right
        panel_start_col = curses.COLS - 25  # Start from right side
        for i, line in enumerate(info_lines):
            if i + 2 < curses.LINES and panel_start_col > 0:
                self.stdscr.addstr(i + 2, max(0, panel_start_col), line, self.main_color_pair)

    def handle_input(self):
        """Handle keyboard input"""
        try:
            # Use nodelay to avoid blocking, but with a small timeout
            self.stdscr.nodelay(True)
            key = self.stdscr.getch()
            self.stdscr.nodelay(False)  # Reset to blocking mode
            
            if key != -1:  # Only process if a key was pressed
                if key == ord('q') or key == 27:  # q or ESC to quit
                    self.running = False
                elif key == ord('r'):  # r to reload config
                    self.load_config_file()
                    # Reapply settings
                    self.current_font = self.config['font']
                    self.color = self.config['color']
                    self.bg_color = self.config['bg_color']
                    self.animation_enabled = self.config['animation']
                    self.show_date = self.config['date']
                    self.show_info = self.config['info']
                    self.format_24h = self.config['format'] == '24h'
                elif key == ord('f'):  # f to cycle fonts
                    font_list = list(self.font_data.keys())
                    current_idx = font_list.index(self.current_font) if self.current_font in font_list else 0
                    next_idx = (current_idx + 1) % len(font_list)
                    self.current_font = font_list[next_idx]
        except:
            pass  # Ignore errors in input handling

    def run(self):
        """Main run loop"""
        try:
            self.save_default_config()  # Create default config if needed
            self.load_config_file()
            self.parse_arguments()
            self.load_fonts()
            self.init_curses()
            
            last_time = ""
            animation_counter = 0
            
            while self.running:
                # Handle input
                self.handle_input()
                
                # Get current time
                current_time = self.get_time_string()
                
                # Only redraw if time changed (or for animation effect)
                if current_time != last_time or self.animation_enabled:
                    self.draw_clock(current_time)
                    self.draw_date()
                    self.draw_info()
                    
                    self.stdscr.refresh()
                    last_time = current_time
                
                # Check for terminal resize
                curses.update_lines_cols()
                
                # Control refresh rate (about 10 FPS for smooth animation)
                # If animating, update more frequently
                if self.is_transitioning:
                    time.sleep(0.05)  # More frequent updates during animation
                else:
                    time.sleep(0.1)
                
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup_curses()

def main():
    clock = TerminalClock()
    clock.run()


if __name__ == "__main__":
    main()
