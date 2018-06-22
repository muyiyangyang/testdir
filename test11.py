# coding=utf-8

print "中文测试"
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
def fact(n):
    return fact_iter(n, 1)

