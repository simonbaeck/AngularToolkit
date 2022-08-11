import subprocess
import os

def main():
    start_dir = input("Root directory of Angular project (Full path): ")
    tailwind_init(start_dir)
    fontawesome_init(start_dir)
    print('DONE!')


def tailwind_init(start_dir):
    # npm install TailwindCSS for Angular
    tailwind_init_step1 = subprocess.Popen(['npm', 'install', '-D', 'tailwindcss', 'postcss', 'autoprefixer'], cwd=start_dir, shell=True)
    tailwind_init_step1.wait()
    os.system("cls")

    # Generate TailwindCSS config file
    tailwind_init_step2 = subprocess.Popen(['npx', 'tailwindcss', 'init'], cwd=start_dir, shell=True)
    tailwind_init_step2.wait()
    os.system("cls")

    # Overwrite config file with preset config
    with open('tailwind.config.js', 'r') as file:
        config_data = file.read()
    with open(f'{start_dir}\\tailwind.config.js', 'w') as file:
        file.write(config_data)
    os.system("cls")

    # Overwrite angular styles.css file with preset css file
    with open('styles.css', 'r') as file:
        css_data = file.read()
    with open(f'{start_dir}\\src\\styles.css', 'w') as file:
        file.write(css_data)
    os.system("cls")


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

    with open('icon.service.ts', 'r') as file:
        icon_service_data = file.read()
    with open(f'{start_dir}\\src\\app\\services\\icon.service.ts', 'w') as file:
        file.write(icon_service_data)
    os.system("cls")


if __name__ == "__main__":
    main()
