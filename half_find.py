# 二分查找
def half_find(target, arr):
    size = len(arr)
    if size == 0:
        return False
    mid = size // 2
    if target < arr[mid]:
        num_low = arr[0:mid]
        return half_find(target, num_low)
    elif target > arr[mid]:
        num_high = arr[mid + 1:]
        return half_find(target, num_high)
    else:
        return arr[mid]


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 10, 11, 11, 11,
            11, 12, 13, 13, 15, 16, 16, 20, 21, 21, 23, 24, 26,
            26, 27, 28, 28, 31, 33, 33, 34, 35, 38, 38, 39, 40,
            42, 43, 45, 45, 46, 46, 47, 47, 51, 52, 52, 53, 53,
            55, 55, 56, 56, 57, 57, 57, 58, 59, 61, 62, 64, 66,
            66, 67, 68, 69, 69, 71, 72, 72, 74, 74, 75, 76, 78,
            78, 79, 79, 79, 79, 80, 82, 85, 88, 89, 90, 90, 91,
            91, 91, 94, 99, 99]
    print(half_find(40, nums))
