# Name: Jaylen Howe
# Date: January 17, 2025

# The following Python script covers the tasks as outlined for the assignment. 
# It demonstrates the creation and manipulation of a list, tuple, and dictionary. 

# LIST:
# Create a list with at least five elements
my_list = [10, 20, 30, 40, 50]

# Print the length of the list
print("Length of the list:", len(my_list))

# Print only the elements in the first three positions of the list
print("First three elements:", my_list[:3])

# Print only the last element in the list
print("Last element:", my_list[-1])

# Append an element to the list, then print out the new list
my_list.append(60)
print("List after appending 60:", my_list)

# Insert a new element in the list at the beginning of the list, print out the list
my_list.insert(0, 5)
print("List after inserting 5 at the beginning:", my_list)

# Sort the list, print out the sorted list
my_list.sort()
print("Sorted list:", my_list)

# TUPLE:
# Create a tuple with at least five elements, print out the tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Print the number of items in the tuple
print("Number of items in the tuple:", len(my_tuple))

# DICTIONARY:
# Create a dictionary with at least five keys and their values, print the dictionary
my_dict = {"name": "Jaylen", "age": 20, "city": "Land O Lakes", "profession": "Student", "hobby": "Music"}
print("Dictionary:", my_dict)

# Index a specific key, print the value associated with that key
print("The value associated with 'name' is:", my_dict["name"])

# Add a key to the dictionary, print the dictionary
my_dict["favorite_color"] = "Blue"
print("Dictionary after adding 'favorite_color':", my_dict)

# Delete a key within the dictionary, print the dictionary
del my_dict["hobby"]
print("Dictionary after deleting 'hobby':", my_dict)
