#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.set("key", key)
        element.set("type", type(value).__name__)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='UTF-8', xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for element in root.findall("item"):
        key = element.get("key")
        type_name = element.get("type")
        text = element.text.strip()
        if text_name == "int":
            value = int(text)
        elif text_name == "float":
            value = float(text)
        elif type_name == "bool":
            value = text == "True"
        else:
            value = text
        result[key] = value
    return result
