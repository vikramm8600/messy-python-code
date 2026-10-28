Python Code Anti-Patterns 🐍

Project Overview

This project demonstrates common Python programming anti-patterns and poor coding practices through a deliberately confusing Python script.

The program uses global variables, mutable default arguments, unclear variable names, unnecessary dynamic code execution, complex expressions, and random inputs to demonstrate how poorly structured code can become difficult to understand, maintain, and debug.

The purpose of this project is to identify problematic coding practices and understand how they affect code readability, reliability, and maintainability.

Objectives

* Understand common Python programming anti-patterns.
* Identify confusing variable and function names.
* Understand the risks of mutable default arguments.
* Recognize problems associated with global variables.
* Identify unnecessary use of exec().
* Understand why side effects in expressions can reduce readability.
* Learn the importance of clean, maintainable code.

Technologies Used

* Python
* random module
* math, os, and sys modules

The program uses Python’s standard library and does not require external packages.

Features

* Generates random integer values.
* Selects random multipliers.
* Modifies a list inside a function.
* Filters even numbers using a list comprehension.
* Updates a global counter.
* Executes a dynamically constructed Python statement.
* Returns a lambda function that behaves differently depending on the counter’s parity.
* Repeats the operations five times.

How the Program Works

1. Global Variable

The program initializes a global variable named global_cOunt with the value 666.

The function modifies this variable, making the program’s behavior dependent on shared state.

2. Mutable Default Argument

The function do_stuff_O_0() uses a list as its default argument:

I=[1, 2, 3]

Because this list is mutable and created only once when the function is defined, modifications can persist across calls that use the default argument.

3. List Modification

The function appends a value to the list and removes the first element if the list grows beyond ten elements.

4. List Comprehension

The program selects even numbers from the list and multiplies them by a supplied value.

The number of selected elements is added to the global counter.

5. Dynamic Code Execution

The program uses exec() to print the current counter.

Although it works for this simple example, using exec() unnecessarily can make code harder to understand and introduce security risks in situations involving untrusted input.

6. Lambda Function

The function returns a lambda expression whose behavior depends on whether the global counter is even or odd.

Depending on the counter’s parity, the lambda either reverses the string representation of its input or attempts to convert that representation into an integer.

This inconsistent return behavior makes the function difficult to reason about.

7. Randomized Main Loop

The main loop executes five times.

During each iteration, the program generates a random integer between 10 and 50 and randomly selects a multiplier from 2, 3, and 5.

It then calculates the sum of integers below the generated number that are divisible by the selected multiplier and passes that sum to the returned lambda function.

Identified Anti-Patterns

Anti-Pattern	Description
Unclear Naming	Names such as O, l, I, and do_stuff_O_0 are difficult to interpret.
Global State	The global counter creates dependencies between function calls.
Mutable Default Argument	The default list retains modifications across calls.
Unnecessary exec()	Dynamic execution is unnecessary for printing a value.
Side Effects	The function modifies shared state and a list while performing calculations.
Inconsistent Return Types	The lambda may return a string or an integer.
Magic Numbers	Values such as 666, 10, and 5 are embedded directly in the code.
Unused Imports	The math, os, and sys modules are imported but not used.
Randomized Behavior	Random values make exact output difficult to reproduce without controlling the random seed.

How to Run

1. Install Python 3 if it is not already installed.
2. Download or clone the repository.
3. Open a terminal in the project directory.
4. Run the program:

python messy.py

    Alternatively, use:

python3 messy.py

5. Observe the debug messages and the results of the five iterations.

Expected Behavior

The program prints the current global counter and the result of each iteration.

The exact output can vary because the program uses random numbers and random multipliers.

Note: The program is intentionally written with confusing practices for educational purposes. It is not intended to serve as an example of production-quality Python code.

Recommended Improvements

* Replace unclear variable and function names with descriptive names.
* Avoid mutable default arguments by using None and initializing lists inside functions.
* Pass shared state explicitly instead of relying on global variables.
* Replace exec() with a normal print() statement.
* Separate calculations from operations that modify state.
* Ensure functions return consistent data types.
* Replace magic numbers with named constants where appropriate.
* Remove unused imports.
* Add tests and control random inputs when reproducible behavior is needed.

Conclusion

This project illustrates how common Python anti-patterns can make a program confusing and difficult to maintain.

By studying the code and identifying its weaknesses, developers can better understand the importance of clear naming, predictable functions, safe data handling, and readable program structure.

The project serves as a learning exercise in code quality, debugging, and Python best practices.
