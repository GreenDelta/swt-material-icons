import os

ICON_DIR = './src/main/resources/org/openlca/swt/material/icons'

def main():
    items = []
    for f in os.listdir(ICON_DIR):
        item = f.removesuffix('.png').upper()
        if item[0].isdigit():
            item = f'NUMBER_{item}'
        items.append(f'{item}("{f}"),')

    for item in items:
        print(item)

if __name__ == '__main__':
    main()
