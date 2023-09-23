# HBNB - The Console

Welcome to the HBNB Console, an exciting project inspired by the popular Airbnb website! This repository represents the initial stage of our journey to create a clone of Airbnb's functionality. Our goal is to provide a backend interface or console to manage program data effectively. Through this console, users can create, update, and destroy objects, all while seamlessly handling file storage using JSON serialization and deserialization. The best part? Your data remains persistent between sessions.

---

## Explore Our Repository by Project Task

### *Task 0: Authors/README File*
- [AUTHORS](https://github.com/justinmajetich/AirBnB_clone/blob/dev/AUTHORS)
- Meet the brilliant minds behind this project.

### *Task 1: Pep8*
- Our code adheres to the PEP8 style guide, ensuring clean and readable code.

### *Task 2: Unit Testing*
- Dive into our extensive unit tests for class-defining modules, assuring code reliability.

### *Task 3: Make BaseModel*
### *Task 4: Update BaseModel w/ kwargs*
- Enhancing functionality, we enable the recreation of class instances from dictionary representations.

### *Task 5: Create FileStorage class*
- Our custom FileStorage class manages persistent file storage elegantly.

### *Task 6: Console 0.0.1*
- In our early console version, we've added basic functionality. It can quit, handle empty lines, and recognize Ctrl+D commands.

### *Task 7: Console 0.1*
- With further enhancements, the console can now create, destroy, show, and update stored data seamlessly.

### *Task 8: Create User class*
- Dynamically implementing a user class for added versatility.

### *Task 9: More Classes*
- Expanding our dynamic class implementation to include additional essential classes.

### *Task 10: Console 1.0*
- In this major update, our console and file storage system now work dynamically with all
- classes. Expect even greater functionality.

---

## How to Get Started

1. Begin your journey by cloning this repository.

2. Once you have cloned the repository, locate the "console.py" file, and run it using the following command:

   
   ./console.py
   

3. Upon executing the command, you'll be greeted with the following prompt:

   
   (hbnb)
   

4. This prompt signifies that you are now in the "HBnB" console, ready to explore its various commands.

### Available Commands
### Available Commands
- create - Generate an instance based on a specified class.
- destroy - Remove an object based on class and UUID.
- show - Display an object based on class and UUID.
- all - List all objects accessible to the program or objects of a given class.
- update - Modify existing attributes of an object based on class name and UUID.
- quit - Gracefully exit the program (EOF works too).

### Unlock Advanced Syntax
For experienced users, we offer an advanced syntax for some commands:

- all - Show all objects accessible to the program or objects of a given class.
- count - Retrieve the number of object instances by class.
- show - Display an object based on class and UUID.
- destroy - Remove an object based on class and UUID.
- update - Modify existing attributes of an object based on class name and UUID.

---

## Let's Dive into Some Examples

### Primary Command Syntax

*Example 1: Create an Object*
(hbnb) create BaseModel


*Example 2: Show an Object*

(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8


*Example 3: Destroy an Object*

(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8


*Example 4: Update an Object*

(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"


### Advanced Syntax

*Example 1: Show all User Objects*

(hbnb) User.all()
*Example 2: Destroy a User*

(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")


*Example 3: Update User by Attribute*

(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")


*Example 4: Update User by Dictionary*

(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})


---

We're excited to embark on this journey of recreating Airbnb's functionality, one step at a time. Join us as we continue to refine and expand the HBNB Console to offer even more features and capabilities.

For any questions or feedback, feel free to reach out to our dedicated team of developers. Happy coding!

