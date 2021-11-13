def display():
    print('\n'+('************//Display List//*************').center(95)+'\n')
    print('Sl. No.'.center(9) + 'Name of Item'.center(15) + 'Present Stock'.center(17) + 'Purchased Quantity'.center(
        19) + 'Issue Quantity'.center(19)+ 'Total Quantity'.center(15))
    print('*'*95)
    j=0
    for i in item_list:
        j=j+1
        print((' '+str(j)+'.').ljust(12)+i.ljust(13)+(str(item_list[i][0])).center(16)+('+'+str(item_list[i][
                                                                                                    1])).center(
            19)+('-'+str(item_list[i][2])).center(17)+(str(item_list[i][3])).center(17))
    print('\n')
    input("Press any key to return to previous section")


def update():
    print('\n==Update menu==\n')
    print('Warning!! updating the list will lead to loss of Purchase data in the database. Are you sure you want to '
          'continue? ')
    cont=input('Press Y to continue or press any other key to go back to previous section...')
    for i in item_list:
        item_list[i][0]=item_list[i][3]
        item_list[i][1]=0
        item_list[i][2]=0
    print ('\nDatabase updated successfully...\n')


def database(s):
    if s==0:
        input('Database is empty!! Please register an item before visiting the database section. Press any key to '
              'go back to previous section... ')
        return
    while(1):
        print('\n==Database menu==\n')
        print('1. Display Database','2. Update Database', '3. Go back to previous section\n',sep='\n')
        d=input('Your answer: ')
        if d=='1':
            display()
        elif d=='2':
            update()
        elif d=='3':
            return
        else:
            print('Invalid input')




def item_addition(slno):
    print('\n==New items Registration menu==\n')
    n=int(input('How many item(s) will you like to add? '))
    for i in range(slno,slno+n):
          item = input('\nAdd your item '+str(i+1)+': ')
          pstock = int(input('Present stock quantity: '))
          recieved = 0
          issue = 0
          total=pstock
          item_list[item]=[pstock,recieved,issue,total]
    if n==0:
        print('No new items registered!!')
        return n
    print('\nNew item(s) registered')
    return slno+n


def item_removal(s):
    while(1):
        print('\n==Item Removal menu==\n')
        print('Press','1. Remove all items','2. Remove selective item(s)','3. Go back to previous section\n',sep='\n')
        ans=input('Your answer: ')
        if ans=='1':
            item_list.clear()
            print('All items removed!!')
            s=0
            return s
        elif ans=='2':
            ritem=int(input('How many item(s) you want to remove? '))
            removelist=[input('Enter the item '+str(k+1)+': ') for k in range(ritem)]
            j=0
            for i in range(ritem):
                if removelist[i] in item_list:
                    del item_list[removelist[i]]
                    print(removelist[i]+' removed successfully!!')
                    j=j+1
                else:
                    print(removelist[i]+' not found in the database!!')
            s= s-j
            if s==0:
                return s
        elif ans=='3':
            return s
        else:
            print('Invalid input')


def item_reg(s):
    while(1):
        print('\n==Item Registraion==\n')
        if s == 0:
            a = input('Press any key to start adding your first item(s)... or Press N to go back: ')
            if a == 'N':
                return s
            s = item_addition(s)
        print('What would you like to do?\n')
        print('1. Register new item(s)', '2. Remove registered item(s)','3. Go back to previous '
                                                                                       'section\n', sep='\n')
        ans = input('Your answer: ')
        if ans == '1':
            s=item_addition(s)
        elif ans == '2':
            s=item_removal(s)
        elif ans == '3':
            return s
        else:
            print('Invalid option. Choose again!\n')





def purchase(s):
    if s==0:
        print("No items are registered yet. Please register an item before beginning the purchase process.",
              'Press any key to go back to previous section....',sep='\n',end='')
        input()
        return
    while (1):
        print('\n==Purchase Store==\n')
        print('How many different item(s) have you purchased from the database? (Press 0 to go back to '
                         'previous section)')
        pans=int(input('Your answer: '))
        print('\n')
        if pans == 0:
            return
        for i in range(pans):
            item = input('Enter the item ' + str(i + 1) + ': ')
            if item in item_list:
                while (1):
                    value = int(input('Enter the amount you want to issue for this item: '))
                    if ((item_list[item][0] + value)<item_list[item][2]):
                        print('Purchase quantity cannot be less than the present issue quanity which is greater than ('
                              'Present Stock + Purchase Quantity). Please re-adjust the issue value to make '
                              'further changes in the purchase database or enter an equal or greater value')
                    else:
                        break
                item_list[item][1] = value
                item_list[item][3] = item_list[item][0] + item_list[item][1]-item_list[item][2]
                print('Item found and purchase details included in the database..\n')
            else:
                print("Item not found in the database. Please register the item first to enter purchase detail..\n")
        return



def sell(s):
    if s == 0:
        print("No items are registered yet. Please register an item before beginning the issue process.",
              'Press any key to go back to previous section....', sep='\n', end='')
        input()
        return
    while (1):
        print('\n==Issue Store==\n')
        print('How many different item(s) do you want to issue from the database? (Press 0 to go back to '
              'previous section)')
        pans = int(input('Your answer: '))
        print('\n')
        if pans == 0:
            return
        for i in range(pans):
            item = input('Enter the item ' + str(i + 1) + ': ')
            if item in item_list:
                while(1):
                    value = int(input('Enter the amount you want to issue for this item: '))
                    if value<=(item_list[item][0] + item_list[item][1]):
                        break
                    else:
                        print('Invalid input. Issue quantity cannot be greater than (Present Stock + Purchase '
                              'Quantity)')
                item_list[item][2] = value
                item_list[item][3] = (item_list[item][0] + item_list[item][1])-item_list[item][2]
                print('Item found and issue details included in the database..\n')
            else:
                print("Item not found in the database. Please register the item first to enter issue detail..\n")
        return



if __name__ == "__main__":
    s=0
    item_list={}
    while(1):
        print('\n********Item Store*********\n')
        print('Press','1. Database','2. Item Registration', '3. Purchase Store','4. Issue Store','5. Exit\n',sep='\n')
        isans=input('Your answer: ')
        if isans == '1':
            database(s)
        elif isans == '2':
            s=item_reg(s)
        elif isans == '3':
            purchase(s)
        elif isans == '4':
            sell(s)
        elif isans == '5':
            exit(-1)
        else:
            print('Invalid input')
