class Kata:
    def run(self, test_case):
        if test_case <= 0:
            return "Bad input!"
        if test_case % 3 == 0:
            return "Fizz"
        else:
            return test_case
