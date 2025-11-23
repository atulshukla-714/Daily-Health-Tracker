 Daily Health Tracker

A simple command-line Python script to track your **daily calorie intake** and **water consumption**.

How to Run :

Prerequisites :

You need "Python 3" installed on your system.

Execution :

1.  **Save the code:** Save the Python code into a file named `health_tracker.py`.

2.  **Run from the terminal:** Open your terminal or command prompt and exeute the script using the following comand:

    ```bash
    python health_tracker.py
    ```

3.  **Follow the prompts:** The script will ask you to enter the calorie count breakfast, lunch, and dinner, and your total water intake for the day.


Features :

  **Calorie Tracking:** Quickly input and sum up your calories from three main meals (breakfast, lunch, and dinner).
  **Water Tracking:** Record your total water intake in liters.
  **Daily Summary:** Provides a clear summary of the total calories consumed and water intake for the day.



 Code Overview :

The script uses basic Python input and arithmetic operations.

| Section | Description | Variables Used |
| :--- | :--- | :--- |
| **Initialization** | Sets starting values for tracking. `calories`, `water` |
| **Calorie Input** | Prompts the user to enter calories for each meal and calculates the total. | `breakfast`, `lunch`, `dinner` |
| **Water Input** | Prompts the user to enter total water intake in liters. | `water` |
| **Summary Output** | Prints the final calculated summary. | `calories`, `water` |

-----

Future Enhancements

Add tracking for snacks and and exercise.
Implement daily calorie and water intake **goals**.
Store the data in a file (e.g., CSV or a database) for historical tracking.
Add **data validation** (e.g., ensuring only positive numbers are entered).

