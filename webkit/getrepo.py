import urllib, zipfile, os, shutil

urllib.urlretrieve ("https://github.com/Hextris/hextris/archive/gh-pages.zip", "./gh-pages.zip")

print "Extracting..."

with zipfile.ZipFile('./gh-pages.zip', "r") as z:
	z.extractall(".")

