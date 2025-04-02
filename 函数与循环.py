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
    