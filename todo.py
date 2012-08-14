#!/usr/bin/env python

import sys
import cli

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        cli.main(sys.argv[1:])
