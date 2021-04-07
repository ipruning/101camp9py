import pol
import sys


print("sys.path: ", sys.path)
print("pol     : ", pol)
print("pol path: ", pol.__path__)
print("dir     : ", dir())

pol.app.ch1()  # 调用某个实例
