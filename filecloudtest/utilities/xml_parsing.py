import xml.etree.ElementTree as ET


def xml_parse(response, api_type):
    result_dict = {}

    root = ET.fromstring(response)

    if api_type == 'login':
        command_element = root.find('.//command')
        if command_element is not None:
            type_element = command_element.find('type')
            result_element = command_element.find('result')
            message_element = command_element.find('message')

            if type_element is not None:
                result_dict['type'] = type_element.text
            if result_element is not None:
                result_dict['result'] = result_element.text
            if message_element is not None:
                result_dict['message'] = message_element.text
    elif api_type == 'group':
        group_element = root.find('.//group')
        if group_element is not None:
            groupid_element = group_element.find('groupid')
            groupname_element = group_element.find('groupname')

            if groupid_element is not None:
                result_dict['groupid'] = groupid_element.text
            if groupname_element is not None:
                result_dict['groupname'] = groupname_element.text

    return result_dict
