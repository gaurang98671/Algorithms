def stringHash(str):
    p = 31
    m = 1e9 + 9
    power_of_p = 1
    hash_val = 0

    for i in range(len(str)):
        hash_val = (hash_val + (ord(str[i]) - ord('a') + 1) * power_of_p) % m
        power_of_p = (power_of_p * p) % m

    return int(hash_val)


if __name__ == '__main__':

    print(stringHash("gaurang"))

