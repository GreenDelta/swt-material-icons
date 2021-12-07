import zipfile
from PIL import Image

TARGET_DIR = "./src/main/resources/org/openlca/swt/material/icons"
ICON_ZIP = "./raw/material-design-icons-master.zip"


def main():
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
                break


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
    base = file_name.split('/')[-1].removesuffix('_black_18dp.png')
    return f'{TARGET_DIR}/{base}.png'


""""
img_dir = './src/main/resources/org/openlca/swt/material/icons'
img = Image.open(img_dir + '/lock.png')
img.resize((14, 14), Image.ANTIALIAS, box=(16, 16, 16, 16))
img.alpha_composite
img.save(img_dir + '/lock_16.png')
"""

if __name__ == '__main__':
    main()
