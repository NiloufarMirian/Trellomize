import pandas as pd

# Sample data for tasks and statuses
data = {'Task': ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5'],
        'Status': ['Completed', 'In Progress', 'Pending', 'Completed', 'Pending'],
        'Priority': ['High', 'Medium', 'Low', 'High', 'Medium'],
        'Due Date': ['2022-12-31', '2022-11-15', '2022-10-20', '2022-12-10', '2022-11-30'],
        'Assigned To': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the tasks in a table
print(df)

# Select a task by index
task_index = int(input("Enter the index of the task you want to view and modify: "))

# Display details of the selected task
selected_task = df.iloc[task_index]
print("\nSelected Task Details:")
print(selected_task)

# Modify the task status
new_status = input("Enter the new status for the task: ")
df.at[task_index, 'Status'] = new_status

# Display the updated table
print("\nUpdated Task Table:")
print(df)