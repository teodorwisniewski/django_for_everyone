


# class Test:
#     """
#     ex:
#         t1 = Test("Teodor")
#         t1.party()
#         t1.party()
#         t1.party()
#         t1.party()
#
#         t2 = Test("Mat")
#         t2.party()
#
#     Output:
#         Hey Teodor, x is equal to 1
#         Hey Teodor, x is equal to 2
#         Hey Teodor, x is equal to 3
#         Hey Teodor, x is equal to 4
#         Hey Mat, x is equal to 5
#
#
#     """
#     x: int = 0
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def party(self):
#         Test.x += 1
#         print(f"Hey {self.name}, x is equal to {self.x}")


# class Test:
#     """
#     ex:
#         t1 = Test("Teodor")
#         t1.party()
#         t1.party()
#         t1.party()
#         t1.party()
#
#         t2 = Test("Mat")
#         t2.party()
#
#     Output:
#         Hey Teodor, x is equal to 0
#         Hey Teodor, x is equal to 0
#         Hey Teodor, x is equal to 0
#         Hey Teodor, x is equal to 0
#         Hey Mat, x is equal to 0
#     """
#     x: int = 0
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def party(self):
#         self.x += 1
#         print(f"Hey {self.name}, x is equal to {Test.x}")


class Test:
    x: int = 0

    def __init__(self, name: str):
        self.name = name

    def party(self):
        Test.x += 1
        print(f"Hey {self.name}, x is equal to {Test.x}")


class TestChild(Test):
    x: int = 0

    def __init__(self, name):
        self.name = name
        self.x = 0

    def party(self):
        Test.x += 5
        TestChild.x += 10
        self.x += 111

        print(f"Hey {self.name}, self.x is equal to {self.x}")
        print(f"Hey {self.name}, TestChild.x is equal to {TestChild.x}")
        print(f"Hey {self.name}, Test.x is equal to {Test.x}")


if __name__ == "__main__":

    t1 = Test("Teodor")
    t1.party()
    t1.party()
    t1.party()
    t1.party()

    t_child = TestChild("Child")
    t_child.party()

    t2 = Test("Mat")
    t2.party()
