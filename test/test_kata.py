from FizzBuzzKata import Kata


class TestDataGetsReturned:
    def test_answer(self):
        myKata = Kata()
        assert myKata.run(3) == "Fizz"
