import zipfile
from PIL import Image

TARGET_DIR = "./src/main/resources/org/openlca/swt/material/icons"
ICON_ZIP = "./raw/material-design-icons-master.zip"


def main():
    with zipfile.ZipFile(ICON_ZIP, 'r') as z:
        count = 0
        for n in z.namelist():
            if matches(n):
                count += 1
        print(f'{count} images')


def matches(file_name: str) -> bool:
    if not file_name.endswith('.png'):
        return False
    path_args = [
        '/png/',
        '/materialicons/18dp/1x/'
    ]
    for arg in path_args:
        if not arg in file_name:
            return False
    return True


""""
img_dir = './src/main/resources/org/openlca/swt/material/icons'
img = Image.open(img_dir + '/lock.png')
img.resize((14, 14), Image.ANTIALIAS, box=(16, 16, 16, 16))
img.alpha_composite
img.save(img_dir + '/lock_16.png')
"""

if __name__ == '__main__':
    main()
