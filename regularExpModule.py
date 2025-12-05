# import  re
# text = "my number is 12345 5 and my friend's number is 67890."
# match = re.search(r'\d+', text)
# print("Matched number:", match.group())  # one or more digits
# print(re.findall(r'\d+', text))  # all occurrences of one or more digits
# # res = re.match(r"hi", "hellow word")
# # print(res.gruop())  # entire stringoup()  # entire string

# new_text = re.sub(r'\d+', 'X', text)
# print("After substitution:", new_text)  # replace numbers with 'X'



# email = "swapnil@gmail.com"
# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# if re.match(pattern, email):

#     print("Valid email address")
# else:
#     print("Invalid email address")


# text2 = "The rain in Spain stays mainly in the plain."
# match_obj = re.search(r"bird",text2)
# if match_obj:
#     print("Match found:", match_obj.group())
# else:
#     print("No match found")


text3 = "The quick brown fox jumps over the lazy dog."


for i in text3.split():
    if i == "fox": 
        print(f"'{"fox"}' found in the text.")
        break
    else:
        print(f"'{"fox"}' not found in the text.") 
         
    