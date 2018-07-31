"""#!/usr/local/bin/python3"""

from PIL import Image

def create_image(size=None, color=None):
    if not(size and color):
        return
    img = Image.new('RGB', size, color)
    img.save('/Users/danishprakash/programming/solid/sample.png')
    print('Done')

create_image((500, 500), 'red')

