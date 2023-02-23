import requests
import json

while(True):
    print("------------------------------GENERATING Captch TOKEN BELOW------------------------") 

    headersCT = {'content-type': 'application/json', 'Authorization': 'Basic U2xpY1VBVFNMSUNBU1RSQVVTRVI6YVlybS9BL3QrMWRXWmJYZm5DQVBqT1k1dXIyRFBJMjlFSUluZlcxZjdBZz0=', 'Vid': 'SlicUATSLICASTRA2022'}

    rCT = requests.post('https://uatslicapi.shriramlife.me/UATASTRAWebAPI/api/PropAPI/GetCaptchaToken', json={"CIP":{"UserID":"S1411696","Captcha":"264338"}}, headers=headersCT)

    CTjso = rCT.json()

    for key, value in CTjso.items():
        CaptchaToken = value["CaptchaToken"]
        
    print(CaptchaToken)

    print("------------------------------GENERATING JWT TOKEN BELOW------------------------")

    headersGToken = {'content-type': 'application/json'}

    rGToken = requests.post('https://uatslicapi.shriramlife.me/UATASTRAWebAPI/api/PropAPI/GenerateAPIToken', json={"ip":{"Key3":"S1411696","Key6":""+CaptchaToken+""}}, headers=headersGToken)

    #print(rGToken)

    GTokenjso = rGToken.json()

    for key, value in GTokenjso.items():
        JWT = value["Key1"]

    print(JWT)    

    print("------------------------------GENERATING No Rate Limit BELOW------------------------")

    headerNRL = {'content-type': 'application/json', 'Authorization': 'Bearer ' +JWT}
    #print(headerNRL)
    NRLjson = requests.post('https://uatslicapi.shriramlife.me/UATASTRAWebAPI/api/PropAPI/GenerateOTPPOSIrdai', 
    json={"ip":{"MobileNumber":"9131154627","ApplicationNo":"202302204","EmailID":"ergdk@gmail.com","PlanID":"130","MobUserID":"S1411696"}}, headers=headerNRL)
    print(NRLjson.json())
