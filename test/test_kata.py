from FizzBuzzKata import Kata


class TestKata:

    def test_three_prints_fizz(self):
        my_kata = Kata()
        assert my_kata.run(3) == "Fizz"

    def test_six_prints_fizz(self):
        my_kata = Kata()
        assert my_kata.run(6) == "Fizz"

    def test_number_gets_returned(self):
        my_kata = Kata()
        assert my_kata.run(4) == 4

    def test_zero_bad_input(self):
        my_kata = Kata()
        assert my_kata.run(0) == "Bad input!"

    def test_minus_5_bad_input(self):
        my_kata = Kata()
        assert my_kata.run(-5) == "Bad input!"

    def test_5_prints_buzz(self):
        my_kata = Kata()
        assert my_kata.run(5) == "Buzz"

    def test_10_prints_buzz(self):
        my_kata = Kata()
        assert my_kata.run(5) == "Buzz"

    def test_15_prints_fizzbuzz(self):
        my_kata = Kata()
        assert my_kata.run(15) == "FizzBuzz"

    def test_30_prints_fizzbuzz(self):
        my_kata = Kata()
        assert my_kata.run(30) == "FizzBuzz"
