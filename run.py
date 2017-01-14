import os
import Skype4Py


TARGET_FILE = os.path.join(os.path.expanduser('~'), 'SkypeContacts.txt')

if __name__ == '__main__':
    if os.path.exists(TARGET_FILE):
        print('Backup file already exists. Rename it or move it away.')
        exit(0)

    skype = Skype4Py.Skype()
    skype.Attach()
    handles = [user.Handle for user in skype.Friends]

    with open(TARGET_FILE, 'w') as backup:
        backup.writelines(handles)

    print('{} contacts saved'.format(len(handles)))
