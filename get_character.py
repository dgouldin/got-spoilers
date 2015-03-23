#!/usr/bin/env python
from xml.etree import ElementTree
import requests
import unicodecsv as csv
import sys

url = "http://en.wikipedia.org/wiki/List_of_Game_of_Thrones_characters"
response = requests.get(url)

def get_characters(table):
    for row in table.findall('tr')[2:]:
        td = row.find('td')
        if td is None or td.attrib.get('colspan'):
            continue
        a = td.find('a')
        if a is not None:
            yield a.text
        else:
            yield td.text

tree = ElementTree.fromstring(response.content)
tables = filter(lambda t: t.findtext("./tr/th") == "Name",
                tree.findall(".//table[@class='wikitable']"))

writer = csv.writer(sys.stdout)
for table in tables:
    for character in get_characters(table):
        writer.writerow((character,))

