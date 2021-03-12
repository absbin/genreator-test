from cx_Freeze import setup, Executable

base = None    

executables = [Executable("simple_gui.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "simple_gui",
    options = options,
    version = "1.0.0",
    description = 'Enjoy bro!',
    executables = executables
)