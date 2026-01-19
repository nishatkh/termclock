<h1 align="center">
  ⏰ termclock – Animated Terminal Clock for Linux & SSH
</h1>

<p align="center">
  A fast and lightweight <strong>animated terminal clock</strong> written in Python.<br>
  A modern <strong>tty-clock alternative</strong> with ASCII fonts, smooth animations,
  and optional system information.
</p>

<p align="center">
  <strong>terminal clock</strong> ·
  <strong>animated terminal app</strong> ·
  <strong>tty-clock alternative</strong> ·
  <strong>linux terminal clock</strong> ·
  <strong>python terminal UI</strong>
</p>

<hr>

<h2>📌 What is termclock?</h2>

<p>
  <strong>termclock</strong> is a modern animated terminal clock designed for
  Linux, macOS, SSH, and TTY environments. It runs fully inside the terminal
  and focuses on clean visuals, smooth animations, and low CPU usage.
</p>

<p>
  It is written in Python and works as a lightweight alternative to tty-clock,
  while offering better customization, multiple ASCII fonts, color themes,
  and optional system monitoring.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
  <li>Animated terminal clock with smooth transitions</li>
  <li>Multiple ASCII and Unicode fonts</li>
  <li>Customizable colors and themes</li>
  <li>Optional date display</li>
  <li>Optional system info (CPU, RAM, disk, battery, network)</li>
  <li>CLI flags and config file support</li>
  <li>Low CPU usage</li>
  <li>Works on SSH, TTY, and local terminals</li>
</ul>

<hr>

<h2>📦 Installation</h2>

<pre><code>cd termclock
chmod +x install.sh
./install.sh
</code></pre>

<p>The installer will:</p>

<ul>
  <li>Check Python version (Python 3.6+ required)</li>
  <li>Install <code>psutil</code> if missing</li>
  <li>Copy <code>termclock</code> to <code>/usr/local/bin</code></li>
  <li>Create a default configuration file</li>
</ul>

<p>After installation, run:</p>

<pre><code>termclock</code></pre>

<hr>

<h2>🚀 Usage</h2>

<pre><code>termclock
termclock --help
termclock --font digital
termclock --color cyan
termclock --24h
termclock --date
termclock --info
termclock --no-animation
</code></pre>

<hr>

<h2>⌨️ Keyboard Controls</h2>

<ul>
  <li><strong>q</strong> — Quit</li>
  <li><strong>f</strong> — Cycle fonts</li>
  <li><strong>r</strong> — Reload configuration</li>
</ul>

<hr>

<h2>⚙️ Configuration</h2>

<p>Configuration file location:</p>

<pre><code>~/.termclock.conf</code></pre>

<p>Example configuration:</p>

<pre><code>font=block
color=cyan
format=24h
animation=true
date=false
info=false
</code></pre>

<p>Press <strong>r</strong> to reload the config while the app is running.</p>

<hr>

<h2>🔠 Font Preview</h2>

<p><strong>Block</strong></p>
<pre><code> ███   ███
█   █ █   █
█   █ █   █
█   █ █   █
 ███   ███
</code></pre>

<p><strong>Digital</strong></p>
<pre><code> _|_|_   _|_|_
   |       |
 _|_|_   _|_|_
 |           |
 _|_|_   _|_|_
</code></pre>

<p><strong>Slim</strong></p>
<pre><code> ┃  ┃
 ┃  ┃
 ┃  ┃
</code></pre>

<p><strong>Dots</strong></p>
<pre><code> ●●●
   ●
 ●●●
 ●
 ●●●
</code></pre>

<p>Available fonts:</p>

<ul>
  <li><code>block</code></li>
  <li><code>slim</code></li>
  <li><code>digital</code></li>
  <li><code>rounded</code></li>
  <li><code>ascii</code></li>
  <li><code>outline</code></li>
  <li><code>star</code></li>
  <li><code>braille</code></li>
  <li><code>dots</code></li>
</ul>

<hr>

<h2>🎞️ Animations</h2>

<ul>
  <li>Smooth digit slide on time change</li>
  <li>Optional fade-style transition</li>
  <li>No flicker or screen tearing</li>
  <li>Frame rate limited for performance</li>
</ul>

<p>Disable animations:</p>

<pre><code>termclock --no-animation</code></pre>

<hr>

<h2>📊 System Information</h2>

<p>When enabled, termclock can display:</p>

<ul>
  <li>CPU usage</li>
  <li>RAM usage</li>
  <li>Disk usage</li>
  <li>Battery level (if available)</li>
  <li>Network activity</li>
</ul>

<p>Enable system info:</p>

<pre><code>termclock --info</code></pre>

<hr>

<h2>🎨 Colors</h2>

<pre><code>black  red  green  yellow
blue   magenta  cyan  white
</code></pre>

<hr>

<h2>⚡ Performance</h2>

<ul>
  <li>CPU usage usually below 2%</li>
  <li>Stable refresh loop</li>
  <li>Handles terminal resize correctly</li>
</ul>

<hr>

<h2>📋 Requirements</h2>

<ul>
  <li>Python 3.6 or newer</li>
  <li><code>curses</code> module (usually preinstalled)</li>
  <li><code>psutil</code> (optional, for system info)</li>
</ul>

<hr>

<h2>🗑️ Uninstall</h2>

<pre><code>./uninstall.sh</code></pre>

<hr>

<h2>📄 License</h2>

<p>MIT License</p>
