递归函数

    满足两个条件
        * 函数内部调用自身
        * 具有退出循环，即递归的边界条件
        
计算阶乘 n! = 1 * 2 * 3 * ... * n

```python
def cal_num(num):
    #定义的这个函数本身就是为了计算阶乘的,比如要计算n~(n-1)的阶乘
    # 只需要n * cal_num(n-1)后面只需要调用函数本身计算阶乘即可
    if num > 1:
        result = num * cal_num(num - 1)
        return result
    else:
        result = 1 #num=1即为边界
        return result

print(cal_num(39))
```

    斐波那契数列指的是这样一个数列 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，........
    
        特点： 前面两个数的和等于第三个数
```python
def get_num(num):
    if num > 2:
        return get_num(num-1)+ get_num(num-2)
    else:
        result = 1
        return result

nums = []
for i in range(1 , 21):
    nums.append(get_num(i))

print(nums)
```