#-*- coding: utf-8 -*-
import sys
import time
from collections import deque

print "中文测试"
fancy_loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)
