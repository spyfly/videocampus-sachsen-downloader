import sys
import urllib.request
import re
import ssl

if (len(sys.argv) > 1 and sys.argv[1]):
    downloadUrl = sys.argv[1]
else:
    downloadUrl = input("Please enter the Download URL: ")
downloadUrl = re.sub("_[0-9]{3}.ts", "", downloadUrl)

if (len(sys.argv) > 2 and sys.argv[2]):
    filename = sys.argv[2] + ".ts"
else:
    filename = input("File Name? (No ext and special chars): ") + ".ts"
print("Downloading from " + downloadUrl)

filesize = 100
i = 0
videodata = ""
context = ssl._create_unverified_context()
phpSessId = None
while filesize > 0:
    numberStr = str(i)
    if i < 10000:
        numberStr = numberStr.zfill(3)
    url = downloadUrl + "_"+ numberStr +".ts"
    localFile = numberStr + ".ts"
    #print(url)
    print('.', end='',flush=True)
    #urllib.request.urlretrieve(url, localFile)
    try:
        request = urllib.request.Request(url)
        # Add login Cookie
        if (phpSessId):
            request.add_header("Cookie", "PHPSESSID=" + phpSessId)
        response = urllib.request.urlopen(request, context=context)
        ts = response.read()
        filesize = len(ts)
        tsfile = open(filename, 'ab')
        tsfile.write(ts)
        #filesize = os.stat(localFile).st_size
        i = i + 1
    except urllib.error.HTTPError as e:
        if (e.code == 404):
            phpSessId = input("Please enter the PHPSESSID Cookie: ")
print('Done downloading ' + localFile + '!')