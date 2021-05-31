#!/usr/bin/env python3
import os
import time

source = ['/home/radmir/PycharmProjects/PycharmProjects/pythonProject1/functions_A_Byte_of_Python']

target_dir = '/home/radmir/Общедоступные/test_folder_2_backup2'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)


target = today + os.sep + now + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')