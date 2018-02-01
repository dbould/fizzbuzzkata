from FizzBuzzKata import Kata


class Test3ReturnsFizz:
    def test_answer(self):
        myKata = Kata()
        assert myKata.run(3) == "Fizz"
