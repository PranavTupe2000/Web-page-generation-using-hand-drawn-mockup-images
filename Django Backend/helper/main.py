import os
import sys
import shutil
from os import walk

p_name = sys.argv[1]
a_name = sys.argv[2]

p_path = '../output/' + p_name
a_path = p_path + '/' + a_name

# p_test = "taskmate"
# a_test = "todoapp"
# p_path = '../output/' + p_test
# a_path = p_path + '/' + a_test

f = []

def addApptoSettings(p,a):
    
    with open('../output/' + p +'/' + p +'/settings.py', 'r') as file :
        filedata = file.read()
    
    filedata = filedata.replace('INSTALLED_APPS = [', 'INSTALLED_APPS = [\n\t\'' + a + '\',')

    with open('../output/' + p +'/' + p +'/settings.py', 'w') as file:
        file.write(filedata)

def urlMain(p,a):
    with open('../output/' + p +'/' + p +'/urls.py', 'r') as file :
        filedata = file.read()
    
    filedata = filedata.replace('import path', 'import path,include')
    filedata = filedata.replace("path('admin/', admin.site.urls),", 
                                "path('admin/', admin.site.urls),\n\tpath('',include('" + a + ".urls'))")
    

    with open('../output/' + p +'/' + p +'/urls.py', 'w') as file:
        file.write(filedata)
     
def createTemplates(p,a):
    os.mkdir(a_path + '/templates')
    for (dirpath, dirnames, filenames) in walk("../input"):
        f.extend(filenames)
        break
    print(f)
    for i in f:
        if '.html' in i:
            src = "../input/" + i
            des = a_path + '/templates'
            shutil.copy(src,des)

def urlApp(p,a):
    src = "urls.py"
    des = a_path
    shutil.copy(src,des)
    
    
    with open('../output/' + p +'/' + a +'/urls.py', 'r') as file :
        filedata = file.read()
    
    for i in f:
        if '.html' in i:
            i1 = i[:-5]
            filedata = filedata.replace('{{}}',"path('', views." + i1 + "View.as_view(), name='"+ i1 +"'),\n\t{{}}")
            pass
    
    filedata = filedata.replace('{{}}',"")

    with open('../output/' + p +'/' + a +'/urls.py', 'w') as file:
        file.write(filedata)


def createViews(p,a):
    fileHandle = open("views.py", "r")
    texts = fileHandle.readlines()
    fileHandle.close()

    fileHandle = open(a_path + "/views.py", "w")
    for s in texts:
        fileHandle.write(s)
    fileHandle.close()
    
    
    with open('../output/' + p +'/' + a +'/views.py', 'r') as file :
        filedata = file.read()
        
    for i in f:
        if '.html' in i:
            i1 = i[:-5]
            filedata = filedata.replace('{{}}',"class " + i1 + "View(TemplateView):\n\t" + "template_name = '" + 
                                    i +"'\n\n{{}}")
    filedata = filedata.replace('{{}}',"")
    
    with open('../output/' + p +'/' + a +'/views.py', 'w') as file:
        file.write(filedata)
    pass

   
#addApptoSettings(p_test,a_test)
# createTemplates(p_test,a_test)
# # urlMain(p_test,a_test)
# urlApp(p_test,a_test)
# createViews(p_test,a_test)

addApptoSettings(p_name,a_name)
createTemplates(p_name,a_name)
urlMain(p_name,a_name)
urlApp(p_name,a_name)
createViews(p_name,a_name)