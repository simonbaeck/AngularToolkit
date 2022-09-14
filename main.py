import subprocess
import os
import webbrowser


def main():
    start_dir = input("Root directory of Angular project (Full path): ")
    tailwind_init(start_dir)
    fontawesome_init(start_dir)
    hello_world(start_dir)


def tailwind_init(start_dir):
    # npm install TailwindCSS for Angular
    tailwind_init_step1 = subprocess.Popen(['npm', 'install', '-D', 'tailwindcss', 'postcss', 'autoprefixer'], cwd=start_dir, shell=True)
    tailwind_init_step1.communicate()
    tailwind_init_step1.wait()

    # Generate TailwindCSS config file
    tailwind_init_step2 = subprocess.Popen('npx tailwindcss init', cwd=start_dir, shell=True)
    tailwind_init_step2.wait()

    # Overwrite config file with preset config
    with open('tailwind.config.js', 'r') as file:
        config_data = file.read()
    with open(f'{start_dir}\\tailwind.config.js', 'w') as file:
        file.write(config_data)

    # Overwrite angular styles.css file with preset css file
    with open('styles.css', 'r') as file:
        css_data = file.read()
    with open(f'{start_dir}\\src\\styles.css', 'w') as file:
        file.write(css_data)

    # Overwrite app.component.html file with preset app.component.html
    with open('app.component.html', 'r') as file:
        app_comp_data = file.read()
    with open(f'{start_dir}\\src\\app\\app.component.html', 'w') as file:
        file.write(app_comp_data)

    # End tailwind init
    os.system("cls")


def fontawesome_init(start_dir):
    # npm install fontawesome core
    fontawesome_init_step1 = subprocess.Popen(['npm', 'install', '@fortawesome/fontawesome-svg-core'], cwd=start_dir, shell=True)
    fontawesome_init_step1.wait()

    # npm install fontawesome free solid icons
    fontawesome_init_step2 = subprocess.Popen(['npm', 'install', '@fortawesome/free-solid-svg-icons'], cwd=start_dir, shell=True)
    fontawesome_init_step2.wait()

    # npm install fontawesome free regular icons
    fontawesome_init_step3 = subprocess.Popen(['npm', 'install', '@fortawesome/free-regular-svg-icons'], cwd=start_dir, shell=True)
    fontawesome_init_step3.wait()

    # npm install fontawesome angular
    fontawesome_init_step4 = subprocess.Popen(['npm', 'install', '@fortawesome/angular-fontawesome@latest'], cwd=start_dir, shell=True)
    fontawesome_init_step4.wait()

    # Add FontAwesomeModule to app.module.ts
    # Overwrite app.component.html file with preset app.component.html
    with open('app.module.ts', 'r') as file:
        app_module_data = file.read()
    with open(f'{start_dir}\\src\\app\\app.module.ts', 'w') as file:
        file.write(app_module_data)

    # Create icons service
    fontawesome_init_iconservice = subprocess.Popen(['ng', 'generate', 'service', 'services/icon', '--skip-tests'], cwd=start_dir, shell=True)
    fontawesome_init_iconservice.wait()
    with open('icon.service.ts', 'r') as file:
        icon_service_data = file.read()
    with open(f'{start_dir}\\src\\app\\services\\icon.service.ts', 'w') as file:
        file.write(icon_service_data)

    # End fontawesome init
    os.system("cls")


def hello_world(start_dir):
    url = 'http://localhost:4200/'
    webbrowser.open(url)
    start_project = subprocess.Popen(['ng', 'serve'], cwd=start_dir, shell=True)
    start_project.wait()


if __name__ == "__main__":
    main()
