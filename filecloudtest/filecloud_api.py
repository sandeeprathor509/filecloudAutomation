import requests
import os
from datetime import datetime, time


class FileCloudAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        current_time = int(time.time() * 1000)
        self.query_params = {
            'time': current_time
        }
        self.headers = {
            'Accept': 'application/x-www-form-urlencoded',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def create_user(self, displayname, email, username):
        data = {
            'op': 'adduser',
            'username': username,
            'displayname': displayname,
            'email': email,
            'password': username + '@123',
            'authtype': 0,
            'status': 1,
            'isteamfolderuser': 'false',
            'sendpwdasplaintext': 'false',
            'sendapprovalemail': 0
        }
        url = self.base_url + "admin"
        response = requests.post(url=url, params=self.query_params,
                                 headers=self.headers,
                                 data=data)
        response.raise_for_status()
        return response

    def add_group(self, groupname):
        data = {
            "groupname": groupname
        }
        url = self.base_url + "admin/addgroup"
        response = requests.post(url=url, params=self.query_params,
                                 data=data, headers=self.headers)

        return response

    def add_user_to_group(self, groupId, user):
        data = {
            "groupid": groupId,
            "user": user
        }
        url = self.base_url + "admin/addmembertogroup"
        response = requests.post(url=url, params=self.query_params,
                                 data=data, headers=self.headers)
        return response

    def validate_user(self):
        response = requests.get(f"{self.base_url}/miniadmin/search", headers=self.headers)
        response.raise_for_status()
        return response

    def login(self, username, password):
        data = {
            'username': username,
            'password': password,
            'passwordType': 'password',
            'g-recaptcha-response': '',
            'tfa': 1
        }

        response = requests.post(f"{self.base_url}/core/loginguest", query_params=self.query_params,
                                 headers=self.headers, data=data)
        response.raise_for_status()
        return response

    def upload_file(self, file_path, file_name):
        file_size = os.path.getsize(file_path)
        current_date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')

        headers = {
            'Accept': 'application/x-www-form-urlencoded',
            'Content-Type': 'multipart/form-data'
        }
        params = {
            'appname': 'explorer',
            'filesize': file_size,
            'path': '%2Fautomation',
            'uploadpath': '',
            'adminproxyuserid': 'automation',
            'offset': 0,
            'date': current_date,
            'filename': file_name,
            'complete': 1
        }
        url = self.base_url + "upload"
        with open(file_path, 'rb') as file:
            files = {'filedata': file}
            response = requests.post(url=url, params=params, files=files, headers=headers)
        response.raise_for_status()
        return response

    def get_file_versions(self, file_name):
        headers = {
            'Accept': 'application/x-www-form-urlencoded',
            'Content-Type': 'multipart/form-data'
        }
        data = {
            "filepath": "/automation/",
            "adminproxyuserid": "automation",
            "filename": file_name,
            "checksum": 1
        }
        url = self.base_url + "core/getversions"
        response = requests.get(url=url, params=self.query_params, data=data,
                                headers=headers)
        response.raise_for_status()
        return response
