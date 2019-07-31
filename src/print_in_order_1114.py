class Foo:
    def __init__(self):
        import threading
        self.sem1 = threading.Semaphore(0)
        self.sem2 = threading.Semaphore(0)     

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.sem1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.sem1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.sem2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.sem2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
