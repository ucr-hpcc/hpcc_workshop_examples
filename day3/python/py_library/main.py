#!/usr/bin/env python3

import helpers

helpers.say_hi()

## Load this file with `python -i main.py` and try the following:
# print(COLOR)              ## Should this work?
# dir()                     ## Check the symbol table
# dir(helpers)              ## COLOR isn't here, but helpers is...
# print(helpers.COLOR)      ## Based on how we imported, COLOR is part of the helpers namespace
# print(helpers.vars.COLOR) ## Try changing the commented lines in helpers.py
                            ## The difference in the symbol path affects this file as well.
