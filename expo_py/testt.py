# -*- coding: utf-8 -*-

from test import testmode
from datetime import datetime

startTime = datetime.now()
df = testmode()      
print(datetime.now() - startTime)