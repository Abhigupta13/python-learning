# a='''AKG is
# rockx 
# \\_(*_*)_/'''
# b=454
# c=578.47
# d=True
# d= None
# print("the value of 3+4 IS ",3+4)
# e = 14>7;
# print(d)
# print(a)
# print(b)
# print(c)
# print(e)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# b1 = True
# b2 = False
# print("the value of b1 and b2 is ",b1 and b2 )
# print("value of b1 or b2 is ",b1 or b2)
# print("the value of b1 not b2 is ",not b2)
# a1="78"
# a1=int(a1)
# print(a1+4)
# a2 = input("Enter your name ")
# print(a2)
# print(3//4) gives int value
# a="hello my name is AKG "
# # a[0]='d' --> does not work
# print(a[1],a[2],a[6])
# # SLICING 
# print(a[0:3]) #will print from 0 to 3 excluding 3
# print(a[:3]) #same as above one 
# print(a[1:]) #same as print(a[1:19])
# print(a[-5]) #s   minus start from last element -1,-2,-3,-4.......
# c= a[1:6]
# print(c)

# # Slicing with skip
# d=a[1:4:2] 
# # print(d)
# d=a[0::2] #SKIPPING EVERY SECOND ELEMENT
# print(d)

# # String functions
# story="once upon a time there was a youtuber named AKG"
# print(len(story))
# print(story.endswith("iuh")) #jaisa naam waisa kaam / check that whether the string is ending with the provided string
# print(story.endswith("AKG"))
# print(story.count("a"))
# print(story.count("time")) # gives the frequency of the provided word in the string
# print(story.capitalize()) # capatalize the first word of the string
# print(story.find("once")) # -1 shows not present | it will show only about the first occurence of the word in the string
# print(story.replace("AKG","AKG.ROCKX")) # temporary replaces all the occurence
# print(story)
# c=story.replace("AKG","AKG.ROCKX") 
# print(c)

# ESCAPE SEQUENCE 
# a="AKG is good. \nHe \tis very good" #\n,\t are some examples of escape sequence characters
# print(a)
# ~~~~~~~~~~~~~~~~~~~~~~~LISTS AND TUPLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a=[1,2,3,56,8]   # index= 0,1,2,3,4,........
# print(a)
# access using index using a[0],a[1],.....
# print(a[3])
# print(a[5])    # give error
# a[0]=45
# print(a)
        #   &&   we can create a list with items of different types    $$
# b=[23,"akg", True,4.6]
# print(b)

# LIST SLICING
# friends=["umang","akd","dj","asdfgh","com","deva",45]
# print(friends[0:4])
# print(friends[-4:])    #-4,-3,-2,-1

# LIST METHODS
# l1=[1,8,7,2,34,15,21]
# print(l1)
# l1.sort()               # ascending order
# l1.reverse()           #   reverces the list
# l1.append(45)           # adds 45 at the end of the list
# l1.append(90)           # adds 90 at the end of the list
# l1.insert(2,544)        #insert 544 at index 2
# l1.pop(2)               #remove 2nd index element
# l1.remove(15)           #remove 15 from the list
# ~~~~~~~~~~~~~~~~~~search  list methods python docx on google for this~~~~~~~~~~~~~~~~~~~~~~~~~``
# print(l1)

#  Creating a tuple usint ()
# t=(1,2,4,2,1,1,5)
# t1=()   empty tuple
# t1=(1)              # wrong wey to declare a tuple with single element
# t1=(1,)                # tuple with single element
# print(t1)
# printing the elements of tuple
# print(t[0])
# t[0]=23  #error       # cannot update the value of tuple
                    #~~~~~~~~~~~~~~~~~~~~~~~~~~ tuple methods~~~~~~~~~~~~~~~~~~~~~~~~~~``
# print(t.count(1))    # count the occurance
# print(t.index(5))

#``````````````````````````````dictionary & set````````````````````````````
# collection of key value pairs

# mydic={
#     "Fast": "In a Quick manner ",    #  don't forgot comma
#     "Harry": "A Coder",
#     "marks" :[1,2,54,65,3,3],
#     "anotherdic": {"harry": "player"},
#     1:2
# }
# print(mydic['Fast'])
# print(mydic['marks'])
# mydic["marks"]=[23,45,3]           # can change list in dictionary
# print(mydic["anotherdic"])         #  prints>>> {'harry': 'player'}
# print(mydic["anotherdic"]["harry"])         # print>> player
# print(mydic["marks"])                #prints new list

#  ``````````````dictionary methods`````````````
# print(list(mydic.keys()))     # print the kays of dictionary
# print(mydic.values())         # prints the values of dictionary
# print(mydic.items())      #print the (kays,value) for all contents of dictionary
# print(mydic)
# updatedic={
#     "Lovish":"friend",
#     "kjdfk":"uuu",
#     "Harry": "sir"        # updates existing values of keys
# }
# mydic.update(updatedic)   # updates the dictionary by adding key value pairs from updatedic
# print(mydic)

# print(mydic.get("Harry"))    # prints value associated with key "Harry"
# print(mydic["Harry"])         #prints value associated with key "Harry"

# # difference between .get and [ ] syntex in the dictionary?
# print(mydic.get("Harry2"))    # returns None  as Harry2 is not presnt in the dictionary
# print(mydic["Harry2"])         #throws an error as Harry2 is not presnt in the dictionary
  
  # SETS IN PYTHON
# a={1,3,4,5,1}       # collection of non repeatative elements
# print(type(a))
# print(a)
# a={}   #Important : this syntex will create an empty dictionary and not a empty set
# print(type(a))

#An empty set can be created by the below syntex
# b=set()
# # adding values to an empty set
# b.add(4)
# b.add(5)
# b.add(4)        #adding a value repeatatively does not changes a set
# # b.add([4,5,6]) &  b.add({1:2})  # cannot add list or dictionary to sets
# b.add((4,5,6))                    #tuples can be add bcz tuples are unchangable
# print(type(b))
# print(b)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~methods of sets~~~~~~~~~~~~~~~~~~~#
# print(len(b))   #prints the length of this set
# b.remove(5)     #removes 5 from set b
# b.remove(15)    #error bcz 15 is not present in set
# print(b.pop())
# print(b.clear())
# print(b)
# print(b.union({3,7}))
# print(b.intersection({4}))