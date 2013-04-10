#!/usr/bin/env python

import urllib

# url handler respone
base = r'http://localhost:8081'
data3 = urllib.urlencode({"time":1323333"user":"ygs","action":"answer","content":"abcde"})  
# data3 = { 'name': 'dark-bull', 'age': 200 }
handler = urllib.urlopen(base, data3)
print r'http header:/n', handler.info()  
print r'http status:', handler.getcode()  
print r'url:', handler.geturl()  

def cbk(a, b, c):  
	# a : has download counts
	# b : block size
	# c : remote file size
    per = 100.0 * a * b / c  
    if per > 100:  
        per = 100  
    print '%.2f%%' % per  
  
# download url 
href = r'http://down.51voa.com/201303/us-budget-impasse-could-affect-air-travel.mp3'
local = r'./test.mp3'  
urllib.urlretrieve(href, local, cbk)  
handler.close()

# url escape
data = 'name=dasf'
data1 = urllib.quote(data)
print data1
print urllib.unquote(data1)

print urllib.quote_plus(data)

# json file 
data3 = urllib.urlencode({ 'name': 'dark-bull', 'age': 200 })  
print data3

data4 = urllib.pathname2url(r'd:/a/b/c/23.php')  
print data4 # result: ///D|/a/b/c/23.php  
print urllib.url2pathname(data4)    # result: D:/a/b/c/23.php  
