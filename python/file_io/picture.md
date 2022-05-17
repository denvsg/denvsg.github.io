# 图片读写

```python
# This is a sample Python script about modify format of picture.

from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    for i in range(1, 101):
        print(i, end=",")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    pic = Image.open("C:/cmder/icons/ubuntuorange.png")
    # aa.size = (77, 78)
    pic.save('a.ico', quality=100)
```