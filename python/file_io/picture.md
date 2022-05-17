# 图片读写

```python
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    for i in range(1, 101):
        print(i, end=",")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    aa = Image.open("C:/cmder/icons/ubuntuorange.png")
    # aa.size = (77, 78)
    aa.save('a.ico', quality=100)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

```