heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# Q1 Length of the list
print("Total numbers of heros are: ", len(heros))

# Q2 Add 'black panther' at the end of this list
heros.append("black panther")
print("New hero added!: ", heros)

# Q3 You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
heros.insert(3, 'black panther')
print(heros)

# Q4 Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).Do that with one line of code.
heros[1:3]=["doctor strange"]
print(heros)

# Q5 Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)
