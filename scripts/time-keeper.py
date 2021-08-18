import pyautogui
from datetime import datetime

import sys
print('Press Ctrl-C to quit.')
try:
    while True:
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        restx, restxtime = x, datetime.now().strftime("%Y/%m/%d, %H:%M:%S%SSS")
        print(restx, restxtime)
except KeyboardInterrupt:
    print('\n')
