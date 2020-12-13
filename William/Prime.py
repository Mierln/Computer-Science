
def check_prime(cur_num, cur_list):
    checker = 0
    for cur_index in cur_list:
        if cur_num % cur_index == 0:
            checker += 1

    if checker > 0:
        return True
    else:
        return False


def prime_creator(length):
    cur_list = [2, 3]

    if length == 1:
        cur_list = [2]
    elif length == 2:
        cur_list = [2, 3]
    else:
        num = cur_list[-1] + 2
        while len(cur_list) < length:
            if check_prime(num, cur_list) == False:
                cur_list.append(num)
            else:
                num += 2

    return cur_list

def main():
    length = int(input("Limit: "))
    print(prime_creator(length))

main()