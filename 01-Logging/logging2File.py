#!/usr/bin/env python3


import logging as log

log.basicConfig(filename='trace.log', level=log.DEBUG)
log.debug('This message should go to the logfile')
log.info('Wing-ga-di-woomb Ra-bi-oo-sa')
log.warning('And this, too')
log.error('and non-ascii stuffs, 저장 했습')

