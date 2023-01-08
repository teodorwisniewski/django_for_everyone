

class Test:
    x: int = 0

    def __init__(self, name: str):
        self.name = name

    def party(self):
        Test.x += 1
        print(f"Hey {self.name}, x is equal to {Test.x}")


if __name__ == "__main__":

    t1 = Test("Teodor")
    t1.party()
    t1.party()
    t1.party()
    t1.party()

    t2 = Test("Mat")
    t2.party()