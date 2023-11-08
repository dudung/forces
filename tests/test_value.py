import sys,os
src = os.path.join(os.getcwd(), "src")
sys.path.append(src)

from forces.constant import value

print("forces.constant.value")
print(value([2, 1, 2]))

print("forces.constant.value")
print(value(5))

print("forces.constant.value")
print(value([3, 4]))

print("forces.constant.value")
print(value([10]))
