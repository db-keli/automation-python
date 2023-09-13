import os
import pprint
import zipfile

# print(os.path.abspath('.'))

# Reading zip files
print(os.path.abspath('.'))
os.chdir('/home/kekeli/Downloads')
print(os.path.abspath('.'))
everything = os.listdir()
pprint.pprint(everything)
zips = zipfile.ZipFile('rufus-4.2.zip')
pprint.pprint(zips.namelist())

