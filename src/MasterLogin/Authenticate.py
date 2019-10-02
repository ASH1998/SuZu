from src.MasterLogin.login import  get_connection

# def users(newuser, )

if __name__ == '__main__':
	df = get_connection(r"pythonsqlite.db")
	print("IF new user input 1, if old user input 0")
	userage = input("input > ")
	if userage=='1':
		print(df)
