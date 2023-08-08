import os
from PIL import Image
import sys
sys.path.insert(1, '/home/codio/workspace')


def test_images_exist():
    # Check if the initial image exists
    if not os.path.isfile('cool.png'):
        print("The 'cool.png' image doesn't exist")
        return False

    # Check if the rotated image exists
    if not os.path.isfile('rotated_45_cool.png'):
        print("The 'rotated_45_cool.png' image doesn't exist")
        return False

    # Check if the final image exists
    if not os.path.isfile('final_cool.png'):
        print("The 'final_cool.png' image doesn't exist")
        return False

    print("OK")
    return True


def test_images_open():
    # Try to open the initial image
    try:
        img = Image.open('cool.png')
    except IOError:
        print("The 'cool.png' image couldn't be opened")
        return False

    # Try to open the rotated image
    try:
        img = Image.open('rotated_45_cool.png')
    except IOError:
        print("The 'rotated_45_cool.png' image couldn't be opened")
        return False

    # Try to open the final image
    try:
        img = Image.open('final_cool.png')
    except IOError:
        print("The 'final_cool.png' image couldn't be opened")
        return False

    print("OK")
    return True


if __name__ == '__main__':
    test1 = test_images_exist()
    test2 = test_images_open()
    if test1 and test2:
        print("Final Test: PASS")
    else:
        print("Final Test: FAIL")
