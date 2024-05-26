import logging

logging.basicConfig(filename='loggerfile.log', level=logging.INFO)
logger = logging.getLogger()

file_handler = logging.FileHandler('loggerfile.log')
logger.addHandler(file_handler)

logger.info(f"User {user} is already in the project.")
logger.error(f"User {user} removed.")
logger.error(f"User {user} is not in the project.")
logger.info("this user is currently assigned to this task")
logger.info(f"User {user} added")
logger.error(f"User {user} removed")
logger.error(f"User {user} is not in the task.")
logger.error("Invalid email format.")
logger.error("Invalid username. It must be alphanumeric and between 3 and 20 characters.")
logger.info("Email is already used.")
logger.info("Username is already taken.")
logger.info(f"User {username} registered successfully.")
logger.info("Registration successful.")
logger.error("Registration failed. Please try again.")
logger.error("Username does not exist.")
logger.error("This account has been deactivated")
logger.error("Incorrect password.")
logger.info("Project created")
logger.info("Task created")
logger.info("user added")
logger.error("user removed")
#logger.info("priority changed")
logger.error("wrong input")
#logger.info("status changed")
logger.error("wrong input")
logger.info("comment added")
logger.info("comment added")
logger.error("there is no tasks")
logger.error("wrong input")
logger.error("there is no projects")
logger.error("wrong input")
logger.info("User added successfully")
logger.error(f"User {user} not found.")
logger.error("there is no projects")
logger.error("wrong input")
logger.error("wrong input")
logger.info("Login successful.")
logger.info("Login failed. Please try again.")