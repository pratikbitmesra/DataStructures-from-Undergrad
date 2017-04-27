
import os
import sys
import operator
import time

#Global Variables
store_line = []
changed_store_line = []
changed_begin_end_count = []
char_begin_end_count = []
previous_position = 0

def find_line_and_cursor_from_beginning(cursor):	
	char_counter = 0
	line_of_cursor = -11111111
	cursor_from_beginning = 0
	global changed_begin_end_count 
	global changed_store_line 
	global previous_position
	position_from_end = 0
	for line_counter, line_string in enumerate(changed_store_line):
		for every_char in line_string:	
			if (char_counter == 0) and (cursor == 0):
				line_of_cursor = line_counter
				cursor_from_beginning = 0				
			char_counter += 1
			if (char_counter == cursor):
				line_of_cursor = line_counter
				cursor_from_beginning = (cursor - changed_begin_end_count[line_of_cursor][0])
				position_from_end = (changed_begin_end_count[line_of_cursor][1] - cursor)
	return line_of_cursor,cursor_from_beginning,position_from_end

	
def print_current_state(cursor):
	char_counter = 0
	line_of_cursor = -11111111
	cursor_from_beginning = 0
	
	global changed_begin_end_count 
	global changed_store_line 
	global previous_position
	
	for line_counter, line_string in enumerate(changed_store_line):
		'''for every_char in line_string:						
			char_counter += 1
			if char_counter == cursor:
				line_of_cursor = line_counter
				cursor_from_beginning = (cursor - changed_begin_end_count[line_of_cursor][0])'''
		print_line = line_string + " |"+ str(changed_begin_end_count[line_counter][0])+":"+ str(changed_begin_end_count[line_counter][1]) +"|"
		print ("%s"%str(print_line))
		line_of_cursor = find_line_and_cursor_from_beginning(cursor)[0]
		cursor_from_beginning = find_line_and_cursor_from_beginning(cursor)[1]
		
		if line_counter == line_of_cursor:
			#print ("cursor_from_beginning%s, Line cursor%s" %(cursor_from_beginning,line_of_cursor))
			this_line = (" "*(cursor_from_beginning)) + "^"
			print ("%s"%str(this_line))

	#print line_of_cursor; print cursor_from_beginning
    #print cursor_from_beginning	
	
def erase_function(no_of_places):
	global changed_begin_end_count 
	global changed_store_line
	global previous_position
	int_no_of_places = int(no_of_places)
	line_number = find_line_and_cursor_from_beginning(previous_position)[0]
	position_from_beginning_of_line = find_line_and_cursor_from_beginning(previous_position)[1]	
	position_from_end = find_line_and_cursor_from_beginning(previous_position)[2]
	char_end = 0
	char_begin = 0
	line_in_consideration = changed_store_line[line_number]
	line = ""
	if int_no_of_places == 1:
		char_count = 0
		for char_in in line_in_consideration:
			char_count += 1
			if (position_from_beginning_of_line == 0) and (char_count == 1):
				continue
			
			if char_count == position_from_beginning_of_line:
				continue
			line += char_in
		changed_store_line[line_number]	= line
	elif int_no_of_places>=position_from_end:
		diff = (int_no_of_places -position_from_end)
		if diff == 0:
				del changed_store_line[line_number]  
		elif len(changed_store_line[line_number]) <= int_no_of_places:
				del changed_store_line[line_number]				
		else:
			line_reverse = line_in_consideration[::-1]
			line = line_reverse[diff:]
			changed_store_line[line_number] = line[::-1]
			#pass
			#changed_store_line[line_number] = changed_store_line[line_number]
	else:
		diff = (position_from_end-int_no_of_places)
		changed_store_line[line_number] = line_in_consideration[diff:]
	
	
	char_end = 0
	char_begin = 0
	for line_no,line in enumerate(changed_store_line):
		char_end += len(line)  
		changed_begin_end_count[line_no] = (char_begin,char_end)
		#print changed_begin_end_count
		char_begin = char_end + 1	
	print_current_state(previous_position)
	#pass
	#changed_store_line[line_number] = changed_store_line[line_number][0:position_from_beginning_of_line] + inp_str + changed_store_line[line_number][(position_from_beginning_of_line):]
	
def insert_string_function(inp_str):
	global changed_begin_end_count 
	global changed_store_line
	global previous_position
	length_of_string = len(inp_str)	
	
	line_number = find_line_and_cursor_from_beginning(previous_position)[0]
	position_from_beginning_of_line = find_line_and_cursor_from_beginning(previous_position)[1]
	
	#print ("%d"%line_number)
	#print ("%d" %position_from_beginning_of_line)
	char_end = 0
	char_begin = 0
	
	#print changed_store_line[line_number]
	changed_store_line[line_number] = changed_store_line[line_number][0:position_from_beginning_of_line] + inp_str + changed_store_line[line_number][(position_from_beginning_of_line):]
	#print changed_store_line[line_number]
	for line_number,line in enumerate(changed_store_line):
			char_end += len(line)  
			changed_begin_end_count[line_number] = (char_begin,char_end)
			#print changed_begin_end_count
			char_begin = char_end + 1
	print_current_state(previous_position)
		
		


def move_position(position):
	global previous_position	
	if (float(position).is_integer() == False) or (int(position) > changed_begin_end_count[-1][1]) or (int(position) < 0):
		print ("Error in position, earlier session restored")
		
	else:
		previous_position = int(position)
	print_current_state(previous_position)
	#return previous_position


def save_file(final_file_name):
	global changed_begin_end_count 
	global changed_store_line
	global previous_position
	
	with open(final_file_name,'w+') as outputFile:
		for line in changed_store_line:
			outputFile.write(line)
			outputFile.write("\n")
			
	outputFile.close()
	
	
def open_file(file_name):
	global changed_begin_end_count 
	global changed_store_line
	global previous_position
	# Open the file
	with open(file_name,'r') as inputFile:
			char_begin = 0
			char_end = 0
			
			for line in inputFile.readlines():
				line_strip = line.strip()		
				char_end += len(line_strip)
				char_begin_end_count.append((char_begin,char_end))
				print_line = line + " |"+ str(char_begin)+":"+ str(char_end) +"|"
				#begin_end = "|"+ str(char_begin)+":"+ str(char_end) +"|"
				print ("%s"%str(print_line))
				if char_begin == 0:
					print ("^")
				#print ("%s"%line),
				#print ("%s"%begin_end)
				
				
				char_begin = char_end + 1	
				store_line.append(line_strip)
				previous_position = 0
				
				
	inputFile.close()
	changed_store_line = store_line
	changed_begin_end_count = char_begin_end_count
	#print changed_begin_end_count[-1][1]

def main():
    # Change this line so you get the data from a file (ask Mickey).
    #f = open("example.txt")
    #data = f.read()
	global previous_position
	print ("Welcome to the CS1064 Text Editor.")
	first_input = raw_input(">")
	first_input_str = str(first_input)

	
	flag = True			
	while flag is True:
			shift_strip = first_input_str.strip()
			shift_split = shift_strip.split()
			first_part = shift_split[0] #function which you need to perform
			if first_part == "open":
				second_part = shift_split[1] 
				open_file(second_part)
			elif first_part == "move":
				second_part = shift_split[1] 
				move_position(second_part)
			elif first_part == "insert":
				input_string = ""
				for k in shift_split[1:]:
					input_string = input_string + k + " "
				input_string_strip = input_string.strip()
				insert_string_function(input_string_strip)
				#print input_string_strip
			elif (first_part == "saveas"):
				if len(shift_split) > 2:
					print "File Name Error cannot have file with spaces"				
				else:
					modified_file_name = shift_split[1]
					save_file(modified_file_name)
					flag = False
					# If it has to quit the entire thing, just put flag = False break
			elif (first_part == "erase"):
				
				if len(shift_split) > 2:
					print "Cannot be more than one number or wrong input type"
				elif len(shift_split) == 1:
					erase_function(1)
				elif float(shift_split[1]).is_integer() is False:
					print "wrong input type"
				else:
					erase_function(shift_split[1])
			elif (first_part == "quit"):
				quit_signal = raw_input("Would you like to save before you exit? (Y/N):")
				if quit_signal == 'Y':
					file_name_to_be_saved = raw_input("Enter File Name:")
					save_file(file_name_to_be_saved)
				flag = False
				break	
			else:
				print "That's not an editor command."
				print_current_state(previous_position)
			#print (store_line)
			first_input = raw_input(">")
			first_input_str = str(first_input)		




    #file_data = "Abbott: You throw the ball to first base.\nCostello: Then who gets it?\nAbbott: Naturally.\nCostello: Naturally."
    #cursor = 0
    #is_open = False
    #is_modified = False

    #print_file(file_data, cursor)

if __name__ == "__main__":
    main()
