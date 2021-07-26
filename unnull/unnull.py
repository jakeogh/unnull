#!/usr/bin/env python3

# pylint: disable=C0111  # docstrings are always outdated and wrong
# pylint: disable=W0511  # todo is encouraged
# pylint: disable=C0301  # line too long
# pylint: disable=R0902  # too many instance attributes
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0103  # single letter var names, func name too descriptive
# pylint: disable=R0911  # too many return statements
# pylint: disable=R0912  # too many branches
# pylint: disable=R0915  # too many statements
# pylint: disable=R0913  # too many arguments
# pylint: disable=R1702  # too many nested blocks
# pylint: disable=R0914  # too many local variables
# pylint: disable=R0903  # too few public methods
# pylint: disable=E1101  # no member for base
# pylint: disable=W0201  # attribute defined outside __init__
# pylint: disable=R0916  # Too many boolean expressions in if statement

import sys
from typing import Union

#from enumerate_input import read_by_byte


def errexit():
    print(sys.argv[0],
          'Error: -v / --verbose is the only option.',
          file=sys.stderr,)
    sys.exit(1)


def cli():
    verbose: Union[bool, int] = False
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            if arg.startswith('-v'):
                for vee in arg[1:]:
                    if vee == 'v':
                        verbose += 1
                    else:
                        errexit()
            elif arg == '--verbose':
                verbose += 1
            else:
                errexit()

    if verbose:
        import inspect
        depth = len(inspect.stack())
        verbose += depth

    for chunk in iter(lambda: sys.stdin.buffer.read(1024), b""):
        chunk = chunk.replace(b'\x00', b'\n')
        try:
            sys.stdout.buffer.write(chunk)
        except BrokenPipeError as e:
            if verbose:
                print(sys.argv[0], e, file=sys.stderr)
            sys.exit(1)

    #end = b'\n'
    #iterator = read_by_byte(sys.stdin.buffer,
    #                        byte=b'\x00',
    #                        verbose=verbose,
    #                        debug=False)

    #for line in iterator:
    #    try:
    #        sys.stdout.buffer.write(line + end)
    #    except BrokenPipeError as e:
    #        if verbose:
    #            print(sys.argv[0], e, file=sys.stderr)
    #        sys.exit(1)
