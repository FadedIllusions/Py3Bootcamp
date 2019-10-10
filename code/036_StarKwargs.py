# **kwargs
# Special operator we can pass to function
# Gathers remaining keyword arguments as a dictionary
# Generates such a dictionary via a generator
#
# def fav_colors(colt="purple", ruby="red", ethel="teal"):

def fav_colors(**kwargs):
	#{print(f"{key} : {value}" for key,value in kwargs.items())}
	for key, value in kwargs.items():
		print(f"{key[0].upper() + key[1::]} : {value[0].upper() + value[1::]}")
	
fav_colors(colt="purple", ruby="red", ethel="teal")