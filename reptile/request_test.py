#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests

r=requests.get('https://github.com/timeline.json')
print r.text