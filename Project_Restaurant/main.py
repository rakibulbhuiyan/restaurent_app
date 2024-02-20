from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from User import Chef, Customer, Server, Manager,User,Employee
from Order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta Pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 500, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    barger_1 = Burger('Chicken Burger', 600, 'small', ['chicken', 'onion'])
    menu.add_menu_item('barger', barger_1)
    barger_2 = Burger('Tomato Burger', 400, 'small', ['potato', 'tomato', 'oil'])
    menu.add_menu_item('barger', barger_2)
    barger_3 = Burger('meat Burger', 500, 'small', ['meat', 'oil'])
    menu.add_menu_item('barger', barger_3)
    menu.show_menu()

    print('Adding Customer:\n')
    customer_1 = Customer('Rocky', '012345', 'r@gmail.com', 'Dhaka', 200)
    selected_items = [barger_1]
    order=Order(customer_1,selected_items)
    print('Showing Order Details:')
    print(f'Customer Name: {order.customer.name}')
    print('Ordered Items:')
    for item in order.items:
        print(f'- {item.name}: {item.price} BDT')
    print(f'Total Bill: {order.bill} BDT')
    


if __name__ == '__main__':
    main()
