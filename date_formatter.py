'''
Program for taking various date formats and modifying them into a desired format for a pizza delivery company.
The input is entered as ["date" "current format" "desired format"]. 
Created for the Microsoft coding competition at the University of Victoria, September 21st 2017.
'''

import re
import sys
import fileinput

#Formats the input. Takes a list of input as parameter.
def format_dates(lines):
	new_dates = []
	for line in lines:
		#Separating the date from the current date and desired date.
		term = line.split()

		#Separating the day from month from year.
		numbers = re.split('[^a-zA-Z0-9]', term[0])
		#Separating the "mm" from "dd" from "yyyy".
		str = re.split('[^a-zA-Z0-9]', term[1])

		dic = dict(zip(str,numbers))

		#Replacing the "dd", "mm" and "yyyy" in the desired date format with the actual date.
		if dic.get('dd'):
			term[2] = term[2].replace('dd', dic['dd'])
		if dic.get('yyyy'):
			term[2] = term[2].replace('yyyy', dic['yyyy'])
		if dic.get('mm'):
			term[2] = term[2].replace('mm', dic['mm'])

		new_dates.append(term[2])
	return new_dates

def main():
	#Reading from the input file.
	with open("PracticeInput.txt") as f:
		lines = f.readlines()
	lines = [x.strip() for x in lines]

	lines = format_dates(lines)

	for line in lines:
		print line

if __name__ == '__main__':
	main()
