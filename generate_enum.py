import os

ICON_DIR = './src/main/resources/org/openlca/swt/material/icons'
ENUM_FILE = './src/main/java/org/openlca/swt/material/icons/MaterialIcon.java'

TEMPLATE = """
package org.openlca.swt.material.icons;

public enum MaterialIcon {

  // region generated
$$$$
  // endregion

  private final String name;

  MaterialIcon(String name) {
    this.name = name;
  }

  public IconDescriptor baseline() {
    return new IconDescriptor("baseline_" + name);
  }

  public IconDescriptor outline() {
    return new IconDescriptor("outline_" + name);
  }

  public IconDescriptor round() {
    return new IconDescriptor("sharp_" + name);
  }

  public IconDescriptor sharp() {
    return new IconDescriptor("sharp_" + name);
  }

  @Override
  public String toString() {
    return name;
  }
}
""".strip()


def main():

    prefixes = [
        'baseline_',
        'outline_',
        'round_',
        'sharp_'
    ]

    # collect all icons
    all_names: set[str] = set()
    base_names: set[str] = set()
    for f in os.listdir(ICON_DIR):
        all_names.add(f)
        for prefix in prefixes:
            if f.startswith(prefix):
                base_names.add(f.removeprefix(prefix))
                break

    # filter the icons that occur in all varians
    icons = []
    for base_name in base_names:
        has_all = True
        for prefix in prefixes:
            if f'{prefix}{base_name}' not in all_names:
                has_all = False
                break
        if has_all:
            icons.append(base_name)
    icons.sort()

    print(f'Collected {len(icons)} base icons')

    item_block = ''
    for i in range(0, len(icons)):
        icon = icons[i]
        item = icon.removesuffix('.png').upper()
        if item[0].isdigit():
            item = f'NUMBER_{item}'
        if i > 0:
            item_block = item_block + ",\n"
        item_block = item_block + f'  {item}("{icon}")'
    item_block = item_block + ";\n"

    text = TEMPLATE.replace('$$$$', item_block)
    with open(ENUM_FILE, 'w', encoding='utf-8') as f:
        f.write(text)

    print('wrote enum; done')


if __name__ == '__main__':
    main()
