# Function to read issue types from the external file
def read_issue_types(file_name):
    issue_types = {}
    with open(file_name, 'r') as file:
        for line in file:
            category, types = line.strip().split(': ')
            issue_types[category] = types.split(', ')
    return issue_types

# Function to display issue types and categories
def display_issue_types(issue_types):
    for category, types in issue_types.items():
        print(f"{category}: {', '.join(types)}")

# Function to create a new support ticket
def create_ticket(issue_types):
    print("Enter your name:")
    name = input()

    print("Select a category:")
    display_issue_types(issue_types)
    category = input()

    while category not in issue_types:
        print("Invalid category, please try again.")
        category = input()

    print("Select an issue type:")
    types = issue_types[category]
    print(", ".join(types))
    issue_type = input()

    while issue_type not in types:
        print("Invalid issue type, please try again.")
        issue_type = input()

    print("Describe your issue:")
    description = input()

    ticket = {
        "Name": name,
        "Category": category,
        "Issue Type": issue_type,
        "Description": description
    }
    return ticket

# Main function
def main():
    issue_types = read_issue_types("issue_types.txt")

    print("Welcome to Technical Support Ticketing System")
    while True:
        print("\n1. Create a new ticket")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            ticket = create_ticket(issue_types)
            print("\nTicket created successfully:")
            print(ticket)
        elif choice == "2":
            print("Thank you for using the Technical Support Ticketing System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
