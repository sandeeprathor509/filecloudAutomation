import pytest
from filecloud_api import FileCloudAPI


@pytest.fixture(scope='session')
def filecloud_api():
    base_url = 'https://automation.filecloudonline.com/'
    return FileCloudAPI(base_url)


@pytest.fixture(scope='session')
def user_token(filecloud_api):
    username = 'sandeeprathor509'
    password = 'oqY1PxUf'
    return filecloud_api.login(username, password)
