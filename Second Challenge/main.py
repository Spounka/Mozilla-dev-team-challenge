number = int(input("Enter the desired number: "))


def loop(num=100):
    i = 0
    result = 0
    while i < num:
        result += len(str(i))
        i += 1
    return result


if __name__ == "__main__":
    print(loop(number))
