## BITBOT GUI

------------------

A simple bit-distortion program for randomly overriding different segments of data from any given byte stream. Works particularly well for images.

### TODO:

* Need to implement the 'Attempt Photo Fix' functionality
* Fine-tune bit distortion algorithm with other, more interesting methods
* Address other various graphical bugs
* Fix lack of icon in .exe
* Fix missing GitHub logo in .exe

#### venv setup:

On Windows, run `call Scripts/activate` from the `/bitbot/` directory.


#### Compiling Executables

From root directory: `pyinstaller --noconsole -i ./bitbot-logo.ico --onefile bitbot-gui/main.py`
