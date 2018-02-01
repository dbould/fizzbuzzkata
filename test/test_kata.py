from FizzBuzzKata import Kata


class TestKata:
    def test_answer(self):
        myKata = Kata()
        assert myKata.helloWorld() == "Hello World!"
