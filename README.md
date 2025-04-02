# 仇河东 324085503103 24机械1班 github：(https://github.com/Key407/12345)
## 1、循环与函数.py：3个计算功能的代码
```python
# 定义一个计算阶乘的函数
def factorial(n):
    # 检查输入的 n 是否为整数且为非负整数
    if not isinstance(n, int) or n < 0:
        # 如果不满足条件，抛出 ValueError 异常
        raise ValueError("输入必须为非负整数")
    # 初始化阶乘结果为 1
    result = 1
    # 使用 for 循环从 1 到 n 进行迭代
    for i in range(1, n + 1):
        # 每次迭代将当前的 i 乘到结果中
        result *= i
    # 返回计算得到的阶乘结果
    return result


# 定义一个判断素数的函数
def is_prime(n):
    # 如果 n 小于 2，因为素数定义要求大于 1，所以直接返回 False
    if n < 2:
        return False
    # 使用 for 循环遍历从 2 到 n 的平方根的所有整数
    for i in range(2, int(n**0.5) + 1):
        # 如果 n 能被当前的 i 整除，说明 n 不是素数，返回 False
        if n % i == 0:
            return False
    # 如果循环结束都没有找到能整除 n 的数，说明 n 是素数，返回 True
    return True


# 定义一个生成斐波那契数列的函数
def fibonacci(n):
    # 如果 n 为 0，斐波那契数列长度为 0，返回空列表
    if n == 0:
        return []
    # 如果 n 为 1，斐波那契数列只有一个元素 0，返回 [0]
    elif n == 1:
        return [0]
    # 初始化斐波那契数列的前两个元素
    sequence = [0, 1]
    # 使用 while 循环不断添加新元素到数列中，直到数列长度达到 n
    while len(sequence) < n:
        # 新元素为数列中最后两个元素之和
        sequence.append(sequence[-1] + sequence[-2])
    # 返回生成的斐波那契数列
    return sequence


# 进入一个无限循环，用于和用户进行交互
while True:
    # 打印功能选择菜单
    print("请选择要执行的功能：")
    print("1. 计算阶乘")
    print("2. 判断素数")
    print("3. 打印斐波那契数列")
    print("4. 退出")
    # 获取用户输入的选项
    choice = input("请输入选项（1-4）：")

    # 如果用户选择 1，执行计算阶乘的功能
    if choice == '1':
        try:
            # 提示用户输入一个非负整数
            num = int(input("请输入一个非负整数来计算阶乘："))
            # 调用 factorial 函数计算阶乘并打印结果
            print(f"{num} 的阶乘是：{factorial(num)}")
        except ValueError as e:
            # 如果输入不合法，捕获异常并打印错误信息
            print(e)
    # 如果用户选择 2，执行判断素数的功能
    elif choice == '2':
        try:
            # 提示用户输入一个整数
            num = int(input("请输入一个整数来判断是否为素数："))
            # 调用 is_prime 函数判断是否为素数并打印结果
            if is_prime(num):
                print(f"{num} 是素数。")
            else:
                print(f"{num} 不是素数。")
        except ValueError:
            # 如果输入不合法，捕获异常并打印错误信息
            print("输入必须为整数。")
    # 如果用户选择 3，执行打印斐波那契数列的功能
    elif choice == '3':
        try:
            # 提示用户输入一个整数作为斐波那契数列的长度
            num = int(input("请输入一个整数来生成斐波那契数列的长度："))
            # 调用 fibonacci 函数生成斐波那契数列并打印结果
            print(f"长度为 {num} 的斐波那契数列是：{fibonacci(num)}")
        except ValueError:
            # 如果输入不合法，捕获异常并打印错误信息
            print("输入必须为整数。")
    elif choice == '4':
        print("程序已退出。")
        break
    else:
        print("无效的选项，请输入 1-4 之间的数字。")
```

### 功能描述
编写了一个名为循环与函数.py的文件，文件中的代码实现了三个计算功能：计算阶乘、判断素数和生成斐波那契数列
### 使用方法
1、保存循环与函数.py文件

2、在终端或命令行中执行启动程序

3、按提示操作


## 2、系统信息收集
```bash
#!/bin/bash

# 显示当前用户
current_user=$(whoami)
echo "当前用户: $current_user"

# 显示当前系统时间
current_time=$(date)
echo "当前系统时间: $current_time"

# 显示cpu负载情况
cpu_load=$(uptime)
echo "CPU负载情况: $cpu_load"

# 显示磁盘使用情况
disk_usage=$(df -h)
echo "磁盘使用情况:"
echo "$disk_usage"

# 显示当前内存使用情况
memory_usage=$(free -m)
echo "当前内存使用情况:"
echo "$memory_usage"

# 将输出结果保存到system_report.txt
{
    echo "当前用户: $current_user"
    echo "当前系统时间: $current_time"
    echo "CPU负载情况: $cpu_load"
    echo "磁盘使用情况:"
    echo "$disk_usage"
    echo "当前内存使用情况:"
    echo "$memory_usage"
} > system_report.txt

echo "系统信息已保存到 system_report.txt"
    
```

### 功能描述
编写了一个名为sys_info.sh的Bash脚本，用于收集并保存系统信息。脚本执行后会显示并保存以下信息到system_report.txt文件中。
### 使用方法
1、保存脚本sys_info.sh文件

2、赋予执行权限，在终端中运行以下命令为脚本文件添加执行权限：
```bash
chmod +x sys_info.sh
```

3、执行脚本：
```bash
./sys_info.sh
```
执行完成后，脚本会在当前目录下生成一个system_report.txt文件，其中包含了当前用户、时间、CPU 负载、磁盘使用情况、内存使用情况等信息。

4、查看输出：
```bash
cat system_report.txt
```


## 3、批量创建用户
```bash
#!/bin/bash
while IFS= read -r username
do
    if id "$username" &>/dev/null; then
        echo "用户 $username 已存在，跳过创建。"
    else
        useradd "$username"
        if [ $? -eq 0 ]; then
            echo "用户 $username 创建成功！"
        else
            echo "创建用户 $username 失败！"
        fi
    fi
done < user_list.txt
```

### 功能描述
该脚本用于批量创建用户。
它会从user_list.txt文件中逐行读取用户名，并检查用户是否存在：
如果用户已存在，则跳过该用户，并输出提示信息。
如果用户不存在，则使用useradd命令创建该用户，并输出创建成功或失败的提示。
### 使用方法
1、保存脚本create_users.sh文件

2、创建一个名为 user_list.txt`的文件，按行列出需要创建的用户名

3、为脚本添加执行权限：
```bash
chmod +x create_users.sh
```
