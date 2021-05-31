import subprocess
import os
import time

source = ['/home/radmir/PycharmProjects/PycharmProjects/pythonProject1/functions_A_Byte_of_Python']

target_dir = '/home/radmir/Общедоступные/teest_folder_4_backup4'

today = target_dir +os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Введите коментарий -->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Католог успешно создан', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Создание резервной копии не удалось!')
