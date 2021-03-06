'''
希尔排序
'''

# 1、描述
'''
  希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
  希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 
  希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
'''

# 2、算法步骤
'''
  （1）选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；
  （2）按增量序列个数 k，对序列进行 k 趟排序；
  （3）每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
'''

# 3、代码实现
def shell_sort(arr):
  count = len(arr)
  step = 2
  gap = count // step  # Python2.2开始，"/"表示除法, 结果可能为浮点数，而"//"表示整除，结果不计小数部分，直接为整数
  while gap > 0:
    for i in range(0, gap):
      j = i + gap
      while j < count:
        k = j - gap
        temp = arr[j]
        while k >= 0:
          if arr[k] > temp:
            arr[k + gap] = arr[k]
            arr[k] = temp
          k -= gap
        j += gap
    gap //= step
  return arr

# 4、示例
arr = [10, 23, 6, 8, 2, 16, 0, 9]
print(shell_sort(arr))  # 输出结果为 [0, 2, 6, 8, 9, 10, 16, 23]
