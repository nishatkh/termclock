<h1 align="center">⏰ termclock</h1>

<p align="center">
  A modern terminal clock with smooth animations and clean fonts.<br>
  A simple and customizable alternative to tty-clock.
</p>

<p align="center">
  <code>Python</code> · <code>Terminal</code> · <code>ASCII Fonts</code> · <code>Low CPU</code>
</p>

<hr>

<h2>✨ Features</h2>

<ul>
  <li>Animated terminal clock</li>
  <li>Multiple ASCII and Unicode fonts</li>
  <li>Color customization</li>
  <li>Optional system information</li>
  <li>Optional date display</li>
  <li>Config file and CLI flags</li>
  <li>Works on SSH and TTY</li>
</ul>

<hr>

<h2>📦 Installation</h2>

<pre><code>cd termclock
chmod +x install.sh
./install.sh
</code></pre>

<p>The installer will:</p>

<ul>
  <li>Check Python version (3.6+)</li>
  <li>Install <code>psutil</code></li>
  <li>Copy binary to <code>/usr/local/bin</code></li>
  <li>Create default config</li>
</ul>

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

<h2>⌨️ Controls</h2>

<ul>
  <li><strong>q</strong> — Quit</li>
  <li><strong>f</strong> — Change font</li>
  <li><strong>r</strong> — Reload config</li>
</ul>

<hr>

<h2>⚙️ Configuration</h2>

<p>Config file location:</p>

<pre><code>~/.termclock.conf
</code></pre>

<p>Example:</p>

<pre><code>font=block
color=cyan
format=24h
animation=true
date=false
info=false
</code></pre>

<hr>

<h2>🔠 Fonts Preview</h2>

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
  <li>Optional fade effect</li>
  <li>No flicker</li>
  <li>Low refresh rate to save CPU</li>
</ul>

<p>Disable animations:</p>

<pre><code>termclock --no-animation
</code></pre>

<hr>

<h2>📊 System Info</h2>

<ul>
  <li>CPU usage</li>
  <li>RAM usage</li>
  <li>Disk usage</li>
  <li>Battery level</li>
  <li>Network activity</li>
</ul>

<p>Enable:</p>

<pre><code>termclock --info
</code></pre>

<hr>

<h2>🎨 Colors</h2>

<pre><code>black red green yellow
blue magenta cyan white
</code></pre>

<hr>

<h2>⚡ Performance</h2>

<ul>
  <li>CPU usage under 2%</li>
  <li>Stable refresh loop</li>
  <li>Handles terminal resize</li>
</ul>

<hr>

<h2>📋 Requirements</h2>

<ul>
  <li>Python 3.6+</li>
  <li><code>curses</code></li>
  <li><code>psutil</code> (optional)</li>
</ul>

<hr>

<h2>🗑️ Uninstall</h2>

<pre><code>./uninstall.sh
</code></pre>

<hr>

<h2>📄 License</h2>

<p>MIT License</p>
