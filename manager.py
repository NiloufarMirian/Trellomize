import argparse
import os

def create_admin(username, password):
    
    admin_file = "admin_credentials.txt"
    
    
    if os.path.exists(admin_file):
        print("Error: Admin user already exists.")
        return
    
    
    try:
        with open(admin_file, 'w') as f:
            f.write(f"username: {username}\n")
            f.write(f"password: {password}\n")
        print(f"Admin user '{username}' created successfully.")
    except Exception as e:
        print(f"Error: Unable to create admin user. {e}")


def purge_data():
    """Function to purge (delete) the data.json file."""
    confirmation = input("Are you sure you want to delete 'data.json'? This action cannot be undone. (yes/no): ").strip().lower()
    if confirmation == 'yes':
        try:
            os.remove("data.json")
            print("Data file 'data.json' has been removed.")
        except FileNotFoundError:
            print("Data file 'data.json' does not exist.")
    else:
        print("Action cancelled. 'data.json' was not deleted.")


def main():
    parser = argparse.ArgumentParser(description="System Manager Script")
    parser.add_argument('command', choices=['create-admin', 'purge-data'], help="Command to execute")
    parser.add_argument('--username', help="Username for the admin")
    parser.add_argument('--password', help="Password for the admin")
    args = parser.parse_args()

    if args.command == 'create-admin':
        if args.username and args.password:
            create_admin(args.username, args.password)
        else:
            print("Error: Both username and password are required for creating admin.")

    elif args.command == 'purge-data':
        purge_data()

if __name__ == "__main__":
    main()
