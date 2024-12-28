A command-line application to add, remove, and display tasks. You can extend it by saving tasks to a file.

Key Concepts to Implement:
Classes for task representation.
File I/O or SQLite for data persistence.
List/Dict to manage tasks in memory.
User Input Handling for interaction.

Implement a simple menu (text-based) where the user can:
Add a task
View tasks (with optional filtering)
Update a task
Delete a task
Continuously prompt the user for input until they choose to exit.

Task Representation:
Define a Task class that includes attributes like:
id: Unique identifier (can be an integer or UUID).
description: A string for the task.
status: Boolean or string to indicate if the task is completed.
