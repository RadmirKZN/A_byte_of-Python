#!/usr/bin/env python3
import os
import time

source = ['/home/radmir/PycharmProjects/PycharmProjects/pythonProject1/functions_A_Byte_of_Python']

target_dir = '/home/radmir/Общедоступные/test_folder_1_backup1'


target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось!')
