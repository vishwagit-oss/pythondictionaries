# two ways to create a dictionary

new_dict1 = {}
new_dict2 = dict()

#print(new_dict1)
#print(new_dict2)

textbook_dict = {
  "textbook1" : {
    "id" : "1",
    "title" : "network programmability and automation",
	"author" : "Jason Adalman",
	"year" : 2004,
	"awards" : ["globe", "star", "gold"]
  },
  "textbook2" : {
    "id" : "2",
    "title" : "automation made simple",
	"author": "Gaurav Narula",
	"year": 2016,
	"awards":["star"]
  },
  "textbook3" : {
    "id" : "3",
    "title" : "practical ansible",
	"author": "Oluwole Kayoke",
	"year": 2022,
	"awards":["redhat"]
  },
  "textbook4" : {
    "id" : "4",
    "title" : "python for network scripting",
	"author": "Daisy Chan",
	"year": 2019,
	"awards":["star"]
  },
  "textbook5" : {
    "id" : "5",
    "title" : "containers in action",
	"author": "Alan D'Sousa",
	"year": 2017,
	"awards":["DS3"]
  }
}

# a dictionary is made of a bunch of key:value pairs. The key almost always is a string, and the value take data structure (integer, string, float, list, tuple, dictionary)
# in the example dictionary above, we have textbookx that have a value of type dictionary
# and within each textbook entry we have a dictionary of attributes of a bunch of textbooks
# if we want the information for textbook 2, we would

#print(textbook_dict["textbook1"])

# this prints the value associated with the "textbook1" key, notice it is a dictionary
#print(textbook_dict["textbook1"]["title"])

# now if we wanted to access the "title" key, the output is a string; and "awards" is a list, that means we apply string and list methods to those items

#print(type(textbook_dict["textbook1"]["title"]))
#print(type(textbook_dict["textbook1"]["awards"]))
#print(textbook_dict["textbook1"]["title"].upper())
#print(textbook_dict["textbook1"]["awards"][1])
#textbook_dict["textbook1"]["awards"].append("world")
#print(textbook_dict["textbook1"]["awards"])

#### add a new award names topstar to textbook4
textbook_dict["textbook4"]["awards"].append("topstar")

#### commit changes to main
print(textbook_dict["textbook4"]["awards"])

#there are two ways to get a value associated with a key (like above), or by using the get methods
#print(textbook_dict["textbook1"])
#print(textbook_dict.get("textbook1"))


#what is the difference between the two ways? Check using the code below
#print(textbook_dict["textbook7"])
#print(textbook_dict.get("textbook7"))

#let's add a new entry into the dictionary
textbook6_dict = {
    "id" : "6",
    "title" : "python in motion",
	"author" : "Kelsey Andretti",
	"year" : 2013,
}

textbook_dict['textbook6'] = textbook6_dict
#print(textbook_dict)

# ooops, we forgot to all of the awards that this has received
textbook_dict['textbook6']["awards"] = ["globe", "gold"]
#print(textbook_dict)

# what keys are available
#print (textbook_dict.keys())


#print(textbook_dict.values())
#print(textbook_dict['textbook5'].values())

#if "textbook6" in textbook_dict:
#  print("Yes, 'textbook6' is one of the keys in the textbook_dict dictionary")
#if "awards" in textbook_dict['textbook6']:
#  print("Yes, 'awards' is one of the keys in the textbook_dict dictionary")
#if "globe" in textbook_dict['textbook6']['awards']:
#  print("Yes, 'globe' is one of the awards in the awards list")



#for key in textbook_dict:
#    print(key)
#for key in textbook_dict['textbook2']:
#    print(key)


# two different ways to print values of a dictionary
#for key in textbook_dict['textbook1']:
#    print(textbook_dict['textbook1'][key])
#for value in textbook_dict['textbook1'].values():
#    print(value)

# accessing both the key and value in the same statement
#for key,value in textbook_dict['textbook4'].items():
#    print (f"for textbook4: the {key} key has a value of {value}")
#    if key is 'author':
#        print(textbook_dict['textbook4']['author'])


#### using one of the dictionary methods, change the author of textbook3 to Kloey Twistar 
textbook_dict["textbook3"].update({"author": "Kloey Twistar"})
#### commit changes to main

#### find out if "Kevin Ramdas" is an author of one of the books
kevin_ramdas_author = any(textbook["author"] == "Kevin Ramdas" for textbook in textbook_dict.values())

#### find out if "jason adalman" is an author of one of the books
jason_adalman_author = any(textbook["author"].lower() == "jason adalman" for textbook in textbook_dict.values())

print("Is 'Kevin Ramdas' an author of one of the books? ", kevin_ramdas_author)
print("Is 'Jason Adalman' an author of one of the books? ", jason_adalman_author)
#### oops, Kloey Twistar is not actually the author of textbook3, maybe we should go back in time to the previous commit 


pages_list = [120, 243, 78, 94, 552, 188]
cntr = 0 
# used as the index for pages_list
#### for each of the textbooks in textbook_dict add a new key called pages with the respective value of pages_list

#### commit changes to main