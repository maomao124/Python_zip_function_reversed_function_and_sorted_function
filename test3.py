"""
 * Project name(项目名称)：Python_zip函数_reversed函数和sorted函数
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 13:20
 * Version(版本): 1.0
 * Description(描述)： sorted函数
 其功能是对序列（列表、元组、字典、集合、还包括字符串）进行排序。
 sorted() 函数不会改变所传入的序列，而是返回一个新的、排序好的列表。
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
    list2 = sorted(list1)
    print(list2)

    a = (5, 9, 3, 1, 8, 5)
    print(sorted(a))

    list3 = sorted(list1, reverse=True)
    print(list3)

    list4 = ["1", "211111", "311", "1111", "11", "111111111", "11111"]
    print(sorted(list4))
    print(sorted(list4, key=lambda x: len(x)))

    input()
