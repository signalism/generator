#!/usr/bin/env python3

import os
import re
import streamlit as st

code = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-L8KY40QQTX"></script><script>window.dataLayer = window.dataLayer || []; function gtag () { dataLayer.push(arguments); }; gtag('js', new Date()); gtag('config', 'G-L8KY40QQTX');</script>'''

path = os.path.dirname(st.__file__) + '/static/index.html'

with open(path, 'r') as file_r:
	data = file_r.read()
	if len(re.findall('G-L8KY40QQTX', data)) == 0:
		with open(path, 'w') as file_w:
			file_w.write(re.sub('<head>', '<head>' + code, data))
