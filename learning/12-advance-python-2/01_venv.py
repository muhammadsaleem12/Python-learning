'''Venv Virtual Environmets'''
# A venv virtual environment is an isolated,
# self-contained folder that holds a specific version of Python and its own set of packages.
# It keeps project tools separate from your main system and other projects. 
# This prevents version fights and keeps your computer clean.


# we used the command "pip install virtualenv"
# and the created "env" using the command "python -m virtualenv env" basically a python isolated environment is prepared.

# ".\env\Scripts\activate.ps1" using this cmd in the terminal of VS code or your regular cmd or powershell in the working folder where you created you vitrual environment, we can access the virtual environment.

# Note; i used the activate.ps1 file in the Scripts folders beacuse i was using powershell but if your using the terminal cmd, you might wanna use the activate.bat file in order to access the environment.


'''i tired installing pandas and the latest version 3.0.5 of pandas was installed in the global system,
    by using the isolated virtual environment i was seperately be able to install pandas 2.3.3 in the virtual environment.'''


