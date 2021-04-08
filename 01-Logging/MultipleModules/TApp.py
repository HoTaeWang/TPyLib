#!/usr/bin/env python3

import logging as log
import mylib

def main():
    log.basicConfig(filename='tapp.log', level=log.INFO)
    log.info('Started')
    mylib.do_something()
    log.info('Finished')

if __name__ == '__main__':
    main()

