

from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="jogo de zumbis",
    version="1.0",
    description="jogo de zumbis app",
    options={"build_exe":{"packages":["pygame"]}},
    executables=executables
)


