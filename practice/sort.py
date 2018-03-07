import sys
sys.path.append('/Users/apple/Documents/GitHub/python/practice')
import utf8

utf8.setutf8()


def print_sort_options():
    print("＝＝＝可選擇的排序法如下＝＝＝")
    print("1. 氣泡排序法")
    print("2. 選擇排序法")
    print("3. 插入排序法")


def set_sort():
    sorts['1'] = bubble
    sorts['2'] = selection
    sorts['3'] = insertion


def swap(int_arr, index1, index2):
    temp = int_arr[index1]
    int_arr[index1] = int_arr[index2]
    int_arr[index2] = temp


def bubble(int_arr):
    for round in range(0, endNum, 1):
        swap_count = 0
        print("/ ROUND %d / \n %s" % (round + 1, int_arr))
        for n in range(0, endNum - round, 1):
            if(int_arr[n] > int_arr[n + 1]):
                swap(int_arr, n, n + 1)
                swap_count += 1
                print("    %s" % (int_arr))
        if(swap_count == 0):
            break


def selection(int_arr):
    for round in range(0, endNum, 1):
        print("/ ROUND %d / \n %s" % (round + 1, int_arr))
        min = int_arr[round]
        index = 0
        for n in range(round + 1, endNum + 1, 1):
            if(int_arr[n] < min):
                min = int_arr[n]
                index = n
        if(min != int_arr[round]):
            swap(int_arr, round, index)
            print("    %s" % (int_arr))


def insertion(int_arr):
    for round in range(1, endNum + 1, 1):
        temp = int_arr[round]
        n = round - 1
        print("/ ROUND %d / \n %s" % (round, int_arr))
        while n >= 0 and int_arr[n] > temp:
            int_arr[n + 1] = int_arr[n]
            print("    %s" % (int_arr))
            n = n - 1
        int_arr[n + 1] = temp
        print("    %s" % (int_arr))


if __name__ == '__main__':
    try:
        sorts = {}
        set_sort()

        seq = input("請輸入欲排序之數列，並以,隔開數字：")
        arr = list(map(int, seq.split(',')))
        endNum = len(arr) - 1

        print_sort_options()
        sort = input("請選擇排序法(輸入排序法對應之數字)：")
        if sort in sorts:
            print("----------PROCESS----------")
            sorts[sort](arr)
            print("----------RESULT----------")
            print(arr)

    except ValueError:
        print("請勿輸入數字以外的字元！")
