#!/usr/bin/python3
def safe_print_division(a, b):
	rem = 0
	try:
		rem = a / b
	except (TypeError, ZeroDivisionError):
		rem = None
	finally:
		print("Inside result: {}".format(rem))
	return (rem)
