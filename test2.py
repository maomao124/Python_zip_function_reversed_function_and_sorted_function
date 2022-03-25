"""
 * Project name(项目名称)：Python_zip函数_reversed函数和sorted函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 13:12
 * Version(版本): 1.0
 * Description(描述)： reversed函数
 reserved() 是 Python 内置函数之一，其功能是对于给定的序列（包括列表、元组、字符串以及 range(n) 区间），
 该函数可以返回一个逆序序列的迭代器（用于遍历该逆序序列）。
 """
import random

if __name__ == '__main__':

    list1 = []
    i = 0
    while i < 20:
        r = random.randint(10, 99)
        list1.append(r)
        i = i + 1
    print(list1)

    re = reversed(list1)
    print(list(re))

    print([x for x in reversed(range(20))])

    input()
