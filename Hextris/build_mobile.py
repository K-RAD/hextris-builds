import urllib, zipfile, os, shutil

urllib.urlretrieve ("https://github.com/Hextris/hextris/archive/gh-pages.zip", "./gh-pages.zip")

print "Extracting..."

with zipfile.ZipFile('./gh-pages.zip', "r") as z:
	z.extractall("./www/")

os.remove('./www/hextris-gh-pages/.gitignore')
os.remove('./www/hextris-gh-pages/README.md')

fs = os.listdir('./www/hextris-gh-pages/')
for i in fs:
	shutil.move('./www/hextris-gh-pages/' + i, './www/')

with open('./www/js/initialization.js', 'r') as fin:
	data = fin.read().splitlines(True)
with open('./www/js/initialization.js', 'w') as fout:
#	data[0] = 'document.addEventListener(\'deviceready\',initialize, false);'
	fout.writelines(data)

print "Cleaning up..."
os.rmdir('./www/hextris-gh-pages/')
os.remove('./gh-pages.zip')
