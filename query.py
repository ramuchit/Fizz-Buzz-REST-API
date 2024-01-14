def generate_fizz_buzz_string(int1:int, int2:int, limit:int, str1:str, str2:str) ->str:
	string = ""
	for num in range(1,limit):
		if num % int1 == 0 and num % int2 == 0:
			string = string+str1+str2
		elif num % int1 == 0 :
			string = string+str1
		elif num % int2 == 0 :
			string = string+str2
		else:
			string = string +str(num)

		string = string+","

	return string.rstrip(",")