#!/usr/bin/env python
'''
Simple base conversion program; Accepts two arguments for number and base, or prompts for them
If no base is entered, program calculates for all bases up to base 64
'''
import sys,string
def base_conv(num,base):
	base_nums = '0123456789'+string.ascii_uppercase+string.ascii_lowercase+'+/'	#up to base 64
	base_nums = [base_nums[x] for x in range(base)]			#select range according to current base
	n=1
	while base**n<num:				#find upper boundary
		n+=1
	conv=[]
	while num:						#convert to new base
		r=divmod(num,base**n)
		if r[0]:
			conv.append(str(base_nums[int(r[0])]))	
			num-=r[0]*base**n
		else:
			if conv:				#eliminate leading zeros
				conv.append('0')
		n-=1
	return ''.join(conv)
		
def main():
	if len(sys.argv) > 1:			#check for input arguments
		try:
			num = int(sys.argv[1])
			base = int(sys.argv[2])
		except:
			print 'error; script base_conv can take 2 integer args (num and base)'; sys.exit()
	else:
		num = float(raw_input('enter num: '))
		base = raw_input('choose base or hit enter to show all: ')
	print 'Calculating for',num
	if base:
		print base_conv(num,int(base))
	else:
		for base in range(2,65):
			print 'in base',base,':',base_conv(num,base)
	
if __name__ == '__main__':
	main()