import xml.etree.ElementTree as ET
import conf_reader
import uuid


rss_path = conf_reader.read_conf_setting("conf.json", "rss_path")

def write_rss(message, channel):
    group = channel["Group_name"]
    link = channel["URL"]
    time_attack = message.date.strftime('%a, %d %b %Y %H:%M:%S %Z')
    #<pubDate>Wed, 02 Oct 2002 13:00:00 GMT</pubDate> - required Time Format

    tree = ET.parse(rss_path)

    xmlRoot = tree.getroot()
    child = ET.Element("item")
    xmlRoot[0].append(child)
    b1 = ET.SubElement(child, "title")
    b1.text = f"New Malicious Activity from {group}"
    b2 = ET.SubElement(child, "link")
    b2.text = f"{link}"
    b3 = ET.SubElement(child, "description")
    b3.text = f"Full text message:\n{message.text}"
    b4 = ET.SubElement(child, "pubDate")
    b4.text = f"{time_attack}"
    b5 = ET.SubElement(child, "guid")
    b5.attrib = {"isPermaLink": "false"}
    b5.text = str(uuid.uuid4())
    tree.write(rss_path)
