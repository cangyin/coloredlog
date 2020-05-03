Colorize your console output.  
Provides `ConsoleHandler()` for working with `logging` module to get colored logging message.

# Usage Example
## 1. Colorize your logging output
```python
# you can just do `from colorlog import *`
import logging, coloredlog
logging.basicConfig(
    format='%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s',
    handlers=[coloredlog.ConsoleHandler()],
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

logger.info('logging started')
logger.debug('debug message')
logger.info('informative')
logger.log(coloredlog.NOTIFY, 'notification')
logger.warning('a warning message')
logger.error('message on error occurred')
try:
    raise RuntimeError('An exception!')
except:
    logger.exception('Exception:')
logger.critical('THIS IS CRITICAL')

```
**Result on Windows 10**
![result](https://raw.githubusercontent.com/cangyin/coloredlog/master/snapshots/snapshot1.png)


## 2. Decorate your normal message
```python
from coloredlog.color import *

print(deco('Hello, ', 0x011, bold=True) + reset() + 'world!')
print(deco('Hello, ', reverse=True) + reset() + 'world!')
print(deco('Hello, ', FG_BLUE, bold=True) + reset() + 'world!')
print(deco('Hello, ', FG_YELLOW, BG_GREEN, bold=True) + reset() + 'world!')
print(deco('Hello, ', FG_MAGENTA, bold=True) + reset() + 'w...')

# Simple convenience functions
warning("emmm, seems there is a small proble...")
error('Unknown error!')
```
_For more information on parameter rules for deco( ), please refer to the docstring._

**Result on Windows 10**
![result](https://raw.githubusercontent.com/cangyin/coloredlog/master/snapshots/snapshot2.png)

## 3. For **intensive** use case 
Since a complete run-through of `deco()` can be a bit time-consuming under intensive use case, you may consider method below to speed up the operation of `deco()`
```python
from coloredlog.color import *

const_deco = deco('', FG_BLUE, BG_WHITE, bold=True)
# simulates intensive use case
for i in range(10):
    print(deco('Hello world for {} times'.format(i), const_deco=const_deco)) # `deco()` will return immediately

print(reset()) # reset to normal color
```
**Result on Windows 10**
![result](https://raw.githubusercontent.com/cangyin/coloredlog/master/snapshots/snapshot3.png)


# Tested on
- Windows 10 (python 3.6)
- Ubuntu 16.4.1 (python 3.5)
