l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = abroad.difference(friends)
print(local_friends)