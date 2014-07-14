# coding: utf-8
import os, sys
from qfcommon.base import logger
log = logger.install('stdout')
import gevent
import gevent.monkey
gevent.monkey.patch_all()

from gevent.server import StreamServer
import msgpack, struct

def handler(socket, address):
    lenstr = socket.read(4)
    length = struck.unpack('I', lenstr)
    log.debug('length:%s', length)



def start():
    addr = ('0.0.0.0', 9090)
    serv = StreamServer(addr, handler)
    log.info('server start at:%s', addr)
    serv.serve_forever()

if __name__ == '__main__':
    start()

