import os
import shutil
import zipfile
from PIL import Image

TARGET_DIR = "./src/main/resources/org/openlca/swt/material/icons"
ICON_ZIP = "./raw/material-design-icons-master.zip"


def main():
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    os.makedirs(TARGET_DIR)

    print('read zip file ...')
    with zipfile.ZipFile(ICON_ZIP, 'r') as z:

        paths = []
        for n in z.namelist():
            if matches(n):
                paths.append(n)

        print(f'convert {len(paths)} images ...')
        count = 0
        for path in paths:
            with z.open(path) as data:
                image = Image.open(data)
                image.resize((16, 16), Image.ANTIALIAS)
                image.save(target_path(path))
            count += 1
            if count % 100 == 0:
                print(f'  .. converted {count} images ..')
        print('all done')


def matches(file_name: str) -> bool:
    if not file_name.endswith('_black_18dp.png'):
        return False
    path_args = [
        '/png/',
        '/materialicons/18dp/1x/'
    ]
    for arg in path_args:
        if not arg in file_name:
            return False
    return True


def target_path(file_name: str) -> str:
    base = file_name.split('/')[-1]\
        .removesuffix('_black_18dp.png')\
        .removeprefix('baseline_')
    return f'{TARGET_DIR}/{base}.png'


if __name__ == '__main__':
    main()
