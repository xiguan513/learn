#!/usr/bin/env python
# -*- coding: UTF-8 -*-

text='''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''


# fout=open('file_name','wt')
# fout.write(str(text))
# fout.close()

fout=open('file_name','rb')
print(len(fout.read()))
fout.seek(10,1)
print(fout.tell())
print(fout.read(10))


