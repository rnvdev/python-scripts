#!/usr/bin/env python3

"""This is a multi-line commenter

So, here we can describe sucintly whats this scrip do.
Atention, keep this block in 20 lines.
"""


__version__ = "0.0.1"
__author__ = "Raphael Viana"
__license__ = "Unlicense"

import os

# Here we get the environment variable called LANG and with don't exists we set default "en_US" 
# Fron environment variable LANG we get only five firt letters [:5]
current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

