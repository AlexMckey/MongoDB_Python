person = {'name':"Sir Alex Mckey", 'favorite_color':"Blue", 'hair':"Brown",'interests':["cicling","running","biking"]}

for key in person:
	if (key == 'interests'):
		print("Interests...")
		for item in person[key]:
			print("\tinterest = " + item)
	else:
		print("[" + key + "] = " + person[key])