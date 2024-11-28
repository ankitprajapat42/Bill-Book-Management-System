import datetime
bill_book = {101:{'date': '30-08-2022', 'name':'Naveen', 'mobile_no': 6367850035, 'item_no':2, 'data':[['Sugar',45,4] ,['Salt', 28, 2]]}}

def print_bill(bill_no):
    print('+','-'*71, '+')
    print(f'|{"Bill Book":^73}|')
    print('+','-'*71, '+')
    print(f'| Bill No: {bill_no} {bill_book[bill_no]['date']:>58} |')
    print(f"| Custumer Name : {bill_book[bill_no]['name']:<36} {'|':>20}\n| Mobile No.: {bill_book[bill_no]['mobile_no']:>14} {"|":>46}")
    print('+','-'*3, '+','-'*33,'+','-'*7,'+','-'*8,'+','-'*8,'+')
    print(f"|{'SNo':^5}|{'Item Name':^35}|{'Rate':^9}|{'Quntity':^10}|{'Price':^10}|")
    print('+','-'*3, '+','-'*33,'+','-'*7,'+','-'*8,'+','-'*8,'+')
    total = 0
    for i in range(bill_book[bill_no]['item_no']):
        price = bill_book[bill_no]['data'][i][1] * bill_book[bill_no]['data'][i][2]
        total+= price
        print(f"|{i+1:^5}| {bill_book[bill_no]['data'][i][0]:<34}|{bill_book[bill_no]['data'][i][1]:^9}|{bill_book[bill_no]['data'][i][2]:^10}|{price:^10}|")

    print(f"|{'':^5}| {'':<34}|{'':^9}|{'':^10}|{'':^10}|")
    print(f"|{'':^5}| {'':<34}|{'':^9}|{'':^10}|{'':^10}|")
    print('+','-'*3, '+','-'*33,'+','-'*7,'+','-'*8,'+', '-'*8, '+')
    print(f"|{'Total Amount':>61} : {total:^9}|")
    print('+','-'*71, '+')

    

def add_item(n):
    data = []
    for i in range(n):
        item_name = input(f"Enter the Item Name {i+1}: ")
        item_rate = int(input(f"Enter the Item Rate {i+1}: "))
        item_quntity = int(input(f"Enter the Item Quntity {i+1}: "))
        data.extend([[item_name, item_rate, item_quntity]])
    return data
 
while True:
    print('\n',"Bill Book".center(40, '*'),'\n')
    print("Press 1 for Create Bill\nPress 2 for Veiw all bills \nPress 0 for Exit")
    n = input()
    if n=='1':
        name = input("Enter the Custumer Name : ")
        mobile_no = int(input("Enter the Custumer Mobile No.:"))
        no_item = int(input("Enter the Number of item : "))
        data = add_item(no_item)
        bill_no = list(bill_book.keys())[-1] + 1
        date = str(datetime.datetime.now().strftime('%d-%m-%y'))
        bill_book.update({bill_no:{'date': date, 'name':name,'mobile_no': mobile_no, 'item_no': no_item, 'data' : data}})
        print_bill(bill_no)
    elif n=='2':
        for i in bill_book.keys():
            print_bill(i)
            print("\n\n")
    elif n=='0':
        print("Application Close".center(40, '-'))
        
        break
    else:
        print("You Enter Incorrect Option")

