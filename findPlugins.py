# Author - Darshan Deshmukh (dedileep@cisco.com)
# Find the plugins installed on any Jenkins instance
# Command line aurgument - $ python find_plugins.py <jenkins url> <filename.csv>

import xml.etree.ElementTree as ET
import requests
import sys
from itertools import zip_longest
import itertools
from collections import OrderedDict
import collections
import csv

url = sys.argv[1].strip()
filename = sys.argv[2].strip()

response = requests.get(url+'/pluginManager/api/xml?depth=1',stream=True)
response.raw.decode_content = True
tree = ET.parse(response.raw)
root = tree.getroot()
data = {}
for plugin in root.findall('plugin'):
	longName = plugin.find('longName').text
	shortName = plugin.find('shortName').text
	version = plugin.find('version').text
	data[longName] = version
	print (version)
	with open(filename, 'w') as f:
		[f.write('{0},{1}\n'.format(key, value)) for key, value in data.items()]
