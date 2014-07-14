# coding: utf-8


def stat_aio():
    path = '/proc/sys/fs/aio-nr'
    fields = ['aio']
    data = {}
    with open(path) as f:
        data['aio'] = int(f.read())
    return data


def stat_cpu():
    path = '/proc/stat'


def stat_disk():
    path = '/proc/diskstats'


def stat_disk24():
    path = '/proc/partitions'


def stat_disk24old():
    path = '/proc/stat'


def stat_epoch():
    pass


def stat_fs():
    path = '/proc/sys/fs/file-nr'
    path = '/proc/sys/fs/inode-nr'

def stat_int():
    path = '/proc/interrupts'

def stat_io():
    path = '/proc/diskstats'
    fields = ['read','writ']

def stat_ipc():
    path = '/proc/sysipc'


def stat_load():
    path = '/proc/loadavg'

def stat_lock():
    path = '/proc/locks'

def stat_mem():
    path = '/proc/meminfo'

def stat_net():
    path = '/proc/net/dev'

def stat_page():
    path = '/proc/vmstat'

def stat_page24():
    path = '/proc/stat'

def stat_proc():
    path = '/proc/stat'

def stat_raw():
    path = '/proc/net/raw'

def stat_socket():
    path = '/proc/net/sockstat'
    
def stat_swap():
    path = '/proc/swaps'

def stat_swapold():
    path = '/proc/meminfo'


def stat_sys():
    path = '/proc/stat'

def stat_tcp():
    path = '/proc/net/tcp'

def stat_udp():
    path = '/proc/net/udp'

def stat_unix():
    path = '/proc/net/unix'

def stat_vm():
    path = '/proc/vmstat'


def test():
    stat_aio()

if __name__ == '__main__':
    test()



