import pytest
from utilities.xml_parsing import xml_parse

groups_and_users = {
    "Accounting": ["Henderson Nakashima", "Biserka Wilkie", "Giltbert Thatcher", "Octavia Blanchard", "Dawid Morel"],
    "Operations": ["Zülfikar Aafjes", "Vlasi Szilágyi", "Madelyn Donne", "Şule Zima", "Rehema Barr"],
    "Engineering": ["Awee Murdoch", "Tsholofelo Boer", "Mari Winthrop"],
    "Consultants": ["Dragoslav Echevarría", "Kaley Petrov"]
}


@pytest.mark.parametrize("group,users", groups_and_users.items())
def test_create_users(filecloud_api, group, users):
    # adding user into the system
    if len(users) > 0:
        for user in users:
            username = user.replace(' ', '').lower()
            displayname = username
            email = f"{username}@filecloud.com"
            response = filecloud_api.create_user(displayname, email, username)
            assert response.status_code == 200

    # adding groups into the system
    groups_id = {}
    for groupname in group:
        response = filecloud_api.add_group(groupname)
        groups_id[groupname] = xml_parse(response, "group")['groupid']

    # recreating the group_id dict with the users
    id_to_user = {}
    for department, users in groups_and_users.items():
        if department in groups_id:
            ids = groups_id[department]
            id_to_user[ids] = users.replace(' ', '').lower()

    # adding users to their respective groups
    for groupid, usersid in id_to_user.items():
        response = filecloud_api.add_user_to_group(groupid, usersid)
        assert response.status_code == 200
