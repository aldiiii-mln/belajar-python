class RegularMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = 0

    def borrow_book(self):
        if self.borrowed_books >= 3:
            print("You hit your limit for borrowing a book")
        else :
            self.borrowed_books += 1
    
    def return_book(self):
        if self.borrowed_books > 0:
            self.borrowed_books -= 1
        else :
            print("You cant return book because you have 0 borrowing books")
    def display(self):
        print(f"{self.name}, You have {self.borrowed_books} books you already borrowed")

class PremiumMember(RegularMember):
    def __init__(self, name, membership_tier):
        super().__init__(name)
        self.membership_tier = membership_tier
    
    def borrow_book(self):
        if self.borrowed_books >= 5:
            print("You hit your limit for borrowing a book")
        else :
            self.borrowed_books += 1
    
    def get_privileges(self):
        print(f"Premium member {self.name} has {self.membership_tier} privileges")


member1 = RegularMember("Aldi")
member2 = PremiumMember("Ilham", "Gold")
member3 = PremiumMember("Rizal", "Platinum")
member4 = PremiumMember(member1.name, "Gold")

members = [member1, member2, member3, member4]
for member in members:
    member.borrow_book()
    member.display()

member1.return_book()
member1.display()

member2.get_privileges()
member3.get_privileges()
