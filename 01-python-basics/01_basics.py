"""
文件: day01/01_basics.py
Python vs C++ 对照学习
"""

# 声明变量
x=11
y=1.23
name="hello"
flag=True

# 查看变量类型
print(type(x))          # <class 'int'>
print(type(y))          # <class 'float'>
print(type(name))       # <class 'str'>
print(type(flag))       # <class 'bool'>

# python的数字没有溢出，比如计算10的100次方
num=10**100
print(num)   #打印结果是10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


# 变量可以赋值不同类型的值
x=11        # 赋值为int类型
x="abc"     # 赋值为str类型
x=True      # 赋值为bool类型
x=[1,2,3]   # 赋值为list类型


# 字符串操作
str1="hello"
str2='world'    # 单引号双引号都行
str3="""
双引号
这是多行字符串
可以直接换行
类似C++的R"(raw string)"
"""
str4='''
单引号
这是多行字符串
可以直接换行
类似C++的R"(raw string)"
'''
print(str1)
print(str2)
print(str3)
print(str4)

# 字符串拼接
str5=str1+" "+str2
print(str5) # hello world

# 字符串格式化
model_name="YOLOv8"
fps=30.5
info=f"模型{model_name}的帧率是{fps:0.1f}FPS"
print(info) # 模型YOLOv8的帧率是30.5FPS

# 字符串方法
path="/home/user/model.onnx"
print(path.split('/')) # ['', 'home', 'user', 'model.onnx']
print(path.endswith("onnx")) # True
print(path.replace("onnx","engine")) # /home/user/model.engine

# 字符串索引和切片
str1="0123456"
print(str1[0])     # 0
print(str1[-1])    # 6
print(str1[2:5])   # 234
print(str1[:3])    # 012
print(str1[3:])    # 3456