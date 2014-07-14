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
    fields = ['usr','sys','idl','wai','hiq','siq']
    data = []
    with open(path) as f:
        for line in f:
            if line.startswith('cpu'):
                p = line.strip().split()
                data.append(p)
    return data

def stat_disk():
    path = '/proc/diskstats'
    data = []
    with open(path) as f:
        for line in f.read().splitlines():
            p = line.strip().split()
            if len(p) < 13: 
                continue
            if p[3:] == ['0',]*11: 
                continue
            name = p[2]
            data.append(p[2:])
    return data

def stat_disk24():
    path = '/proc/partitions'
    data = []
    with open(path) as f:
        lines = f.read().splitlines()
        header = lines[0].split()
        for line in lines[2:]:
            item = line.split()
            for i in range(0, len(item)-1):
                item[i] = int(item[i])
            data.append(dict(zip(header, item)))
    return data

def stat_disk24old():
    path = '/proc/stat'


def stat_epoch():
    pass


def stat_fs():
    file_path = '/proc/sys/fs/file-nr'
    inode_path = '/proc/sys/fs/inode-nr'

    data = {'files':0, 'files-max':0, 'inodes':0}
    with open(file_path) as f:
        p = f.read().strip().split()
        data['files'] = int(p[0])
        data['files-max'] = int(p[2])
    with open(inode_path) as f:
        p = f.read().strip().split()
        data['inodes'] = int(p[0]) - int(p[1])
    return data

def stat_int():
    path = '/proc/interrupts'

def stat_io():
    path = '/proc/diskstats'
    fields = ['read','writ']

def stat_ipc():
    path = '/proc/sysipc'


def stat_load():
    path = '/proc/loadavg'
    fields = ['avg_5', 'avg_10', 'avg_15', 'task', 'last_pid']
    with open(path) as f:
        p = f.read().strip().split()
        data = dict(zip(fields, p)) 
    return data

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
    import pprint

    print 'aio:', stat_aio()
    print 'disk:', stat_disk()
    print 'partition:', pprint.pformat(stat_disk24())
    print 'fs:', pprint.pformat(stat_fs())
    print 'load:', pprint.pformat(stat_load())

if __name__ == '__main__':
    test()



