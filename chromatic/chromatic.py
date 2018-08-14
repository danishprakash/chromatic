"""Generate monochromatic backgrounds instantly"""

import argparse
import os
import re

from imgurpython import ImgurClient
from PIL import Image
import pyperclip

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

FILE_NAME = 'monochromatic_backgrounds.png'

def create_image(size=None, color=None):
    """Return a PIL Image object."""

    return Image.new('RGB', size, color)


def save_image(image, path):
    """Save `image` to `path`"""

    global FILE_NAME
    if path:
        path = os.path.abspath(path) + '/' + FILE_NAME
    else:
        path = os.getcwd() + '/' + FILE_NAME
    image.save(path)


def upload_to_imgur(path, to_clipboard=True, open_url=False):
    """
    Uploads generated image to imgur

    Parameters:
        path (str)          : Absolute path to the image file generated.
        to_clipboard (bool) : Flag for copying image URL to clipboard.
        open_url (bool)     : Flag for opening the URL in browser.
    """

    configuration_file = '{0}/.chromatic.conf'.format(os.getenv('HOME'))
    if not os.path.isfile(configuration_file):
        with open(configuration_file, 'w') as conf:
            conf.write('[DEFAULT]\nclient_id=\nclient_secret=')

    config_parser = configparser.RawConfigParser()
    config_parser.read(configuration_file)
    client_id = config_parser.get('DEFAULT', 'client_id')
    client_secret = config_parser.get('DEFAULT', 'client_secret')

    client = ImgurClient(client_id, client_secret)
    url = client.upload_from_path('{0}/{1}'.format(path, FILE_NAME), anon=True).get('link', '404')

    if to_clipboard:
        pyperclip.copy(str(url))
        if open_url:
            try:
                os.system('open {0}'.format(url))
            except:
                raise Exception("`open` command not found.")
    else:
        print(url)


def remove_image(path):
    """Delete the generated image"""

    os.remove('{0}/{1}'.format(path, FILE_NAME))


def generate_image(args):
    """Parse arguments appropriately"""

    if args.size and args.color:
        size = tuple(int(x) for x in tuple(args.size.split(',')))
        if re.match('^#.*', args.color):
            color = tuple(int(args.color[i:i+2], 16) for i in (1, 3, 4))
        else:
            color = args.color
    else:
        raise Exception("`color` and `size` are required arguments.")

    if args.name:
        global FILE_NAME
        FILE_NAME = args.name
    if not args.path:
        args.path = os.path.abspath('.')

    save_image(create_image(size, color), args.path)

    if args.imgur:
        open_url = True if args.open else False
        upload_to_imgur(args.path, open_url=open_url)
        if args.nosave:
            remove_image(args.path)


def main():
    """Parse cli arguments and flags"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--color', help='HEX color code', type=str)
    parser.add_argument('--size', help='size of the image in LxB', type=str)
    parser.add_argument('--imgur', help='upload image to imgur and return URL', action='store_true')
    parser.add_argument('--nosave', help='don\'t save file locally', action='store_true')
    parser.add_argument('--open', help='open imgur URL in browser', action='store_true')
    parser.add_argument('--path', help='path to the file', type=str)
    parser.add_argument('--name', help='name of the image file generated', type=str)
    args = parser.parse_args()
    generate_image(args)
