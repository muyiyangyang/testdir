#!/usr/bin/python
#coding=utf-8

#自定义函数，实现二分查找，并返回查找结果
def search(find, list1) :
  low = 0
  high = len(list1)
  while low <= high :
    mid = (low + high) / 2
    if list1[mid] == find :
      return mid
    #左半边
    elif list1[mid] > find :
      high = mid -1
    #右半边
    else :
      low = mid + 1
  #未找到返回-1
  return -1

list1 = [1,2,3,7,8,9,10]
print search(11, list1)
