from math import sqrt

start = int(input("Enter Start range: "))
end = int(input("Enter End range: "))


def check_sqrt(range_start=0, range_end=1):
    i = range_start if range_start > 4 else 4
    count = 0
    while i <= range_end:
        if sqrt(i).is_integer():
            count += 1
        i += 1
    return count


if __name__ == "__main__":
    print(check_sqrt(start, end))
