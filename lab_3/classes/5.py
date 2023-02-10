class Account():
    
    owner = ""
    balance = 0

    def __init__(p, owner, balance):
        p.owner = owner 
        p.balance = balance

    def __str__(p):
        return f"owner of an account is: {p.owner}\naccount balance is: {p.balance}"
    
    def deposit(p, amount):
        p.balance += amount
        return "deposit"

    def withdraw(p, amount):
        if(amount <= p.balance):
            p.balance -= amount
            return "withdraw accepted"
        else:
            return "withdraw can not be accepted"

person = Account("diana", 123456)
print(person)

print(person.deposit(50))
print(person.withdraw(20))
print(person.balance)
