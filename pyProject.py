import subprocess
import readline
import json
import sys
import os

helpText = """
                                              /\________/\ 
                                             /            \  @ddaniboy
                                            /  () w ()     \ 
____________________________________________\  __________  /_____________________________________
| x - []                                     \/          \/                                     |
-------------------------------------------------------------------------------------------------
|                                                                                               |        
|       -c/--create     create a project.                                                       |
|                                                                                               |
|       -i/--install    install dependencies.                                                   |                                    
|                       [install project.json dependencies.]                                    |
|                                                                                               |
|                       to use --install you can use as follows:                                |
|                       python3 pyProject.py -i project                                         |
|                                                                                               |
|                       if you have it inside the project folder you can run as follows:        |
|                       python3 pyProject.py -i                                                 |
|                                                                                               |
|                                                                                               |
|       -u/--update     update the project.json.                                                |
|                       [update project.json dependencies.]                                     |
|                                                                                               |
|                       to use --update you can use as follows:                                 |
|                       python3 pyProject.py -u project                                         |
|                                                                                               |
|                       if you have it inside the project folder you can run as follows:        |
|                       python3 pyProject.py -u                                                 |
|                                                                                               |
|                                                                                               |
|       -h/--help       command to help.                                                        |
-------------------------------------------------------------------------------------------------
"""

def installLibs(project):
    pjson = open(project+"/project.json", encoding='utf-8')
    js = json.load(pjson)

    for item in js[project.split("/")[-1]]["dependencies"]:
        install = str(item) + "==" + js[project.split("/")[-1]]["dependencies"][item]["Version"]
        subprocess.run(["python3", '-m', 'pip', 'install', install])

    pjson.close()


def jsonUpdate(libs, project):

    pjson = open(project+"/project.json", encoding='utf-8')

    js = json.load(pjson)


    def libsPIP(lib):
        lib = str(lib)

        result = subprocess.run(["python3", '-m', 'pip', 'show', lib], capture_output=True, text=True).stdout

        result = result.splitlines()

        var = {}

        values = ["Name", "Version", "Location"]


        for linha in result:
            very=0

            for value in values:
                if value in linha:
                    very=1

            if very == 1:
                linha = linha.split(": ")

                var[linha[0]] = linha[1]


        
        js[project.split("/")[-1]]["dependencies"][var["Name"]] = {"Version":var["Version"], "Location": var["Location"]}
        



    for item in libs:
        libsPIP(item)

    pjson.close()

    Wjson = open(project+"/project.json", "w+")

    Wjson.write(json.dumps(js, indent=4))

    Wjson.close()


def CreateProject():
    ProjectName = input("[+]Project Name> ")

    if ProjectName == "":
        print("Project Name can't be empty")
        exit()

    #-------------------------------------------------------------------

    Version = str(input("[+]Version>(1.0.0) "))
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]




    if Version == "":
        Version = "1.0.0"
    else:
        for c in Version:
            if c not in chars:
                print("version example: 1.0.0, 1.0.4, 2.3.4")
                exit()

    #-------------------------------------------------------------------
    Autor = input("[+]Autor> ")

    #-------------------------------------------------------------------

    os.mkdir(ProjectName)


    project = {ProjectName:{"Version": Version, "Autor": Autor, "dependencies": {}}}

    jsonF = json.dumps(project, indent=4)


    arq = open(ProjectName + "/project.json", "a")
    arq.write(jsonF)
    arq.close


def libsColector(project):
    list = []
    dir = os.listdir(project)
    dir.remove("project.json")


    for arq in dir:
        arquivo = open(project+"/"+arq, "r")
        for linha in arquivo.readlines():
            very = linha.split(" ")[0]
            if very == "import" or very == "from":
                lib = linha.split(" ")[1].replace("\n", "")
                if lib not in list:
                    result = subprocess.run(["python3", '-m', 'pip', 'show', lib], capture_output=True, text=True).stdout

                    if result != "":
                        list.append(lib)


    return list


def libsjson(project):


    listLib = libsColector(project)


    jsonUpdate(listLib, project)
    




try:
    if sys.argv[1] == "-c" or sys.argv[1] == "--Create":
        CreateProject()





    elif sys.argv[1] == "-i" or sys.argv[1] == "--install":
        try:
            if os.path.exists(sys.argv[2]):
                installLibs(sys.argv[2])
            else:
                print("invalid path")
        except:
            installLibs(os.getcwd())






    elif sys.argv[1] == "-u" or sys.argv[1] == "--update":
        try:
            if os.path.exists(sys.argv[2]):
                libsjson(sys.argv[2])
            else:
                print("invalid path")
        except:
            libsjson(os.getcwd())





    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(helpText)
except:
    print("-h/--help for help you") 
  
