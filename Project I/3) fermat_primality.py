from binary_power import binary_power, to_binary_string
import random


def fermat_primality_test(n, k):
    i = 0
    while i < k:
        x = random.randint(1, n - 1)

        if binary_power(x, n - 1, n) == 1:
            i = i + 1
        else:
            return False

    return True


if __name__ == "__main__":
    n = 8325309815617127188841245664781357105867834920235859605968021007230490768949794774780695105749995077037867116397476933522364031417216726144469958416272234308484325432605954611352064393886432939476526281490883245796380041696692609679876881393060625556849668327763565568396520797741075356631794339983077

    #n = int(input("n = "))
    #k = int(input("k = "))
    print(fermat_primality_test(n, k))
