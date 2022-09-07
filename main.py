import subprocess
import os

from classes.Menu import Menu
from classes.Tailwind import Tailwind


def main():
    intro()
    print("[STEP 2] Install styling framework")
    options = ["Install TailwindCSS"]
    main_menu = Menu(options)
    option = main_menu.ask_menu()
    match option:
        case "0":
            print("Install TailwindCSS")


def intro():
    print("*** AngularToolkit v2.0 ***")
    print("[STEP 1] Create new angular project")
    finished = False
    while finished is False:
        ask = input("Do you want to create a new angular project? (y/n): ")
        if ask == "y":
            project_dir = input("New angular project directory (full path): ")
            project_name = input("Project name: ").lower().strip()
            subprocess.Popen(['ng', 'new', f'{project_name}'], cwd=project_dir, shell=True).wait()
        elif ask == "n":
            print("Skipping installation...")
            finished = True
        else:
            finished = False


def tailwind_init():
    Tailwind()


def fontawesome_init(start_dir):
    # npm install fontawesome core
    fontawesome_init_step1 = subprocess.Popen(['npm', 'install', '@fortawesome/fontawesome-svg-core'], cwd=start_dir, shell=True)
    fontawesome_init_step1.wait()
    os.system("cls")

    # npm install fontawesome free solid icons
    fontawesome_init_step2 = subprocess.Popen(['npm', 'install', '@fortawesome/free-solid-svg-icons'], cwd=start_dir, shell=True)
    fontawesome_init_step2.wait()
    os.system("cls")

    # npm install fontawesome free regular icons
    fontawesome_init_step3 = subprocess.Popen(['npm', 'install', '@fortawesome/free-regular-svg-icons'], cwd=start_dir, shell=True)
    fontawesome_init_step3.wait()
    os.system("cls")

    # npm install fontawesome angular
    fontawesome_init_step4 = subprocess.Popen(['npm', 'install', '@fortawesome/angular-fontawesome@latest'], cwd=start_dir, shell=True)
    fontawesome_init_step4.wait()
    os.system("cls")

    # add FontAwesomeModule to app.module.ts
    with open(f'{start_dir}\\src\\app\\app.module.ts') as file:
        lines = file.readlines()
    lines.insert(lines.index('import { BrowserModule } from \'@angular/platform-browser\';\n') + 1, 'import { FontAwesomeModule } from \'@fortawesome/angular-fontawesome\';\n')
    lines.insert(lines.index('    BrowserModule,\n') + 1, '    FontAwesomeModule,\n')
    with open(f'{start_dir}\\src\\app\\app.module.ts', 'w') as file:
        for line in lines:
            file.write(line)
    os.system("cls")

    # create icons service
    fontawesome_init_iconservice = subprocess.Popen(['ng', 'generate', 'service', 'services/icon', '--skip-tests'], cwd=start_dir, shell=True)
    fontawesome_init_iconservice.wait()
    os.system("cls")

    with open('presets/icon.service.ts', 'r') as file:
        icon_service_data = file.read()
    with open(f'{start_dir}\\src\\app\\services\\icon.service.ts', 'w') as file:
        file.write(icon_service_data)
    os.system("cls")


if __name__ == "__main__":
    main()
