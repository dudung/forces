import sys,os
src = os.path.join(os.getcwd(), "src")
sys.path.append(src)

from forces.constant import zero

print("forces.constant.zero")
print(zero())
