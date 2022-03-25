"""
 * Project name(项目名称)：Python_zip函数_reversed函数和sorted函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/25 
 * Time(创建时间)： 12:58
 * Version(版本): 1.0
 * Description(描述)： zip函数
 zip() 函数是 Python 内置函数之一，它可以将多个序列（列表、元组、字典、集合、字符串以及 range() 区间构成的列表）
 “压缩”成一个 zip 对象。所谓“压缩”，其实就是将这些序列中对应位置的元素重新组合，生成一个个新的元组。
 """

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [11, 22, 33, 44, 55, 66]
    z = zip(list1, list2)
    print([x for x in z])
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = [11, 22, 33, 44, 55, 66]
    list3 = [6, 8, 0, 9, 4]
    z = zip(list1, list2, list3)
    print([x for x in z])

    list4 = list(zip(list1, list2, list3))
    # print(list4)
    for i in list4:
        print(i, end="  ")

    print()
    for i in zip(list1, list2, list3):
        print(i, end="  ")

    input()
