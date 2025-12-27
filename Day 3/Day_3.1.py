#odd or even 

class OddOREven:
    @staticmethod
    def even():
        number = int(input("Enter a number: "))
        if number % 2 == 0:
                print("Number is even ")

    @staticmethod
    def odd():
        number = int(input("Enter a number: "))
        if number % 2 != 0:
                print("Number is odd ")