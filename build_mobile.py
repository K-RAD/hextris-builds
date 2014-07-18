import urllib2, zipfile, os, shutil

# url = "https://github.com/Hextris/hextris/archive/gh-pages.zip"

# file_name = url.split('/')[-1]
# u = urllib2.urlopen(url)
# f = open(file_name, 'wb')
# meta = u.info()
# print meta
# file_size = int(meta.getheaders("Content-Length")[0])
# print "Downloading: %s Bytes: %s" % (file_name, file_size)

# file_size_dl = 0
# block_sz = 8192
# while True:
# 	buffer = u.read(block_sz)
# 	if not buffer:
# 		break

# 	file_size_dl += len(buffer)
# 	f.write(buffer)
# 	status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
# 	status = status + chr(8)*(len(status)+1)
# 	print status,

# f.close()

# print "Extracting..."

# with zipfile.ZipFile('./gh-pages.zip', "r") as z:
#     z.extractall("./www/")

# os.remove('./www/hextris-gh-pages/.gitignore')
# os.remove('./www/hextris-gh-pages/README.md')

# fs = os.listdir('./www/hextris-gh-pages/')
# for i in fs:
# 	shutil.move('./www/hextris-gh-pages/' + i, './www/')

# with open('./www/js/initialization.js', 'w+') as f:
# 	s = f.read().split('\n')
# 	s[0] = 'document.addEventListener(\'deviceready\',initialize, false);'
# 	ns = ''
# 	for i in s:
# 		ns += i + '\n'
# 	f.write(ns)

# print "Cleaning up..."
# os.rmdir('./www/hextris-gh-pages/')
# os.remove('./gh-pages.zip')

