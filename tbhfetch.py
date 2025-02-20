from config import ops
from config import de
import os
import platform
if ops == 'mac':
    ops = "\033[96mtbh, mac\033[0m"
    de = "\033[96mtbh, mac de\033[0m"
    mdl = platform.platform()
    tbhfetchout = f"""
          \033[96m.:'\033[0m
      \033[95m__ :'__\033[0m
   \033[94m.'`__`-'__``. \033[0m   {ops}
  \033[93m:__________.-'\033[0m
  \033[92m:_________:\033[0m       {de}
   \033[91m:_________`-;\033[0m
    \033[31m`.__.-.__.'\033[0m     \033[96mtbh, {mdl}\033[0m
    """
    print(tbhfetchout)