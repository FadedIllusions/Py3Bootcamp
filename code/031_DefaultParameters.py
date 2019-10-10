def show_information(first_name="James", is_instructor=False):
	if first_name == "James" and is_instructor:
		return "Welcome back, instructor James!"
	elif first_name == "James":
		return "I really thought that you were an instructor..."
	return f"Hello {first_name}!"

print(show_information())
print(show_information(is_instructor=True))
print(show_information('Molly'))