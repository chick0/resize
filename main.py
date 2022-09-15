from os import mkdir
from os import listdir
from os.path import join
from os.path import exists
try:
    from PIL import Image
except ImportError:
    from sys import exit
    print("** You need to install 'Pillow' to use this script. **")
    exit(-1)

INPUT = join(".", "input")
OUTPUT = join(".", "output")


def test_dir() -> None:
    for target in [INPUT, OUTPUT]:
        if not exists(target):
            mkdir(target)


def resize() -> None:
    for file in listdir(INPUT):
        print(file)
        image = Image.open(join(INPUT, file))
        width, height = image.size

        P = 1920
        if width >= P:
            q = height / (width / P)
            q = height - q

            height = height - q
            width = P

            image = image.resize((width, int(height)))

        name: str = file.rsplit(".", 1)[0]
        image.save(join(OUTPUT, name + ".png"))


if __name__ == "__main__":
    test_dir()
    resize()
