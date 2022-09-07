import subprocess


class Tailwind:
    def __init__(self):
        self.root_dir = input("Angular root directory (Full path): ")
        self.tailwind()

    # Bundle methods
    def tailwind(self):
        self.install_tailwind()
        self.init_tailwind()
        self.set_config_tailwind()
        self.set_style_tailwind()

    # npm install TailwindCSS for Angular
    def install_tailwind(self):
        subprocess.Popen(['npm', 'install', '-D', 'tailwindcss', 'postcss', 'autoprefixer'],
                         cwd=self.root_dir,
                         shell=True).wait()

    # Generate TailwindCSS config file
    def init_tailwind(self):
        subprocess.Popen(['npx', 'tailwindcss', 'init'],
                         cwd=self.root_dir,
                         shell=True).wait()

    # Overwrite config file with preset config
    def set_config_tailwind(self):
        with open('./presets/tailwind.config.js', 'r') as file:
            config_data = file.read()
        with open(f'{self.root_dir}\\tailwind.config.js', 'w') as file:
            file.write(config_data)

    # Overwrite angular styles.css file with preset css file
    def set_style_tailwind(self):
        with open('./presets/styles.css', 'r') as file:
            css_data = file.read()
        with open(f'{self.root_dir}\\src\\styles.css', 'w') as file:
            file.write(css_data)
