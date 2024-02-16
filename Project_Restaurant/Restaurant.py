class Restaurant:
    def __init__(self,name,rent,menu=[]) -> None:
        # all restaurant details entry here
        self.name=-name
        self.orders=[]
        self.chef=None
        self.server=None
        self.manager=None
        self.rent=rent
        self.menu=menu
        self.revenue=0
        self.expense=0
        self.profit=0
        self.balance=0
        # employee add ...here server,manager,chef all are employee
    def add_employee(self,employee_type,employee):
        if employee_type=='chef':
            self.chef=employee
        elif employee_type=='server':
            self.server=employee
        elif employee_type=='manager':
            self.manager=employee
        else:
            print('Invalid employee_type')
    # add order 
    def add_order(self,order):
        self.orders.append(order)

    def paysalary(self,order,customer,amount):
        if amount> order.bill:
            self.revenue +=order.bill
            self.balance +=order.bill
            customer.due_amount=0
            return amount-order.bill
        else:
            print('Not enough money . Pay more...')
            
