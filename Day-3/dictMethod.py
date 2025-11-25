info = {
    "name": "Md Adnan",
    "cgpa": 8.4,
    "subjects":["math", "science"]
    
}

dict_keys = info.keys()
dict_vals = list(info.values())

# info["cgpa"] = 8.7

# print(dict_keys)
# print(dict_vals)
# print(info)
# print(type(info))
# print(info["name"])
# print(info["cgpa"])
# print(info.items)

# print(info.get("cgpa2")) # wrong key

# print("End of code")

info.update({
    "city" : "Cheenai"
})

print(info)