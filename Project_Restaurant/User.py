from abc import ABC ,abstractmethod
# abstruct method 
class User(ABC):
    def __init__(self,name,mobile,email,address) -> None:
        self.name=name
        self.mobiel=mobile
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, mobile, email, address,money) -> None:
        self.wallet=money
        self.__order=None
        self.due_amount=0
        super().__init__(name, mobile, email, address)

    @property
    def order(self):
        return self.__order
    @order.setter
    def order(self,order):
        self.__order=order

    def place_order(self,order):
        self.order=order
        self.bill_due +=order.bill
        print(f'{self.name} place an order with bill {order.bill}')
    
    def eat_food(self,order):
        print(f'{self.name} item food {order.item}')


    def pay_for_order(self, amount):
        # TODO: submit the money to the manager
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, mobile, email, address,salary,starting_data,department) -> None:
        self.salary=salary
        self.due=salary
        self.starting_data=starting_data
        self.department=department
        super().__init__(name, mobile, email, address)
    def received_salary(self):
        self.due=0



class Chef(Customer):
    def __init__(self, name, mobile, email, address, salary, starting_data, department,cooking_item) -> None:
        self.cooking_item=cooking_item
        super().__init__(name, mobile, email, address, salary, starting_data, department)

class Server(Customer):
    def __init__(self, name, mobile, email, address, salary, starting_data, department) -> None:
        self.tips_earn=0
        super().__init__(name, mobile, email, address, salary, starting_data, department)

    def taken_order(self,order):
        pass

    def transfer_order(self,order):
        pass

    def transfer_order(self,order):
        pass

    def receive_tips(self, amount):
        self.tips_earn +=amount
class Manager(Customer):
    def __init__(self, name, mobile, email, address, salary, starting_data, department) -> None:
        super().__init__(name, mobile, email, address, salary, starting_data, department)