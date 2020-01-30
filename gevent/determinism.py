import time

def sleep_and_echo(i):
    time.sleep(0.001)
    return i

# Non Deterministic Process Pool

from multiprocessing.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]
run2 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]
run3 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]
run4 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]

print(run1 == run2 == run3 == run4)

# Deterministic Gevent Pool

from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]
run2 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]
run3 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]
run4 = [a for a in p.imap_unordered(sleep_and_echo, range(10))]

print(run1 == run2 == run3 == run4)
