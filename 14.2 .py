import xml.etree.ElementTree as ET

nums = (28, -144, 50, 831, 72, 140, 90, 120)

max_num = 0

root = ET.Element("root")
max_num_element = ET.SubElement(root, "max_num")
max_num_element.text = str(max_num)

tree = ET.ElementTree(root)
tree.write("output.xml")

tree = ET.parse("output.xml")
root = tree.getroot()
max_num = int(root.find("max_num").text)
print(f"Самое большое число, кратное 5, в кортеже: {max_num}")
