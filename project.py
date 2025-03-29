print("\n=======================================================")
def register_page():
    try:
        with open('staff_details.txt', 'a') as file:
            role = input("Enter the Role (admin/manager/chef/customer): ").lower()
            name = input("Enter the user name: ")
            first = input("Enter the first name: ")
            last = input("Enter the last name: ")
            email = input("Enter the Email: ")
            password = input("Enter the password: ")
            phone = input("Enter the phone number: ")
            file.write(f"role:{role},user name:{name},first_name:{first},last_name:{last},email:{email},password:{password},phone:{phone}\n")
            print("==========Registration successful!==========")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
       
print("\n ========== Welcome to Ahad Restaurants page. ==========")
menu = {
    1: {"item": "Samosa Tarkari", "price": 89.99},
    2: {"item": "Samosa chart", "price": 149.99},
    3: {"item": "Namkin chart", "price": 149.99},
    4: {"item": "Mixed chart", "price": 169.99},
    5: {"item": "vej-chaumin", "price": 99.99},
    6: {"item": "vej-roll", "price": 24.99},
    7: {"item": "vej-mommo", "price": 99.99},
    8: {"item": "buff-momo", "price": 169.99},
    9: {"item": "vej-shoop", "price": 59.99},
    10: {"item": "Aalu Naan", "price": 44.99},
    11: {"item": "Butter Naan", "price": 34.99},
    12: {"item": "Matar paneer", "price": 99.99},
    13: {"item": "Chicken curry", "price": 299.99}
}

def page():
    while True:
        print("1. Register.")
        print("2. login.")
        print("0. Exit.")
        print("\n========================================================")
        choice = int(input("Choose the Option: "))
        if choice == 1:
            register_page()
        elif choice == 2:
            login_page()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid number! Please try again.")
    else:
        print("Invalid! Please try again.")

def display_menu():
    print("\nCurrent Food Menu:")
    for item_id, details in menu.items():
        print(f"{item_id}. {details['item']}: ${details['price']:.2f}")

def login_page():
    print("\n====================================================")
    print("========== welcome to login page ===========")
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        username_or_email = input("Enter your username or email: ").strip().lower()
        password = input("Enter your password: ")
        try:
            with open('staff_details.txt', 'r') as file:
                users = file.readlines()
            for user in users:
                user = user.strip()
                if not user:
                    continue
                try:
                    user_details = dict(item.split(":") for item in user.split(",") if ":" in item)
                except ValueError as e:
                    print(f"{e}.")
                    continue
                if (user_details.get('user name','').lower() == username_or_email or user_details.get('email','').lower() == username_or_email) and user_details.get('password') == password:
                    print("Login successful!")
                    redirect_to_role(user_details.get('role'),user_details)
                    return
            attempts += 1
            print(f"Incorrect! You have {max_attempts - attempts} attempts left.")
        except Exception as e:
            print(f"{e}.")
            return
    print("Your account will be blocked!")

def redirect_to_role(role,user_details):
    while True:
        if role == 'admin':
            admin_profile(user_details)
        elif role == 'manager':
            manager_profile(user_details)
        elif role == 'chef':
            chef_profile(user_details)
        elif role == 'customer':
            customer_profile(user_details)
        else:
            print("Unknown role. Access denied.")
            break
        choice = input("Do you want to return to the main page? (yes/no): ").strip().lower()
        if choice == 'yes':
            break

def update_user_details(user_details):
    print("\nCurrent User Details:")
    for key, value in user_details.items():
        print(f"{key}: {value}")
    
    update_choice = input("Do you want to update your details? (yes/no): ").strip().lower()
    if update_choice == 'yes':
        for key in user_details.keys():
            new_value = input(f"Enter new {key}: ")
            if new_value:
                user_details[key] = new_value
        update_user_file(user_details)

def update_user_file(updated_details):
    try:
        with open('staff_details.txt', 'r') as file:
            users = file.readlines()
        updated = False
        with open('staff_details.txt', 'w') as file:
            for user in users:
                user = user.strip()
                if not user:
                    continue
                user_data = dict(item.split(":") for item in user.split(",") if ":" in item)
                if user_data.get('email') == updated_details.get('email') or user_data.get('name') == updated_details.get('name'):
                    user_data.update(updated_details)
                    updated = True
                file.write(','.join(f"{key}:{value}" for key, value in user_data.items()) + '\n')
        if updated:
            print("User details updated successfully!")
        else:
            print("No matching user found for update.")
    except Exception as e:
        print(f"Error updating user details: {e}")


def manager_profile(user_details):
    while True:
        print("\n========== welcome to Manager profile ==========")
        print("1. Manage Menu.")
        print("2. View Ingredients.")
        print("3. Update Profile.")
        print("4. Sends Sales Reports.")
        print("0. Log out.")
        print("===============================")
        try:
            choice = int(input("Choose an option: "))
            if choice == 0:
                print("Successfully logged out.")
                return login_page()
            elif choice == 1:
                manage_menu()
            elif choice == 2:
                view_ingredients()
            elif choice == 3:
                update_user_details(user_details)
            elif choice == 4:
                sends_sales_reports()
            else:
                print("Invalid option! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def view_ingredients():
    print("\nCurrent Ingredients:")
    try:
        with open("request_ingredients.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("The file 'request_ingredients.txt' does not exist yet.")

def sends_sales_reports():
    print("\nPlease send the reports to admin.")
    try:
        with open('order.txt', 'r') as f:
            orders = f.readlines()
        if orders:
            print("".join(orders))  
        else:
            print("No orders found.")
    except FileNotFoundError:
        print("File does not exist.")
    n = int(input("Enter the number of sales: "))
    for i in range(n):
        order_item = input("Enter the name of items: ")
        order_price = float(input("Enter the price: "))
        order_quantity = int(input("Enter the number of quantity: "))
        total = order_price * order_quantity
        with open("sends_sales_reports.txt", "a") as file:
            file.write(f"{order_item},{total}\n")

def manage_menu():
    while True:
        print("\n========== Manage Menu ==========")
        print("1. Add Food Item.")
        print("2. Edit Food Item.")
        print("3. Remove Food Item.")
        print("4. Edit Food Price.")
        print("0. Go to Profile.")
        print("\n==================================")
        try:
            choice = int(input("Choose an option: "))
            if choice == 0:
                print("Exiting from menu.")
                return
            elif choice == 1:
                add_food_item()
            elif choice == 2:
                edit_food_item()
            elif choice == 3:
                remove_food_item()
            elif choice == 4:
                edit_foods_price()
            else:
                print("Invalid option! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def add_food_item():
    item_name = input("Enter the name of the food item: ")
    item_price = float(input("Enter the price of the food item: "))
    new_id = max(menu.keys()) + 1
    menu[new_id] = {"item": item_name, "price": item_price}
    print(f"Added {item_name} with price ${item_price:.2f}.")

def edit_food_item():
    display_menu()
    try:
        item_id = int(input("Enter the item number to edit: "))
        if item_id not in menu:
            print("Invalid item number! Please try again.")
            return
        new_name = input("Enter the new name of the food item: ")
        new_price = float(input("Enter the new price of the food item: "))
        menu[item_id] = {"item": new_name, "price": new_price}
        print(f"Updated item {item_id} to {new_name} with price ${new_price:.2f}.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def remove_food_item():
    display_menu()
    try:
        item_id = int(input("Enter the item number to remove: "))
        if item_id in menu:
            removed_item = menu.pop(item_id)
            print(f"Removed {removed_item['item']} from the menu.")
        else:
            print("Invalid item number! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def edit_foods_price():
    display_menu()
    try:
        item_id = int(input("Enter the item number to edit price: "))
        if item_id not in menu:
            print("Invalid item number! Please try again.")
            return
        new_price = float(input("Enter the new price of the food item: "))
        original_name = menu[item_id]['item']
        menu[item_id] = {"item": original_name, "price": new_price}
        print(f"Updated item price {item_id} to ${new_price:.2f}.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def customer_profile(user_details):
    while True:
        print("\n========== Welcom to Customer Profile ==========")
        print("1. Update Profile.")
        print("2. View Items.")
        print("3. Take Order.")
        print("4. Send Feedback.")
        print("0. Logout.")
        print("====================================================")
        try:
            choose = int(input("Choose the Option: "))
            if choose == 0:
                print("Successfully! Logout.")
                return login_page()
            elif choose == 1:
                update_user_details(user_details)
            elif choose == 2:
                display_menu()
            elif choose == 3:
                take_order()
            elif choose == 4:
                send_feedback()
            else:
                print("Invalid Option! Please try again.")
        except ValueError:
            print("Invalid Input! Please enter a number.")

def take_order():
    order = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter item number (0 to finish): "))
            if choice == 0:
                break
            if choice not in menu:
                print("Invalid item number! Please try again.")
                continue
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be at least 1!")
                continue
            item = menu[choice]
            order.append({
                "name": item["item"],
                "price": item["price"],
                "quantity": quantity
            })
            print(f"Added {quantity} x {item['item']} to your order.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    if order:
        print("\nYour Order Summary:")
        total = 0
        for item in order:
            item_total = item["price"] * item["quantity"]
            total += item_total
            print(f"{item['quantity']} x {item['name']} @ ${item['price']:.2f} = ${item_total:.2f}")
        print(f"Total: ${total:.2f}")
        order_summary = f"Order: {order}, Total: ${quantity:.2f}"
        with open('order.txt', 'a') as file:
            file.write(f"{order_summary}\n")
        process_payment(total)
    else:
        print("No items ordered.")

def process_payment(total):
    while True:
        payment_method = input("\nChoose payment method (cash/card): ").strip().lower()
        if payment_method == "cash":
            cash = float(input("Enter cash amount: "))
            if cash >= total:
                change = cash - total
                print(f"Payment successful! Your change is: ${change:.2f}")
                break
            else:
                print("Insufficient cash! Please enter a valid amount.")
        elif payment_method == "card":
            print(f"Payment successful! Thank you for your order.$")
            break
        else:
            print("Invalid payment method! Please choose 'cash' or 'card'.")
        send_feedback()
def send_feedback():
    feedback = input("Please says something about our services: ")
    print("Thanks for your feedback!")
    with open('feedback.txt','a') as file:
        file.write(f"{feedback} \n")
   
def admin_profile(user_details):
    while True:
        print("\n=========== Welcome to Admin Profile ===============")
        print("1. Manage Staff.")
        print("2. View sales Reports.")
        print("3. View Feedback.")
        print("4. Update Profile.")
        print("0. Logout.")
        print("======================================================")
        try:
            choice = int(input("Choose the Option: "))
            if choice == 0:
                print("Successfully Logout!")
                return login_page()
            elif choice == 1:
                manage_staff(user_details)
            elif choice == 2:
                def view_sales_reports():
                    try:
                        with open("sends_sales_reports","r") as file:
                            for line in file:
                                print(line.split())
                    except FileNotFoundError:
                        print("files not founds! in send_sales_reports.txt file.")
                    view_sales_reports()
            elif choice == 3:
                view_feedback()
            elif choice == 4:
                update_user_details(user_details)
            else:
                print("Invalid number! Please try again.")
        except ValueError:
            print("Invalid Input! Please try again.")
def view_feedback(): 
    try:
        with open('feedback.txt', 'r') as f:
            feedback = f.readlines()
            feedback = [line.strip().lower() for line in feedback]
            if feedback:
                print("\n".join(feedback))  
            else:
                print("No feedback found.")
    except FileNotFoundError:
        print("File does not exist.")

def manage_staff(user_details):
    print("\n========== managing the staff============")
    while True:
        print("1. Update Staff.")
        print("2. remove the staff.")
        print("0. GO Back to admin page.")
        print("=======================================")
        try:
            choose = int(input("Choose the Option: "))
            if choose == 0:
                return admin_profile(user_details)
            elif choose == 1:
                update_staff(user_details)
            elif choose == 2:
                remove_staff(user_details)
            else:
                print("Invalid Number! Please try again.")
        except ValueError:
            print("Invalid Input! please try again.")

def remove_staff(user_details):
    while True:
        print("1. Remove by Username.")
        print("2. Remove by email.")
        print("0. Returnback.")
        try:
            choose = int(input("Choose the Option: "))
            if choose == 0:
                return manage_staff(user_details)
            elif choose == 1:
                username_to_remove = input("Enter the username to remove: ").strip()
                remove_from_file('staff_details.txt', 'name', username_to_remove)
                print(f"User  with username '{username_to_remove}' removed successfully.")
            elif choose == 2:
                email_to_remove = input("Enter the email to remove: ").strip()
                remove_from_file('staff_details.txt', 'email', email_to_remove)
                print(f"User  with email '{email_to_remove}' removed successfully.")
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid Input! please try again.")
        except Exception as e:
            print(f"{e}. Please try again.")

def remove_from_file(filename, field, value_to_remove):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            for line in lines:
                details = dict(item.split(':') for item in line.strip().split(','))
                if details.get(field) != value_to_remove:
                    file.write(line)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while removing: {e}")

def update_staff(user_detais):
    while True:
        print("1. Add Staff.")
        print("2. update Staff Name.")
        print("3. Update Staff Email.")
        print("0. Go Back to manage Staff.")
        try:
            choose = int(input("Choose the Options: "))
            if choose == 0:
                return manage_staff(user_detais)
            elif choose == 2:
                update_staff_name()
            elif choose == 3:
                update_staff_email()
            elif choose == 1:
                add_staff()
            else:
                print("Invalid number! Please try again.")
        except ValueError:
            print("Invalid Input! Please try again.")

def update_staff_email():
    try:
        choose = input("Choose the role (manager/chef): ").strip().lower() 
        if choose == 'manager':
            update_email = input("Enter the new email for the manager: ").strip()
            with open('store_email.txt', 'a') as file:
                file.write(f"{update_email}\n")
            print("Successfully updated manager email.")
        elif choose == 'chef':
            update_email = input("Enter the new email for the chef: ").strip()
            with open('store_email.txt', 'a') as file:
                file.write(f"{update_email}\n")
            print("Successfully updated chef email.")
        else:
            print("Invalid choice! Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

def update_staff_name():
    try:
        choose = input("Choose the Staff (manager/chef): ").strip().lower()
        if choose == 'manager':
            change = input("Enter the new name for the manager: ").strip()
            with open('updated_name.txt', 'a') as file:
                file.write(f"{change}\n")
            print("Manager name updated successfully.")
        elif choose == 'chef':
            change = input("Enter the new name for the chef: ").strip()
            with open('updated_name.txt', 'a') as file:
                file.write(f"{change}\n")
            print("Chef name updated successfully.")
        else:
            print("Invalid choice! Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

def add_staff():
    try:
        choose = input("Choose the role (manager/staff): ").strip().lower()
        first_name = input("Input Staff First Name: ").strip()
        last_name = input("Input Staff Last Name: ").strip()
        email = input("Input Staff Email: ").strip()
        phone_number = input("Enter the Phone Number: ").strip()
        if choose == 'manager':
            with open('staff_details.txt', 'a') as f:
                f.write(f"{first_name} {last_name}, {email}, {phone_number}, Manager\n")
            print("Manager details added successfully.")
        elif choose == 'staff':
            with open('staff_details.txt', 'a') as f:
                f.write(f"{first_name} {last_name}, {email}, {phone_number}, Staff\n")
            print("Staff details added successfully.")
        else:
            print("Invalid choice! Please choose 'manager' or 'staff'.")
    except Exception as e:
        print(f"{e}. Please try again.")

orders = []
def chef_profile(user_details):
    while True:
        print("\n========== Chef Profile ==========")
        print("1. View Orders.")
        print("2. Update Order(in progress/completed).")
        print("3. Request Ingredients.")
        print("4. Update Profile.")
        print("0. Logout.")
        print("====================================")
        try:
            choose = int(input("Choose the Option: "))
            if choose == 0:
                print("Successfully! logout.")
                return login_page()
            elif choose == 1:
                print("\n==========Customer Orders==========")
                try:
                    with open('order.txt', 'r') as f:
                        orders = f.readlines()
                    if orders:
                        print("".join(orders))  
                    else:
                        print("No orders found.")
                except FileNotFoundError:
                        print("File does not exist.")    
            elif choose == 2:
                update_orders(user_details)
            elif choose == 3:
                def request_ingredients():
                    with open("request_ingredients.txt", "a") as file:
                        try:
                            a = int(input("Enter the number of ingredients you want: "))
                            for i in range(a):
                                items = input("Enter the name of the item: ")
                                amount = int(input("Enter the quantity: "))
                                file.write(f"{items},{amount}\n")
                                print("Successfully sent the ingredient request to the manager.")
                        except ValueError:
                            print("Please enter a valid number.")
                request_ingredients()   
            elif choose == 4:
                update_user_details(user_details)
            else:
                print("Invalid Option! Please try again.")
        except ValueError:
            print("Invalid Input! Please enter a number.")

def update_orders(user_details):
    while True:
        print("\n========== Orders Status =========")
        print("1. Order in Progress.")
        print("2. Order Complete.")
        print("0. Exit form it.")
        try:
            choose = int(input("Choose the Option: "))
            if choose == 1:
                print("orders in progress! Please wait.")
            elif choose == 2:
                print("Orders complete! enjoy your food.")
            elif choose == 0:
                return chef_profile(user_details)
            else:
                print("Invalid number! Please try again.")
        except ValueError:
            print("Invalid Input! Please try again.")

if __name__ == "__main__":
    page()