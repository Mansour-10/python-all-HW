""" Perform acces list , change list , add list and remove list methods data """


# acces list 
week = ["Saturday", "Sunday", "Monday", "Friday"]

print(week[0])

week = ["Saturday", "Sunday", "Monday", "Friday"]

print(week[1:3])

week = ["Saturday", "Sunday", "Monday", "Friday"]

print(week[-2])

week = ["Saturday", "Sunday", "Monday", "Friday"]

print(week[0:3])

# change list

provinces = ["JLD", "MZR", "QDR", "HRT", "NGR", "PKT"]
provinces [2:5] = ["KBL", "SMN"]
print(provinces)

# add list
provinces = ["JLD", "MZR", "QDR", "HRT", "NGR", "PKT"]
provinces.append("NOR")
print(provinces)

# remove list
provinces = ["JLD", "MZR", "QDR", "HRT", "NGR", "PKT"]
provinces.remove("PKT")
print(provinces)