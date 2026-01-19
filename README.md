<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>termclock</h1>

<p>
  <strong>termclock</strong> is a modern animated clock for the terminal.
  It runs fully inside the terminal and looks clean, smooth, and readable.
  It is a simple and flexible alternative to tty-clock.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li>Smooth animated clock display</li>
  <li>Multiple built-in fonts</li>
  <li>Color customization</li>
  <li>Optional system information</li>
  <li>Optional date display</li>
  <li>CLI flags and config file support</li>
  <li>Low CPU usage</li>
  <li>Works on SSH and TTY</li>
</ul>

<hr>

<h2>Installation</h2>

<pre><code>cd termclock
chmod +x install.sh
./install.sh
</code></pre>

<p>The installer will:</p>
<ul>
  <li>Check Python version (Python 3.6+ required)</li>
  <li>Install required packages (<code>psutil</code>)</li>
  <li>Copy <code>termclock</code> to <code>/usr/local/bin</code></li>
  <li>Create a default configuration file</li>
</ul>

<p>After installation, run:</p>

<pre><code>termclock</code></pre>

<hr>

<h2>Usage</h2>

<pre><code>termclock                     # Default clock
termclock --help              # Show all options
termclock --font digital      # Change font
termclock --color green       # Change color
termclock --24h               # 24-hour format
termclock --date              # Show date
termclock --info              # Show system info
termclock --no-animation      # Disable animation
</code></pre>

<hr>

<h2>Keyboard Controls</h2>
<ul>
  <li><strong>q</strong> – Quit</li>
  <li><strong>f</strong> – Change font</li>
  <li><strong>r</strong> – Reload config</li>
</ul>

<hr>

<h2>Configuration File</h2>

<p>Config file location:</p>

<pre><code>~/.termclock.conf</code></pre>

<p>Example:</p>

<pre><code>font=block
color=cyan
format=24h
animation=true
date=false
info=false
</code></pre>

<p>Press <strong>r</strong> to reload the config while running.</p>

<hr>

<h2>Fonts</h2>

<p>Fonts use ASCII / Unicode art and are easy to extend.</p>

<h3>Block Font</h3>
<pre><code> ███   ███
█   █ █   █
█   █ █   █
█   █ █   █
 ███   ███
</code></pre>

<h3>Digital Font</h3>
<pre><code> _|_|_   _|_|_
   |       |
 _|_|_   _|_|_
 |           |
 _|_|_   _|_|_
</code></pre>

<h3>Slim Font</h3>
<pre><code> ┃  ┃
 ┃  ┃
 ┃  ┃
</code></pre>

<h3>Dots Font</h3>
<pre><code> ●●●
   ●
 ●●●
 ●
 ●●●
</code></pre>

<h3>Available Fonts</h3>
<ul>
  <li><code>block</code> – big and bold</li>
  <li><code>slim</code> – narrow and clean</li>
  <li><code>digital</code> – LED style</li>
  <li><code>rounded</code> – smooth Unicode</li>
  <li><code>ascii</code> – classic ASCII</li>
  <li><code>outline</code> – border style</li>
  <li><code>star</code> – star-filled</li>
  <li><code>braille</code> – braille pattern</li>
  <li><code>dots</code> – dot-based</li>
</ul>

<p>Change font:</p>
<pre><code>termclock --font block</code></pre>

<hr>

<h2>Animations</h2>

<ul>
  <li>Digits slide smoothly when time changes</li>
  <li>Optional fade effect</li>
  <li>No screen flicker</li>
  <li>Frame rate limited to save CPU</li>
</ul>

<p>Disable animation:</p>
<pre><code>termclock --no-animation</code></pre>

<hr>

<h2>System Information (Optional)</h2>

<p>When enabled, termclock can show:</p>
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

<h2>Colors</h2>

<pre><code>black, red, green, yellow,
blue, magenta, cyan, white
</code></pre>

<p>Example:</p>
<pre><code>termclock --color cyan</code></pre>

<hr>

<h2>Performance</h2>
<ul>
  <li>CPU usage usually under 2%</li>
  <li>Stable refresh loop</li>
  <li>Works over SSH</li>
  <li>Handles terminal resize correctly</li>
</ul>

<hr>

<h2>Requirements</h2>
<ul>
  <li>Python 3.6 or newer</li>
  <li><code>curses</code> (usually preinstalled)</li>
  <li><code>psutil</code> (optional, for system info)</li>
</ul>

<hr>

<h2>Uninstall</h2>

<pre><code>./uninstall.sh</code></pre>

<hr>

<h2>License</h2>

<p>MIT License</p>

</body>
</html>
