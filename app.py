def adventure_begin():
     print("\n\n\nTHE ADVENTURE BEINGS....\n\n\n") #\n is one line break
     
     begin_options = ["Option 1", "Option 2", "Option 3"]
     begin_message = "\n - ".join(begin_options) #join takes an array/list and joins each object together with an 'opperator' in this case its a dash and a line break to format it in the console. This turns it from a list into a string.
     begin_message = " - " + begin_message # adds a dash to the first item as the join only adds a dash between two items, not at the start
     begin_input = input(f"Pick from the following: \n\n{begin_message} \n\nEnter Here:")
     begin_input = begin_input.strip() #remove any spacing from this
     
     try:
          begin_picked_interger = int(begin_input) #we 'try' to convert the input into a integer
          begin_picked_interger = (begin_picked_interger - 1) #this takes our input and takes 1 from the answer 1 becomes 0. This is because arrays/lists have an index that starts with 0 instead of 1 and our list of options asks for 1 - 3.
          begin_picked_item = begin_options[begin_picked_interger] #use the integer to try and get the item in the list we want. All list/array items have an index starting with 0, so 1 would be 'Option 2'. If it's out of bounds, it will fail in the except
          
          adventure_step("first_question", begin_options, begin_picked_interger)
          
     except:
          print("You god dam fool, that isn't an option.\n\n")



#step can be the name of the chapter/question
#options is the list of options
#integer is the input that we converted to an integer
def adventure_step(step:str, options:[str], index:int):
     if step == "first_question":
          if index == 1: 
               print(f"Alright you are ready {options[index]}") #in line 12 we already checked if the index is valid and in range, so this will never fail and always return a string.
               
          else:
               print(f"{options[index]} Is a lame option.")
               adventure_begin() #can restart the journey here

     elif step == "second_question":
          print("Th second question logic goes here...")

     else:
          print("To be added")


#python code executes first function once it's stored all references of the other functions above in mememory
adventure_begin()