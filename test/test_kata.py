from FizzBuzzKata import Kata


class TestKata:
    def test_data_gets_returned(self):
        my_kata = Kata()
        assert my_kata.run(3) == "Fizz"
