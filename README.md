# PyProject
this tool is designed to manage a project's dependencies, so you can share them without worrying about their version.

NOTE: The tool does not remove a dependency after updating the project.json (the file in which it stores the dependencies).

# Help

![Screen Shot 2022-07-29 at 19 27 51](https://user-images.githubusercontent.com/52128795/181853440-d4c7fcdf-a0bd-4d47-b155-628d112d955b.png)

# Executable

if you want to use an executable to use directly from /bin, you can use the following command:

python3 -m PyInstaller pyProject.py --onefile

NOTE: the pyinstaller that comes by default in kali linux has some problems and it is recommended to download pyinstaller by pip
