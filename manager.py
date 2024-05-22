import argparse
import os

def create_admin(username, password):
    # Define the file path for storing admin credentials
    admin_file = "admin_credentials.txt"
    
    # Check if the admin credentials file already exists
    if os.path.exists(admin_file):
        print("Error: Admin user already exists.")
        return
    
    # Save the admin credentials to the file
    try:
        with open(admin_file, 'w') as f:
            f.write(f"username: {username}\n")
            f.write(f"password: {password}\n")
        print(f"Admin user '{username}' created successfully.")
    except Exception as e:
        print(f"Error: Unable to create admin user. {e}")


def purge_data():
    """Function to purge (delete) the data.json file."""
    try:
        os.remove("data.json")
        print("Data file 'data.json' has been removed.")
    except FileNotFoundError:
        print("Data file 'data.json' does not exist.")



def main():
    parser = argparse.ArgumentParser(description="System Manager Script")
    parser.add_argument('command', choices=['create-admin'], help="Command to execute")
    parser.add_argument('--username', required=True, help="Username for the admin")
    parser.add_argument('--password', required=True, help="Password for the admin")
    parser.add_argument("command", help="Command to perform (e.g., 'purge-data').")
    args = parser.parse_args()

    if args.command == 'create-admin':
        create_admin(args.username, args.password)

if __name__ == "__main__":
    main()