
TICKET_DICTIONARY = {"Sencillo": 2.40, "Casual": 11.35, "Usual": 40.00, "Familiar": 10.00, "Jóven": 80.00}
TICKET_SELECTION_LIST = ["Sencillo", "Casual", "Usual", "Familiar", "Jóven"]
ZONE = ["1 zona", "2 zonas", "3 zonas", "4 zonas", "5 zonas", "6 zonas"]
SECRET_CODE = 4321

def ticket_selection():
    print("//////////////////////////////////////////"
          "\n¿Qué billete desea adquirir?"
          "\n1. Billete sencillo"
          "\n2. Billete Casual"
          "\n3. Billete Usual"
          "\n4. Billete Familiar"
          "\n5. Billete Jóven"
          "\n//////////////////////////////////////////")
    valid_ticket = False
    while not valid_ticket:
        try:
            ticket_value = int(input("Introduce el número de la opción deseada: "))
            if ticket_value in range(1, 6):
                valid_ticket = True
            elif ticket_value == SECRET_CODE:
                secret_code()
            else:
                print("Error: Por favor, introduce una opción válida.")                
        except ValueError:
            print("Error: Por favor, introduce una opción válida.")
    return ticket_value

def zone_selection():
    valid_zone = False
    print("//////////////////////////////////////////"
          "\n¿Cúantas zonas desea?"
          "\n1. 1 zona"
          "\n2. 2 zonas"
          "\n3. 3 zonas"
          "\n4. 4 zonas"
          "\n5. 5 zonas"
          "\n6. 6 zonas"
          "\n//////////////////////////////////////////")
    while not valid_zone:
        try:
            zone_value = int(input("Introduce la zona deseada: "))
            if zone_value in range(1, 7):
                valid_zone = True
            elif zone_value == SECRET_CODE:
                secret_code()
            else:
                print("Error: Por favor, introduce una opción válida.")
        except ValueError:
            print("Error: Por favor, introduce una opción válida.")
    return zone_value

def ticket_completion(ticket_value, zone_value):
    zone_increment = 1.25
    base_price = TICKET_DICTIONARY[TICKET_SELECTION_LIST[ticket_value-1]]
    final_price = base_price
    for i in range(1, zone_value):
        final_price *= zone_increment
    print(f"El precio de su billete {TICKET_SELECTION_LIST[ticket_value-1]} con {ZONE[zone_value-1]} es de {final_price:.2f}€.")
    return final_price

def process_tickets():
    MAX_TICKETS = 3
    tickets = 0
    more_tickets = True
    total_price = 0.0
    ticket_list = []
    while more_tickets:
        ticket_value = ticket_selection()
        zone_value = zone_selection()
        price_to_pay = ticket_completion(ticket_value, zone_value)
        total_price += price_to_pay
        tickets += 1
        ticket_list.append((TICKET_SELECTION_LIST[ticket_value-1], ZONE[zone_value-1], price_to_pay))
        if tickets >= MAX_TICKETS:
            print("Ha alcanzado el número máximo de billetes.")
            more_tickets = False
        else:
            more_tickets = ask_more_tickets()
    return ticket_list, total_price

def ask_more_tickets():
    valid_input = False
    while not valid_input:
        more_tickets_input = input("¿Desea adquirir más billetes? (s/n): ").lower()
        if more_tickets_input == "s":
            return True
        elif more_tickets_input == "n":
            return False
        elif more_tickets_input == str(SECRET_CODE):
            secret_code()
        else:
            print("Error: Por favor, introduce una opción válida.")

def payment(price_to_pay):
    valid_coins = [0.05, 0.10, 0.20, 0.50, 1, 2]
    valid_bills = [5, 10, 20, 50]
    try:
        while price_to_pay > 0:
            amount = float(input("Introduce una moneda/billete: "))
            if amount in valid_coins or amount in valid_bills:
                price_to_pay -= amount
                price_to_pay = round(price_to_pay, 2)
                if price_to_pay < 0:
                    print("Cambio:", price_to_pay*-1, "€")
                    print("/////////////////////")
                elif price_to_pay > 0:
                    print("Importe restante: ", price_to_pay, "€")
                    print("/////////////////////")
                elif price_to_pay == 0:
                    print("/////////////////////")
                
            else:
                print("Error: Por favor, introduzca una moneda/billete real.")
            if amount == SECRET_CODE:
                secret_code()
    except ValueError:
        print("Error: Por favor, introduzca una moneda/billete real.")

def print_ticket_list(ticket_list):
    valid_input = False
    while not valid_input:
       print_ticket_input = input("¿Desea imprimir el recibo de la compra? (s/n): ").lower()
       match print_ticket_input:
            case "s":
                valid_input = True
                print("//////////////////////////////////////////"
                    "\nBilletes adquiridos:"
                    "\n//////////////////////////////////////////")
                for ticket in ticket_list:
                    print(f"Billete: {ticket[0]} | Zona: {ticket[1]} | Precio: {ticket[2]:.2f}€")
                print("Gracias por su compra.")
            case "n":
                valid_input = True
                print("Gracias por su compra.")
            case str(SECRET_CODE):
                secret_code()
            case _:
                print("Error: Por favor, introduce una opción válida.")
                valid_input = False

def secret_code():
    print("Codigo de apagado activado, la máquina procede a apagarse")
    exit()
                               
def subway_machine(): 
    while True:
        ticket_list, total_price = process_tickets()
        print(f"El precio total de los billetes adquiridos es de {total_price:.2f}€.")
        payment(total_price)
        print_ticket_list(ticket_list)


subway_machine()