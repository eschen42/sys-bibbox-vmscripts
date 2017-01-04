import json
import urllib
import base64

import requests
import jsonws
import roles

class Users:

    def __init__(self, companyId=0):

        print ("WELCOME IN USER SERVICE")
        self.allUsers= {}
        self.companyId = companyId

        api = jsonws.API()
        r = api.call("/user/get-company-users", {'companyId': self.companyId, 'start':"0", 'end':'1000'})
        users = json.loads(r.text)
        for ux in users:
            self.allUsers[ux['screenName']] = ux['userId']
        print (self.allUsers)

    def userIds (self):
        return self.allUsers

    def description(self, screenName):
        api = jsonws.API()
        return api.call("/user/get-user-by-screen-name", {'companyId': self.companyId, 'screenName': screenName})


    def initUsers(self):

        api = jsonws.API()

        print("FIRST GENERATE THE ROLES")

        roleService = roles.Roles(companyId='20116')
        roleService.initRoles()
        roleIds = roleService.rolesIds()

        screenNames = self.allUsers.keys()

        if 'bibboxadmin' not in screenNames:
            print("CREATE BIBBOX VM ADMIN USER")

            param =  {
                "companyId":  self.companyId,
                "autoPassword": False,
                "password1": "graz2017",
                "password2": "graz2017",
                "autoScreenName": False,
                "screenName": "bibboxadmin",
                "emailAddress": "bibboxadmin@bibbox.org",
                "facebookId": 0,
                "openId": "",
                "locale": "en_US",
                "firstName": "Roxana",
                "middleName": "",
                "lastName": "Rilling",
                "prefixId": 0,
                "suffixId": 0,
                "male": False,
                "birthdayMonth": 1,
                "birthdayDay": 1,
                "birthdayYear": 1970,
                "jobTitle": "Responsible for the installation of the BIBBOX VM and liferay sys admin",
                "groupIds": None,
                "organizationIds": None,
                "roleIds": [roleIds['BIBBOX VM Admin'], roleIds['Administrator']],
                "userGroupIds": None,
                "sendEmail": False,
                "serviceContext": {"assetTagNames": ["bibboxadmin"]}
            }
            r = api.call("/user/add-user", param )
            user =  json.loads(r.text)
            print(user)

            with open('avatar-pics/roxana.jpg', 'rb') as f:
                picdata = f.read()

            base64_bytes  = base64.b64encode(picdata)
            base64_string = base64_bytes.decode('utf-8')

            param = {
                "userId": user['userId'],
                "bytes": base64_string,
            }
            #r = api.call("/user/update-portrait", param)
            print(r.text)


        if 'admin' not in screenNames:
            print("CREATE BIBBOX  ADMIN USER")

            param = {
                "companyId": self.companyId,
                "autoPassword": False,
                "password1": "graz2017",
                "password2": "graz2017",
                "autoScreenName": False,
                "screenName": "admin",
                "emailAddress": "admin@bibbox.org",
                "facebookId": 0,
                "openId": "",
                "locale": "en_US",
                "firstName": "Alan",
                "middleName": "",
                "lastName": "Punter",
                "prefixId": 0,
                "suffixId": 0,
                "male": True,
                "birthdayMonth": 1,
                "birthdayDay": 1,
                "birthdayYear": 1970,
                "jobTitle": "Admin of the BIBBOX installation",
                "groupIds": None,
                "organizationIds": None,
                "roleIds": roleIds['BIBBOX Admin'],
                "userGroupIds": None,
                "sendEmail": False,
                "serviceContext": {"assetTagNames": ["admin"]}
            }

            r = api.call("/user/add-user", param)
            print (r.text)


        if 'pi' not in screenNames:
                print("CREATE BIBBOX PI USER")

                param = {
                    "companyId": self.companyId,
                    "autoPassword": False,
                    "password1": "graz2017",
                    "password2": "graz2017",
                    "autoScreenName": False,
                    "screenName": "pi",
                    "emailAddress": "pi@bibbox.org",
                    "facebookId": 0,
                    "openId": "",
                    "locale": "en_US",
                    "firstName": "Majmuna",
                    "middleName": "",
                    "lastName": "Sandu",
                    "prefixId": 0,
                    "suffixId": 0,
                    "male": False,
                    "birthdayMonth": 1,
                    "birthdayDay": 1,
                    "birthdayYear": 1970,
                    "jobTitle": "BIBBOX PI",
                    "groupIds": None,
                    "organizationIds": None,
                    "roleIds": roleIds['BIBBOX PI'],
                    "userGroupIds": None,
                    "sendEmail": False,
                    "serviceContext": {"assetTagNames": ["admin"]}
                }
                r = api.call("/user/add-user", param)
                print (r.text)

        if 'curator' not in screenNames:
                print("CREATE BIBBOX PI USER")

                param = {
                    "companyId": self.companyId,
                    "autoPassword": False,
                    "password1": "graz2017",
                    "password2": "graz2017",
                    "autoScreenName": False,
                    "screenName": "curator",
                    "emailAddress": "curator@bibbox.org",
                    "facebookId": 0,
                    "openId": "",
                    "locale": "en_US",
                    "firstName": "Santa",
                    "middleName": "",
                    "lastName": "Morello",
                    "prefixId": 0,
                    "suffixId": 0,
                    "male": False,
                    "birthdayMonth": 1,
                    "birthdayDay": 1,
                    "birthdayYear": 1970,
                    "jobTitle": "BIBBOX Curator",
                    "groupIds": None,
                    "organizationIds": None,
                    "roleIds": roleIds['BIBBOX Curator'],
                    "userGroupIds": None,
                    "sendEmail": False,
                    "serviceContext": {"assetTagNames": ["curator"]}
                }
                r = api.call("/user/add-user", param)
                print(r.text)


        if 'operator' not in screenNames:
            print("CREATE BIBBOX PI USER")

            param = {
                "companyId": self.companyId,
                "autoPassword": False,
                "password1": "graz2017",
                "password2": "graz2017",
                "autoScreenName": False,
                "screenName": "operator",
                "emailAddress": "operator@bibbox.org",
                "facebookId": 0,
                "openId": "",
                "locale": "en_US",
                "firstName": "Carmen",
                "middleName": "",
                "lastName": "Thatcher",
                "prefixId": 0,
                "suffixId": 0,
                "male": False,
                "birthdayMonth": 1,
                "birthdayDay": 1,
                "birthdayYear": 1970,
                "jobTitle": "BIBBOX Operator",
                "groupIds": None,
                "organizationIds": None,
                "roleIds": roleIds['BIBBOX Operator'],
                "userGroupIds": None,
                "sendEmail": False,
                "serviceContext": {"assetTagNames": ["operator"]}
            }
            r = api.call("/user/add-user", param)
            print(r.text)
