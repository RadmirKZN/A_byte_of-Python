import os
import time

source = 'home/radmir/PycharmProjects/PycharmProjects/pythonProject1/functions_A_Byte_of_Python'

target_dir = 'home/radmir/test_folder_1_backup1'

today = time.strftime('%Y%m%d')
target_dir = os.path.join(target_dir, today)

comment = input('Введите коментарий -->')

target = time.strftime('%H%M%S')
if len(comment) != 0:
    target +=  '_' + comment.replace(' ', '_')

target += '.zip'

try:
    os.mkdir(target_dir)
    print('Католог успешно создан', today)
except OSError as error:
    print('Похоже, папка уже существовала')

zip_command = f"zip -qr {os.path.join(target_dir, target)} {source}"
print(zip_command)

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Создание резервной копии не удалось!')