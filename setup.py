from cx_Freeze import setup, Executable

# Include any necessary modules in the 'build_exe_options' dictionary.
# If your script requires additional data files (like the .mp3 files),
# you can include them in the 'include_files' list.
build_exe_options = {
    "packages": [],  # List any packages your script uses.
    "includes": [],  # List any modules that cx_Freeze might miss.
    "include_files": ["enter.mp3", "sonido.mp3", "teclado.mp3","eliza.py"] # Include folders with mp3 files.
}

# The base parameter specifies the type of executable.
# For a console application, this is not needed.
# For a GUI application, you'd use base="Win32GUI".
base = None

setup(
    name="Eliza",
    version="1.0",
    description="Chatbot Eliza",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)