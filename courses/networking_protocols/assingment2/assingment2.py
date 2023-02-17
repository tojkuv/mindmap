import socket

class Assignment2:
    def __init__(self, year: int):
        self.year = year

    def tellAge(self, currentYear: int):
        print("Your age is", currentYear)

    def listAnniversaries(self):
        return_list = []

        num_of_anniversaries = ((2022 - self.year) / 10)

        i = 1
        while i <= num_of_anniversaries:
            return_list.append(i * 10)
            i += 1

        return return_list

    def modifyYear(self, n: int):

        first_two_characters = str(self.year)[:2] * n

        odd_characters = ''
        for i, c in enumerate(str(self.year)):
            if (i + 1) % 2 == 1:
                odd_characters += c

        return first_two_characters + odd_characters

    @staticmethod
    def checkGoodString(string: str):
        length = (len(string) >= 9)
        lower_case = string[0].islower()
        single_num = False

        nums_in_string = 0
        for c in string:
            if c.isdigit():
                nums_in_string += 1

        if nums_in_string == 1:
            single_num = True

        return length & lower_case & single_num

    @staticmethod
    def connectTcp(host: str, port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((host, port))
                return True
            except:
                return False


if __name__ == '__main__':
    a = Assignment2(2000)
    a.tellAge(1990)

    a = Assignment2(2000)
    ret = a.listAnniversaries()
    print(ret)

    a = Assignment2(1991)
    ret = a.listAnniversaries()
    print(ret)

    a = Assignment2(1782)
    ret = a.modifyYear(3)
    print(ret)

    ret = Assignment2.checkGoodString("f1obar0more")
    print(ret)

    ret = Assignment2.checkGoodString("foobar0more")
    print(ret)

    retval = Assignment2.connectTcp("www.google.com", 80)
    if retval:
        print("Connection established correctly")
    else:
        print("Some error")