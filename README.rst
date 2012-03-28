About
=====
Modifies `reddit's image cropping algorithm
<https://github.com/reddit/reddit/blob/master/r2/r2/lib/scraper.py>`_
to accept an image of any dimension to produce a square thumbnail. This is
sometimes referred to as smart-cropping.

Produces an NxN-sized thumbnail of an image without distortion. For example,
a 100px x 50px image can be converted to a 25px x 25px thumbnail. First, the
100x50 will be cropped to 50x50, then reduced to 25x25. The cropping algorithm
works by calculating the entropy of an image and slicing off the side that has
the least entropy.

Installation
============
Runnning setup script installs ``pycrop`` and all its dependencies::

  python setup.py install

.. note::

  ``pycrop`` requires `PIL <http://www.pythonware.com/products/pil/>`_,
  which will be compiled if necessary. However, make sure, that all
  necessary library headers supporting different image files formats
  are installed.

Usage
=====

Basic usage::

  from PIL import Image
  import pycrop

  image = Image.open(path_to_file)
  thumb = pycrop.prepare_image(image, (200,200))
  thumb.save(new_filename, 'JPEG')

API Functions
=============

.. function:: prepare_image(Image, (x, y))
   :module: pycrop

   Takes a PIL Image object and a tuple of the dimensions.
