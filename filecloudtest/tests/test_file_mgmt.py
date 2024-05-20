import pytest
import os


@pytest.fixture(scope='session')
def docx_file_path():
    return os.path.join(os.path.dirname(__file__), '../data/Sandeep_Rathor.docx')


def test_upload_file(filecloud_api, docx_file_path):
    file_name = 'Sandeep_Rathor.docx'
    response = filecloud_api.upload_file(docx_file_path, file_name)
    assert response.status_code == 200


def test_get_file_versions(filecloud_api):
    file_name = 'Sandeep_Rathor.docx'
    versions = filecloud_api.get_file_versions(file_name)
    assert len(versions) >= 1
