<h1 align="center">chromatic</h1>
<p align="center">Create monochromatic backgrounds instantly</p>
<p align="center">
<img src="https://i.imgur.com/pNYTBJU.gif" height="500">
</p>

[![Downloads](https://pepy.tech/badge/chromatic)](https://pepy.tech/project/chromatic)

## Installation

#### pip

```sh
$ pip install chromatic
```

#### Manual

```sh
$ git clone https://github.com/danishprakash/chromatic.git && cd chromatic
$ python3 setup.py install
```

#### Imgur API
If you wish to use `--imgur` option which uploads the generated file to imgur and copies the image link to the clipboard, you'd need the API keys, namely `client_id` and `client_secret`
These are fairly easy to obtain.
1. Register [here](https://imgur.com/signin?redirect=https%3A%2F%2Fapi.imgur.com%2Foauth2%2Faddclient)
2. Copy your keys to `~/.chromatic.conf`

```conf
[DEFAULT]
client_id=<your_id>
client_secret=<your_secret>
```

Your config file should already be present in your home dir `~/.chromatic.conf` and if it's not, then run `chromatic` once without any options or create the file manually.

## Usage

```sh
usage: chromatic [-h] [--color COLOR] [--size SIZE] [--imgur] [--nosave] [--open]
              [--path PATH] [--name NAME]

optional arguments:
  -h, --help     show this help message and exit
  --color COLOR  HEX color code
  --size SIZE    size of the image in LxB
  --imgur        upload image to imgur and return URL
  --nosave       don't save file locally
  --open         open imgur URL in browser
  --path PATH    path to the file
  --name NAME    name of the image file generated
```

## Why?
I've had countless instances wherein I need a solid background image with a given size and color, and after going through the various solid background generators on the web, I end up using photoshop to do the same, which in itself is a tedious task.

## Contributing
Do you want to make this better? Open an issue and/or a PR on Github. Thanks!

## License
MIT License

Copyright (c) 2018 [Danish Prakash](https://github.com/danishprakash)

---
