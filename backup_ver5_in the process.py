import zipfile
import time

source = ['/home/radmir/PycharmProjects/PycharmProjects/pythonProject1/functions_A_Byte_of_Python']

target_dir = '/home/radmir/Общедоступные/test_folder_1_backup5'

today = target_dir + zipfile + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Введите коментарий -->')
if len(comment) == 0:
    target = today + zipfile + now + '.zip'
else:
    target = today + zipfile+ now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Католог успешно создан', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в ', target)
else:
    print('Создание резервной копии не удалось!')