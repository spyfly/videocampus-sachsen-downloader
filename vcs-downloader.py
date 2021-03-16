import os
import sys
import urllib.request
import re

#downloadUrl = sys.argv[1]
downloadUrl = input("Please enter the Download URL: ")
downloadUrl = re.sub("_[0-9]{3}.ts", "", downloadUrl)

filename = input("File Name? (No ext and special chars): ") + ".ts"
print("Downloading from " + downloadUrl)
filesize = 100
i = 0
videodata = ""
while filesize > 0:
    numberStr = str(i)
    if i < 1000:
        numberStr = numberStr.zfill(3)
    url = downloadUrl + "_"+ numberStr +".ts"
    localFile = numberStr + ".ts"
    print(url)
    #urllib.request.urlretrieve(url, localFile)
    response = urllib.request.urlopen(url)
    ts = response.read()
    filesize = len(ts)
    tsfile = open(filename, 'ab')
    tsfile.write(ts)
    #filesize = os.stat(localFile).st_size
    i = i + 1
