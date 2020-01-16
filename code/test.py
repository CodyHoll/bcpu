p2 = 8
p3 = 2

p4 = 0
p5 = 0


print("Running: {} / {}".format(p2,p3))
print()
try:
	print("Expected: base: {}  remainder: {}".format(p2//p3,p2%p3))
except:
	print("cant div that")


# p4=8//2 , p5=8%2

# if denominator is 0, throw error
if p3 != 0:
	# r2 pos, r3 pos
	if(p2 >= 0 and p3 > 0):
		# if denum is greater
		p5 = p2
		# if num is greater
		while(p2 >= p3): 
			p4 = p4 + 1
			p2 = p2 - p3
			p5 = p2

	# r2 pos, r3 neg
	elif(p2 >= 0 and p3 < 0):
		#if either is greater
		while(p2 > 0):
			p4 = p4 - 1
			p2 = p2 + p3
			p5 = p2


	# r2 neg, r3 pos
	elif(p2 <= 0 and p3 > 0):
		# if either is greater
		while(p2 < 0):
			p4 = p4 - 1
			p2 = p2 + p3
			p5 = p2

	# r2 neg, r3 neg
	elif(p2 <= 0 and p3 < 0):
		# if denum is greater
		p5 = p2
		#if num is greater
		while(p2 <= p3):
			p4 = p4 + 1
			p2 = p2 - p3
			p5 = p2


	else:
		print("should never get here")






# denum was zero
else:
	print("error")
	

print()
print("Returned: base: {} remainder: {}".format(p4,p5))


