#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='UTF-8', xml_decleration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for element in root:
        text = element.text
        if text is None:
            value = None
        elif text.isdigit():
            value = int(text)
        else:
            try:
                value = float(text)
            except ValueError:
                value = text
        result[element.tag] = value
    return result
