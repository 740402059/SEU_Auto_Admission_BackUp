# coding: utf-8
# Author：quzard
from admission import *
import sys, os
from time import sleep
from numpy import random

if "USERNAME" in os.environ:
    username = os.environ["USERNAME"]
else:
    print("未找到 ID")
    sys.exit(1)

if "PASSWORD" in os.environ:
    password = os.environ["PASSWORD"]
else:
    print("未找到 PASSWORD")
    sys.exit(1)

if __name__ == '__main__':
    try:
        sleep(random.uniform(5, 15))
        admission = Admission(username, password, "./")
        res = admission.do_report()
        print(res)
        if "入校申请成功" not in res or '已存在通过的申请' not in res or "存在通行证" not in res:
            sys.exit(1)
    except Exception as e:
        print(str(e))
        sys.exit(1)
