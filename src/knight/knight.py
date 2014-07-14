# coding: utf-8
import os, sys
from qfcommon.base import logger
log = logger.install('stdout')
import gevent
import gevent.monkey
import gevent.socket
from gevent import socket
import msgpack, struct

def handler(socket, address):
    lenstr = socket.read(4)
    length = struck.unpack('I', lenstr)
    log.debug('length:%s', length)



def start():
    addr = ('0.0.0.0', 9090)
    client = gevent.socket.create_connection(addr)
    log.info('client connect to:%s', addr)


if __name__ == '__main__':
    start()

