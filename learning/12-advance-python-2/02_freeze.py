'''pip freeze'''
# returns all the package installed in a given python environment along with the versions.

'''OUTPUT'''
# as you can see these are all the packages installed in my system (Virtual Environment).
# numpy==2.5.2
# pandas==2.3.3  -> its the older version as we installed earlier.
# python-dateutil==2.9.0.post0
# pytz==2026.3.post1
# six==1.17.0
# tzdata==2026.3

'''pip freeze > requirements.txt'''

# The above command creates a file named 'requirements.txt' in the same directory containing the output of 'pip freeze'.

# we can distribute this file to other users, and they can recreate the same enviroment using:
'''pip install -r requirements.txt'''



