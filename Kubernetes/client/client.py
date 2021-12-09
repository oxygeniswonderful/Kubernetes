import urllib.request
import time

i = 0

while i < 100:
    fp = urllib.request.urlopen("http://localhost:7777/")
    i += 1
    encodedContent = fp.read()
    decodedContent = encodedContent.decode("utf8")
    print(decodedContent)
    fp.close()
    time.sleep(60)
