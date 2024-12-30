import pandas as pd 

def excel_file(file_name):
  """ Initializing the Excel file """
    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'Username', 'Email', 'Phone'])
    return df

def view_rows(df):
  """ view all rows in the excel file 
  args*:   df
  return: None 
  """
    print(df)

def add_row(df, file_name):
    name = input("Enter name: ")
    username = input('Enter username: ')
    email = input("Enter email: ")
    phone = input("Enter phone: ")
   
    new_row = pd.DataFrame([[name, username, email, phone]], columns=['Name', 'Username', 'Email', 'Phone'])
    df = pd.concat([df, new_row])
    df.to_excel(file_name, index=False)
    print("Row added successfully!")

def edit_row(df, file_name):
    view_rows(df)
    index = int(input("Enter the index of the row to edit: "))
    column = input("Enter the column to edit (Name, Username, Email, Phone): ")
    new_value = input("Enter the new value: ")
   
    df.at[index, column] = new_value
    df.to_excel(file_name, index=False)
    print("Row edited successfully!")

# Delete a row
def delete_row(df, file_name):
    view_rows(df)
    index = int(input("Enter the index of the row to delete: "))
   
    df = df.drop(index)
    df.to_excel(file_name, index=False)
    print("Row deleted successfully!")

# Main function
def main():
    file_name = 'New.xlsx'
    df = excel_file(file_name)
   
    while True:
        print("\nOptions:")
        print("1. View all rows")
        print("2. Add a new row")
        print("3. Edit a row")
        print("4. Delete a row")
        print("5. Quit")
       
        option = input("Enter your choice: ")
       
        if option == '1':
            view_rows(df)
        elif option == '2':
            add_row(df, file_name)
            df = excel_file(file_name)
        elif option == '3':
            edit_row(df, file_name)
            df = excel_file(file_name)
        elif option == '4':
            delete_row(df, file_name)
            df = excel_file(file_name)
        elif option == '5' or 'quit':
            print('See you next time (:')
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

# dataFrame = pd.DataFrame([[First_name, Last_name, username]],
#                          columns=['First Name', 'Last Name', 'Username'])
                         

# FileName = input('Enter the file name: ')
# dataFrame.to_excel(FileName + '.xlsx')
