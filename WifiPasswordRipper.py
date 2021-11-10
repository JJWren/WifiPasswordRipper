import os
import platform
import subprocess
import re
import time
from prettytable import PrettyTable
from datetime import date


def main():
    command_output = subprocess.run(
        ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

    profile_names = (re.findall(
        "All User Profile     : (.*)\r", command_output))

    ptable = PrettyTable()
    comp_name = platform.node()
    title = f'WiFi Profiles - [{comp_name}]'
    ptable.field_names = ['ID', 'SSID', 'Password']
    ptable.align['ID'] = 'c'
    ptable.align['SSID'] = 'l'
    ptable.align['Password'] = 'r'
    ptable.border = False

    if len(profile_names) != 0:
        count = 1
        for name in profile_names:
            wifi_profile = {}

            profile_info = subprocess.run(
                ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                wifi_profile["ssid"] = name

                profile_info_pass = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()

                password = re.search(
                    "Key Content            : (.*)\r", profile_info_pass)

                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]

                ptable.add_row([count, wifi_profile["ssid"],
                                wifi_profile["password"]])
                count += 1

    print(title)
    print(ptable)

    def write_creds_to_file():
        directory = input(
            '\nEnter a directory you wish to write the WiFi credentials too:  ')

        if os.path.isdir(directory):
            now = date.today().strftime('%Y-%m-%d')
            file_name = f'{now}_WiFiProfiles_{comp_name}.txt'
            fullpath = f'{directory}\\{file_name}'

            with open(fullpath, 'w') as new_file:
                new_file.write(ptable.get_string())
        else:
            print(f'"{directory}" did not exist.\nPlease try again...')
            write_creds_to_file()

    write_creds_to_file()


if __name__ == '__main__':
    print('Welcome to WiFi Password Ripper!')
    print('*' * 32 + '\n')
    main()
    print('\n' + '*' * 32)
    print('This concludes WiFi Password Ripper.\nGoodbye!')
    time.sleep(5)
