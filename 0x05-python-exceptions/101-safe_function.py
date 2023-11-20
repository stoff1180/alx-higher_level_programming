#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ar = fct(*args)
        return ar
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
