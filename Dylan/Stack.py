#Book Stack
cn1 = ["In The Deep Blue Ocean", "The Stranger", "Polly wants a cracker"]
cn2 = ["The Secret of Monkey Island"]
cn3 = ["A Good Leader Is A Good Servant", "The Quest Of Rosetta", "Le Chuck's Revenge"]
cn4 = ["The Bloody Hell Mary", "The Lost Necklace", "The Magical Season Of Christmas"]
cn5 = ["Sherlock Holmes", "Graduation Day"]

#Remove Graduation and Sherlock and put graduation
cn5.pop()
cn5.pop()
cn5.append("Graduation Day")

#Put Sherlock 4th bottom
cn4.pop()
cn4.pop()
cn4.pop()
cn4.append("Sherlock Holmes")
cn4.append("The Bloody Hell Mary")
cn4.append("The Magical Season Of Christmas")

#Put Lost necklace 1st bottom
cn1.pop()
cn1.pop()
cn1.pop()
cn1.append("The Lost Necklace")
cn1.append("In The Deep Blue Ocean")
cn1.append("Polly wants a cracker")

#Put Stranger 2nd top
cn2.append("The Stranger")

print(cn1)
print(cn2)
print(cn3)
print(cn4)
print(cn5)