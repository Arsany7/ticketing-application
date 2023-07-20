**Technical Support Ticketing System - README**

This is a basic prototype of a text-based Technical Support Ticketing System written in Python. The application allows users to create new support tickets for different technical issues by selecting predefined categories and issue types. The issue types are organized in categories and defined in an external file (`issue_types.txt`).

**Getting Started:**

1. Clone the repository or download the `ticketing_system.py` and `issue_types.txt` files to your local machine.

2. Ensure you have Python installed on your system. This application was tested on Python 3.7+.

3. Before running the application, make sure to set up the `issue_types.txt` file with the desired issue categories and types. The format of the file should be as follows:

```
Category1: IssueType1, IssueType2, IssueType3
Category2: IssueType4, IssueType5
```

**Running the Application:**

1. Open your terminal or command prompt.

2. Navigate to the directory where you have saved the `ticketing_system.py` and `issue_types.txt` files.

3. To start the Technical Support Ticketing System, execute the following command:

```
python ticketing_system.py
```

**Using the Application:**

1. Upon running the application, you will be presented with a menu:

```
Welcome to Technical Support Ticketing System

1. Create a new ticket
2. Exit
```

2. To create a new support ticket, choose option "1".

3. Follow the prompts to provide your name, select a category, an issue type, and describe your issue.

4. After creating the ticket, its details will be displayed on the screen.

5. To exit the application, choose option "2".

**Customization and Expansion:**

This is a starting prototype for a basic text-based ticketing system. You can customize and expand it further based on your requirements. For instance:

- Implement persistent data storage using databases.
- Enhance error handling for user inputs.
- Include additional features like ticket tracking, ticket status updates, etc.
- Improve the user interface for a better user experience.

**Contributing:**

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on the repository.

**License:**

This Technical Support Ticketing System is open-source and distributed under the MIT License. See the `LICENSE` file for more details.

**Acknowledgments:**

The code for this prototype was developed as a basic implementation of a technical support ticketing system. Thanks to the Python community for their support and inspiration.

Thank you for using the Technical Support Ticketing System! If you have any questions or need assistance, don't hesitate to contact us. Happy ticketing!
