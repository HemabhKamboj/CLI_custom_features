from urllib import request
from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests,os


def get_image():
	res=requests.get('https://bingwallpaper.com/')
	soup=BeautifulSoup(res.text,"lxml")
	image=soup.find('a',{'class':'cursor_zoom'}).find('img')
	url=image.get('src')
	return url

def download():
	url=get_image()
	file_name = dt.now().strftime("%Y-%m-%d")
	user = os.getenv('USER')
	path='/root/Pictures/BingWallpapers'
	full_path=os.path.join(path,file_name)
	

	with open(full_path, 'wb') as f:
		f.write(request.urlopen(url).read())
	return full_path

download()

def change():
	full_path=download()
	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///"+full_path)

change()

def run_wallpaperwebscrapping():
	get_image()