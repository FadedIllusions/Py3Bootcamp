# Example Uses:
# Complex Data Structures -- Matricies, Game Maps,
# And Grouping/Tabulating Data


# Example:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# To Access Last List
print(f"Last List: {nested_list[-1]}")
# To Access Item In Last List
print(f"Last Item: {nested_list[-1][-1]}")


# Iterate Through Nested List
print("\nNested Loop Iteration:")
for l in nested_list:
	for val in l:
		print(f"List: {l}, Value: {val}")

		
# Nested List Comprehension
print("\nNested List Comprehension:")
[[print(f"List: {l}, Value: {val}") for val in l] for l in nested_list]


# Create Game Board Matrix With Nested List Comprehension
board = [[num for num in range(1,4)] for val in range(1,4)]
print("\nGame Board:")
[[print(row)] for row in board]

ttt_board = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print("\nSecond Game Board:")
[[print(row)] for row in ttt_board]