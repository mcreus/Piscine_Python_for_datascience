import sys

def main():
	av = sys.argv
	try:
		if len(av) != 2:
			raise AssertionError("more than one argument is provided" if len(av) > 2 else "argument is required")
		
		_av = av[1]

		try:
			nb = int(_av)
		except ValueError:
			raise AssertionError("argument is not an integer")

		if nb % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")
	except AssertionError as e:
		print(f"AssertionError: {e}")

if __name__ == "__main__":
	main()