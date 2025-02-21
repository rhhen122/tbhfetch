from config import ops
from config import de
import os
import platform
from config import linuxdistro
if ops == 'mac':
    ops = "\033[96mtbh, mac\033[0m"
    if de == "mac": de = "mac desktop enviroment"
    de = f"\033[96mtbh, {de}\033[0m"
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

elif ops == 'arch':
    ops = "\033[35mtbh, arch linux\033[0m"
    if de == "kde": de = "KDE Plasma"
    de = f"\033[35mtbh, {de}\033[0m"
    mdl = platform.platform()
    tbhfetchout = f"""
      \033[96m**
     \033[96m*  *
    \033[96m* ** *                {ops}
   \033[96m* *  * *
  \033[96m* *    * *              {de}
 \033[96m* *      * *
\033[96m* *        * *            \033[35mtbh, {mdl}\033[0m
    """
    print(tbhfetchout)

elif ops == 'linux':
    ops = f"\033[94mtbh, {linuxdistro}\033[0m"
    if de == "kde": de = "KDE Plasma"
    de = f"\033[94mtbh, {de}\033[0m"
    mdl = platform.platform()
    tbhfetchout = f"""
\033[33m _\033[0m
\033[33m| |\033[0m
\033[33m| |\033[0m                         {ops}
\033[33m| |\033[0m
\033[33m| |\033[0m                         {de}
\033[33m| |____________\033[0m
\033[33m(______________|\033[0m            \033[94mtbh, {mdl}\033[0m
    """
    print(tbhfetchout)