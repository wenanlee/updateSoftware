import zipfiles
import urllib.request
import urllib
def listzipfilesinfo(path):
    z=zipfiles.ZipFile(path,'r')
    for file in z.namelist():
        z.extract(file,"./")
def update():
    page = urllib.request.urlopen("http://www.ugmax.cn/psychology/version.html")
    serverVersion=page.read().decode()
    localVersion=0
    with open('version',"r") as f:    #设置文件对象
        localVersion = f.read()
        print(serverVersion,"------",localVersion)
        if serverVersion==localVersion:
            return "暂时没有新版本"
        else:
            urllib.request.urlretrieve("http://www.ugmax.cn/psychology/psychology.zip", "tmp.zip")
            listzipfilesinfo('tmp.zip')
        f.close()
    with open('version',"w+") as f:
        print(serverVersion)
        f.write(serverVersion)
        f.close()
    return "更新完成"
update()