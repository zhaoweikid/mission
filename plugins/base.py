# coding: utf-8


def stat_aio():
    path = '/proc/sys/fs/aio-nr'
    fields = ['aio']
    data = [fields, ]
    with open(path) as f:
        data.append([int(f.read())])
    return data

def stat_cpu():
    path = '/proc/stat'
    fields = ['usr','sys','idl','wai','hiq','siq']
    data = [fields, ]
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
        data.append(header)
        for line in lines[2:]:
            item = line.split()
            for i in range(0, len(item)-1):
                item[i] = int(item[i])
            data.append(item)
    return data

def stat_disk24old():
    path = '/proc/stat'


def stat_epoch():
    pass


def stat_fs():
    file_path = '/proc/sys/fs/file-nr'
    inode_path = '/proc/sys/fs/inode-nr'
    fields = ['files','files-max','inodes']
    data = [fields, [0,0,0]]
    row = data[1]
    with open(file_path) as f:
        p = f.read().strip().split()
        row[0] = int(p[0])
        row[1] = int(p[2])
    with open(inode_path) as f:
        p = f.read().strip().split()
        row[2] = int(p[0]) - int(p[1])
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
    data = [fields, ]
    with open(path) as f:
        p = f.read().strip().split()
        #data = dict(zip(fields, p)) 
        data.append(p)
    return data

def stat_lock():
    path = '/proc/locks'

def stat_mem():
    path = '/proc/meminfo'
    fields = ['total','free','buffer','cached','used']
    data = [fields, [0,0,0,0,0]]
    row = data[1]
    with open(path) as f:
        lines = f.readlines()[:5]
        for line in lines:
            p = line.split()
            if line.startswith('MemTotal'):
                row[0] = int(int(p[1])/1024.0)
            elif line.startswith('MemFree'):
                row[1] = int(int(p[1])/1024.0)
            elif line.startswith('Buffers'):
                row[2] = int(int(p[1])/1024.0)
            elif line.startswith('Cached'):
                row[3] = int(int(p[1])/1024.0)
    
    row[4] = row[0] - row[1] - row[2] - row[3] 
    return data

def stat_net():
    path = '/proc/net/dev'
    fields = ['interface','send_bytes','send_packets','recv_bytes','recv_packets']
    data = [fields, ]
    with open(path) as f:
        lines = f.readlines()
        for line in lines[2:]:
            p = line.strip().split()
            row = [p[0][:-1], int(p[9]), int(p[10]), int(p[1]), int(p[2])]
            data.append(row)
    return data


def stat_page():
    path = '/proc/vmstat'
    fields = ['page_in', 'page_out', 'swap_in', 'swap_out']
    data = [fields, ]
    with open(path) as f:
        x = dict([ ln.strip().split() for ln in f.readlines() ])
        data.append([int(x['pgpgin']), int(x['pgpgout']),
                    int(x['pswpin']), int(x['pswpout'])])
    return data

def stat_page24():
    path = '/proc/stat'

def stat_proc():
    path = '/proc/stat'
    with open(path) as f:
        x = [ ln.split() for ln in f.readlines()]


def stat_raw():
    path = '/proc/net/raw'

def stat_socket():
    path = '/proc/net/sockstat'
    with open(path) as f:
        pass

    
def stat_swap():
    path = '/proc/swaps'
    data = []
    with open(path) as f:
        p = [ x.split() for x in f.readlines() ]
        header = [ x.lower() for x in p[0] ]
        data.append(header)
        for row in p[1:]:
            for i in range(len(row)-3, len(row)):
                row[i] = int(row[i])
            data.append(row)     
    return data

def stat_swapold():
    path = '/proc/meminfo'
    fields = ['total','free']
    data = [fields, [0,0]]
    with open(path) as f:
        p = [ x.strip().split() for x in f.readlines() ]
        for row in p:
            if row[0].startswith('SwapTotal'):
                data[1][0] = int(row[1])
            elif row[0].startswith('SwapFree'):
                data[1][1] = int(row[1])
    return data



def stat_sys():
    path = '/proc/stat'

def stat_tcp():
    path = '/proc/net/tcp'
    data = []
    with open(path) as f:
        p = [ x.split() for x in f.readlines() ]
        header = p[0]
        data.append(header)
        for row in p[1:]:
            if len(row) < len(header):
                row += ['',]*(len(header)-len(row))
            data.append(row) 
    return data

def stat_udp():
    path = '/proc/net/udp'
    data = []
    with open(path) as f:
        p = [ x.split() for x in f.readlines() ]
        header = p[0]
        data.append(header)
        for row in p[1:]:
            if len(row) < len(header):
                row += ['',]*(len(header)-len(row))
            data.append(row) 
    return data


def stat_unix():
    path = '/proc/net/unix'
    data = []
    with open(path) as f:
        p = [ x.split() for x in f.readlines() ]
        header = [ x.lower() for x in p[0] ]
        data.append(header)
        for row in p[1:]:
            if len(row) < len(header):
                row += ['',]*(len(header)-len(row))
            data.append(row) 
    return data


def stat_vm():
    path = '/proc/vmstat'
    fields = ['majpf','minpf','alloc','free']
    data = [fields, ]
    with open(path) as f:
        x = dict([ ln.strip().split() for ln in f.readlines() ])
        row = [int(x['pgmajfault']), int(x['pgfault']), 0, int(x['pgfree'])]

        for k,v in x.iteritems():
            if k.startswith('pgalloc_'):
                row[2] += int(v)
        data.append(row)
    return data



def test():
    import pprint

    print 'aio:', stat_aio()
    print 'disk:', stat_disk()
    print 'partition:', pprint.pformat(stat_disk24())
    print 'fs:', pprint.pformat(stat_fs())
    print 'load:', pprint.pformat(stat_load())
    print 'mem:', pprint.pformat(stat_mem())
    print 'net:', pprint.pformat(stat_net())
    print 'page:', pprint.pformat(stat_page())
    print 'swap:', pprint.pformat(stat_swap())
    print 'swapold:', pprint.pformat(stat_swapold())
    print 'tcp:', pprint.pformat(stat_tcp())
    print 'udp:', pprint.pformat(stat_udp())
    #print 'unix:', pprint.pformat(stat_unix())
    print 'vm:', pprint.pformat(stat_vm())

if __name__ == '__main__':
    test()



