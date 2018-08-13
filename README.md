<h1 align="center">chromatic</h1>
<p align="center">Create monochromatic backgrounds instantly</p>
<p align="center">
<img src="https://i.imgur.com/pNYTBJU.gif" height="500">
</p>

## Installation

#### pip

```sh
$ pip install chromatic
```

#### Manual

```sh
$ git clone https://github.com/prakashdanish/chromatic.git && cd chromatic
$ python3 setup.py install
```

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

Copyright (c) 2018 [Danish Prakash](https://github.com/prakashdanish)

---
