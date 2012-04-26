Sentry Notes
============

Simple plugin for `Sentry <https://github.com/dcramer/sentry/>`_ that allows for plain text notes to be added to message groups.

Getting It
----------

To install it from source, grab the git repository from github and run setup.py::

 $ git clone git://github.com/TrueCar/sentry-notes.git
 $ cd sentry-notes
 $ python setup.py install

Installation
------------

Install it somewhere reachable by Sentry's PYTHONPATH. Most commonly, that can be accomplished with the steps above in `Getting It`_.

Your ``sentry.conf.py`` should be modified similar to something like::

    from sentry.conf.server import *  # Import default settings

    # your custom configuaration here

    INSTALLED_APPS += ('sentry_notes', )  # Add sentry_notes to Sentry
