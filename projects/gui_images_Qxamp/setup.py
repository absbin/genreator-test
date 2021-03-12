from cx_Freeze import setup, Executable

base = None    

executables = [Executable("gui_images_Qxamp.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "pics",
    options = options,
    version = "1.0.0",
    description = 'Enjoy bro!',
    executables = executables
)