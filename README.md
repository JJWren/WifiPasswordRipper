## Credit

_The WiFi Password Ripper's primary logic was created by David Bombal:
[https://github.com/davidbombal/red-python-scripts/blob/main/windows10-wifi.py]()_

_Thanks goes to David for providing a quick and elegant solution that aids in
discovering vulnerabilities in our environments!_

## Changes

The changes made to his script are simply changing the usage of his list
to a PrettyTable using the prettytable library.

Additionally, I added the option to write the findings on a given machine to a file
in a directory of the user's choice. This will recursively ask for a directory until given
a valid one, or until the user closes the terminal window.

Finally, using pyinstaller, I created an executable for the script/program.
