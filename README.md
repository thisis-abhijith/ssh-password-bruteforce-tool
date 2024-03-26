<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<h1>SSH Password Brute-Force Tool</h1>

<h2>Overview</h2>
<p>This Python script is designed to perform a brute-force attack on SSH authentication using a list of common passwords. It utilizes the paramiko library for SSH connections and can be used for educational purposes or in controlled environments where authorized testing is permitted.</p>

<h2>Features</h2>
<ul>
  <li><strong>SSH Brute-Force:</strong> The script attempts to authenticate to an SSH server using a provided username and a list of common passwords.</li>
  <li><strong>Customization:</strong> Users can specify the target host IP, username, and the filename containing a list of passwords.</li>
  <li><strong>Logging:</strong> The script logs the attempted passwords and reports if a valid password is found.</li>
</ul>

<h2>Usage</h2>
<ol>
  <li>Ensure you have Python installed on your system.</li>
  <li>Install the paramiko library using <code>pip install paramiko</code>.</li>
  <li>Prepare a text file containing common passwords (e.g., <code>ssh-common-passwords.txt</code>).</li>
  <li>Modify the <code>host</code>, <code>username</code>, and <code>password_list</code> variables in the script to match your target.</li>
  <li>Run the script using <code>python ssh_brute_force.py</code>.</li>
</ol>

<h2>Example</h2>
<pre><code>python ssh_brute_force.py</code></pre>

<h2>Note</h2>
<ul>
  <li><strong>Ethical Considerations:</strong> Brute-forcing passwords without proper authorization is unethical and may be illegal. Ensure you have explicit permission before using this tool.</li>
  <li><strong>Security Awareness:</strong> Always use strong, unique passwords and consider implementing additional security measures such as SSH key-based authentication and rate-limiting.</li>
</ul>

<p>For more information, connect with me on <a href="https://www.linkedin.com/in/abhijith-soman-5b597225b/">LinkedIn</a>.</p>

</body>
</html>
