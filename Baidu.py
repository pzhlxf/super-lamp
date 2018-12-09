import urllib.request
baidu = "https://www.baidu.com/s?wd=cd"
req = urllib.request.Request(baidu)
data = urllib.request.urlopen(req).read()
fh = open("/Users/lixiufeng/Desktop/未命名文件夹/baidu.html","wb")
fh.write(data)
fh.close
