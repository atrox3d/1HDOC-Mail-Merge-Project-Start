#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

INPUT_LETTER = "input/letters/starting_letter.txt"
INPUT_NAMES = "input/names/invited_names.txt"
OUTPUT_PATH = "output/readytosend"
#
#   read names from input file
#
with open(INPUT_NAMES) as input_names:
    names = input_names.readlines()
#
#   strip \n from name list
#
for _ in range(len(names)):
    names[_] = names[_].strip()
#
#   read template text into variable
#
with open(INPUT_LETTER) as input_letter:
    template = input_letter.read()
print(template)
#
#
#
for name in names:
    output_letter = template.replace("[name]", name)
    output_filename = f"{OUTPUT_PATH}/{name}.txt"
    print(f"creating {output_filename}...")
    with open(output_filename, "w") as letter:
        letter.write(output_letter)
    print("done.")

