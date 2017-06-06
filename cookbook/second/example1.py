#!/usr/bin/env python
# -*- coding: UTF-8 -*-

line='asdf fjdk; afed, fjek,asdf, foo'
import re

print(re.split(r'[;,\s]\s*',line))

fields=re.split(r'(;|,|\s)\s*',line)
print(fields)