class Kata:
    def run(self, test_case):
        if test_case <= 0:
            return "Bad input!"
        if test_case % 3 == 0:
            return "Fizz"
        if test_case % 5 == 0:
            return "Buzz"
        else:
            return test_case
