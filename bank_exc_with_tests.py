from datetime import datetime

bank_accounts = {
1001: {
"first_name": "Alice",
"last_name": "Smith",
"id_number": "123456789",
"balance": -2500.50,
"transactions_to_execute": [
("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
"transaction_history": [
("2024-08-25 09:00:00", 1001, 1002, 500), ("2024-08-15 09:30:00", 1001, 1200, 1200)]},
1002:{
"first_name": "Dayana",
"last_name": "Hersko",
"id_number": "12349865",
"balance": 12500.50,
"transactions_to_execute": [
("2024-08-17 14:00:00", 1002, 1001, 600), ("2024-08-22 15:00:00", 1002, 1003, 200)],
"transaction_history": [
("2024-08-21 09:00:00", 1002, 1001, 700), ("2024-08-25 09:30:00", 500, 700, 1200)]},
1003:{
"first_name": "Dany",
"last_name": "Levy",
"id_number": "12565665",
"balance": 3000.50,
"transactions_to_execute": [
("2024-08-17 09:00:00", 1003, 1001, 600), ("2024-08-22 15:00:00", 1003, 1002, 1200)],
"transaction_history": [
("2024-08-21 09:00:00", 1002, 1001, 700), ("2024-08-22 09:30:00", 1003, 1002, 500)]},
1004:{
"first_name": "Dany",
"last_name": "Levkovitz",
"id_number": "18877665",
"balance": 8000,
"transactions_to_execute": [
("2024-08-17 09:00:00", 1004, 1001, 600), ("2024-08-22 15:00:00", 1004, 1001, 1200)],
"transaction_history": [
("2024-08-21 09:00:00", 1004, 1003, 700), ("2024-08-22 09:30:00", 1004, 1002, 500)]},
1005:{
"first_name": "Dayanad",
"last_name": "Liver",
"id_number": "18877665",
"balance": 10000,
"transactions_to_execute": [
("2024-08-17 09:00:00", 1004, 1001, 600), ("2024-08-22 15:00:00", 1004, 1001, 1200)],
"transaction_history": [
("2024-08-21 09:00:00", 1004, 1003, 700), ("2024-08-22 09:30:00", 1004, 1002, 500)]}
}
success: bool = False
def display_menu():
    print("1. transfer money to another account")
    print("2. perform all waiting transactions")
    print("3. reports")
    print("4 - exit the program")

def display_menu_reports():
    print("1. report of all accounts in the bank")
    print("2. report details of an account by account number")
    print("3. report details of an account by ID number")
    print("4. report details of an account by first name")
    print("5. report of all account sorted by balance, ascending")
    print("6. report of all transactions sorted by date, ascending")
    print("7. report of all transactions from today")
    print("8. report of all account in debit")
    print("9. report of the total balance of all accounts")
    print("10. return to main menu")
def get_menu_choice() -> str:
    while True:
        try:
            choice = input("Enter your choice (1-4): ")
            return choice
        except Exception as e:
            print("please try again, your choice is illegal + str(e)")
            continue

def get_menu_choose() -> str:
    while True:
        try:
            choose = input("Enter your choice (1-10): ")
            return choose
        except Exception as e:
           print("please try again, your choice is illegal + str(e)")
           continue

def check_choice(choice:str)-> bool:
    returnID:bool = False
    if choice.isalpha():
        raise ValueError("you entered an alpha string, try again")
    if int(choice) in range(1, 5):
        return True
    else:
        raise ValueError("Invalid choice, please select a number between 1 and 4")



def check_choose(choose:str)-> bool:
    returnID: bool = False
    if choose.isalpha():
        raise ValueError("you entered an alpha string, try again")
    if int(choose) in range(1, 11):
        return True
    else:
        raise ValueError("Invalid choice, please select a number between 1 and 10")

def handle_menu(choice:any, choose:any) -> bool:
    global bank_accounts
    det_list:list[any] = []
    if choice:
        match choice:
            case 1:
                while True:
                    det_list = get_accs_for_transac()
                    if not det_list:
                        continue
                    try:
                        if check_acc_for_transac(det_list):
                            fromacc, toacc, amm = det_list
                            if transac(int(fromacc), int(toacc), int(amm)):
                                print("the transaction was added to waiting transactions")
                                break
                            else:
                                print("something went wrong, please try again")
                                continue
                        else:
                            print("something went wrong, try again")
                            continue
                    except Exception as e:
                        print("some detail was illegal please try again" + str(e))
                        continue
            case 2:
                mess_from = {key: value["transactions_to_execute"] for key, value in bank_accounts.items()}
                #print(mess_from)

                if all_transac():
                   print("all transactions were processed")
                else:
                    print("something went wrong, try again")
                    return False

            case _:
                return False

    if choose:
        match choose:
            case 1:
               if report1():
                   print("the report was processed")
                   return True
               else:
                   return False
            case 2:
                while True:
                    try:
                        accnumber = get_acc_number()
                        if check_acc_number(accnumber):
                             if report2(accnumber):
                                print("the report was processed")
                                return True
                        else:
                             return False
                    except Exception as e:
                        print("something went wrong, try again " + str(e))
            case 3:
                idnumber:str
                while True:
                    try:
                        idnumber = get_idnumber()
                        if check_idnumber(idnumber):
                            if report3(idnumber):
                                print("the report was processed")
                                return True
                        else:
                            continue
                    except Exception as e:
                        print("something went wrong, try again " + str(e))
                        continue
            case 4:
                while True:
                    firstName = get_first_name()
                    try:
                        if check_first_name(firstName):
                            if report4(firstName):
                                print("the report was processed")
                                return True
                            else:
                                return False
                    except Exception as e:
                        print("something went wrong, please try again " + str(e))
                        return False
            case 5:
                if report5():
                    print("the report was processed")
                    return True
                else:
                    return False
            case 6:
                if report6():
                    print("the report was processed")
                    return True
                else:
                    return False
            case 7:
                if report7():
                    print("the report was processed")
                    return True
                else:
                    return False
            case 8:
                if report8():
                    print("the report was processed")
                    return True
                else:
                    return False
            case 9:
                if report9():
                    print("the report was processed")
                    return True
                else:
                    return False
            case _:
                return False


def check_det_list(det_list:list[any]) -> bool:
    fromacc, toacc, amm = det_list
    if fromacc not in bank_accounts.keys() or toacc not in bank_accounts.keys():
        raise ValueError("one of the accounts is not known")
    else:
        if str(amm).isalpha():
            raise ValueError("you typed an alpha amount, please try again")

        else:
            return True


def get_acc_number() -> int:
    accnumber:int = 0
    accnumber = int(input("please type an account number"))
    return accnumber

def check_acc_number(accnumber:int) -> bool:
    global bank_accounts
    if str(accnumber).isalpha():
        raise ValueError("not an integer")
    if accnumber not in bank_accounts.keys():
        raise ValueError("the account you typed does not exist, try again")
    return True

def get_accs_for_transac() -> list[any]:
        fromacc:str =input("please type the account from which to transfer the money")
        toacc:str = input("please type the account to transfer the money to")
        amm:str = input("what amount would you like to transfer")
        return [fromacc, toacc, amm]

def check_acc_for_transac(transac_det:list[any]) -> bool:

    global bank_accounts
    fromacc, toacc, amm = transac_det
    if fromacc.isalpha() or toacc.isalpha() or amm.isalpha():
        raise ValueError("you entered illegal details, please try again")
    if int(fromacc) not in bank_accounts.keys():
        raise ValueError("'from account' not known, try again")
    if int(toacc) not in bank_accounts.keys():
        raise ValueError("'to account' is not known, please try again")
    if int(fromacc) == 0 or int(toacc) == 0 or int(amm) == 0:
        raise ValueError("one of the parameters is zero, try again")
    return True


def get_idnumber() -> str:
    idnumber:str = ""
    idnumber = input("please type ID number of the accounts")
    return idnumber


def check_idnumber(idnumber:str) -> bool:
    returnId:bool = False
    if idnumber.isalpha():
        raise ValueError("you typed an illegal number, please try again")
    report3L: dict[any] = dict(filter(lambda item: item[1]["id_number"] == idnumber, bank_accounts.items()))
    if not report3L:
        raise ValueError("this id is not known, please try again")
    else: return True

def get_first_name() -> str:
    firstName:str = ""
    firstName = input("please type the first name ")
    return firstName

def check_first_name(firstName:str) -> bool:

    report4L = dict(filter(lambda item: firstName.upper() in (item[1]["first_name"]).upper(), bank_accounts.items()))
    if not report4L:
        raise ValueError("first name not known, please try again")
    return True

def transac(fromacc:int, toacc:int, amm:int) -> bool:

    bank_acc = bank_accounts[fromacc]
    #print(bank_acc)
    listTuples = bank_accounts[fromacc]["transactions_to_execute"]
    #print(listTuples)
    bank_accounts[fromacc]["transactions_to_execute"].append((datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fromacc, toacc, amm))
    bank_acc = bank_accounts[fromacc]
    print(bank_acc)
    return True


def all_transac() ->bool:
    global bank_accounts
    mess_from = {key: value["transactions_to_execute"] for key, value in bank_accounts.items()}
    for key in mess_from.keys():
        if key in bank_accounts.keys():
           print("for this key", mess_from[key])
           for i in range(len(mess_from[key])):
               bank_accounts[key]["transaction_history"].append(mess_from[key][i])
               bank_accounts[key]["balance"] += mess_from[key][i][3]
               print("after append", bank_accounts[key]["transaction_history"])
               print("after balance", bank_accounts[key]["balance"])
           bank_accounts[key]["transactions_to_execute"].clear()
    return True


def report1() -> bool:
    for account_number, values in bank_accounts.items():
        print(f"account number: {account_number}")
        print(f"first_name : {values["first_name"]}")
        print(f"last_name : {values["last_name"]}")

    return True

def report2(accnumber:int) -> bool:
   print(f"account details:")
   print(f"account number: {accnumber} ")
   print(f"first name: {bank_accounts[accnumber]["first_name"]}")
   print(f"last name: {bank_accounts[accnumber]["last_name"]}")
   print(f"ID number: {bank_accounts[accnumber]["id_number"]}")
   print(f"balance: {bank_accounts[accnumber]["balance"]}")
   return True

def report3(id_paramet:str) -> bool:
    report3L = dict(filter(lambda item: item[1]["id_number"] == id_paramet, bank_accounts.items()))
    for account_number, value in report3L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True


def report4(firstName:str) -> bool:
    report4L = dict(filter(lambda item: firstName.upper() in (item[1]["first_name"]).upper() , bank_accounts.items()))
    for account_number, value in report4L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True

def report5() -> bool:
    report5L = dict(sorted(bank_accounts.items(), key=lambda item: item[1]['balance']))
    for account_number, value in report5L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True

def report6() -> bool:
    for i in range(len(bank_accounts.items())):
        report6L = [transaction for account_info in bank_accounts.values() for transaction in
                    account_info['transaction_history']]
        #report6L = [account_info['transaction_history'][i] for account_info in bank_accounts.values()]
        #report6L:list = [lambda (bank_accounts.items(): item[1]["transaction_history"][i])]
    print(report6L)
    report6LS = sorted(report6L, key=lambda x: datetime.strptime(x[0], '%Y-%m-%d  %H:%M:%S'))
    print(report6LS)
    for j in range(len(report6LS)):
        print(report6LS[j])
    return True

def report7() -> bool:
    for i in range(len(bank_accounts.items())):
        report6L = [transaction for account_info in bank_accounts.values() for transaction in
                    account_info['transaction_history']]
    print(report6L)
    today_str = datetime.now().strftime('%Y-%m-%d')
    report6LS = list(filter(lambda x: x[0].startswith(today_str), report6L))
    print(report6LS)
    return True

def report8() -> bool:
    report8L = dict(filter(lambda item: item[1]["balance"] <= 0, bank_accounts.items()))
    if not report8L:
        print("no accounts with negative balance or empty account")
        return
    for account_number, value in report8L.items():
        print(f"account number: {account_number}")
        print(f"first_name : {value["first_name"]}")
        print(f"last_name : {value["last_name"]}")
        print(f"ID number: {value["id_number"]}")
        print(f"balance: {value["balance"]}")
    return True

def report9() -> bool:
    total_balance = sum(account_info['balance'] for account_info in bank_accounts.values())
    print(f"total balance of all accounts: {total_balance}" )

    return True

