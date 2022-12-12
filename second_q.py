# count sort
import random

def count_sort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
    # Create a count array to store count of inidividul
    max_value = max(arr)
    count = [0 for i in range(max_value + 1)]
    ans = [0 for _ in arr]
    for i in arr:
        count[i] += 1
    for i in range(1,max_value + 1):
        count[i] += count[i - 1]
    ret_count = count.copy()
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans, count


def main():
    arr = [random.randint(0, 480 - 2 * 5) for i in range(1000)]
    ans, count = count_sort(arr)
    print(ans)
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    if (a > b or a < 0 or b > len(count) -1):
        raise Exception("Invalid input")

    print(count[b] - count[a - 1])

    #create a file of 1000 random numbers
    f = open("array.txt", "w")
    for i in range(1000):
        f.write(str(random.randint(0, 480)) + "\n")




if __name__ == "__main__":
    main()

