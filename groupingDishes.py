#groupingDishes
'''
You are given a list dishes, where each element consists of a list of 
strings beginning with the name of the dish, followed by all the ingredients
used in preparing it. You want to group the dishes by ingredients,
so that for each ingredient you'll be able to find all the dishes that 
contain it (if there are at least 2 such dishes).
'''
#input:
dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

#Expected output:
expected = [["Cheese", "Quesadilla", "Sandwich"],
            ["Salad", "Salad", "Sandwich"],
            ["Sauce", "Pizza", "Quesadilla", "Salad"],
            ["Tomato", "Pizza", "Salad", "Sandwich"]]
#code:
d={}
for dish,*ingredientes in dishes: #create a dict with the ingredients as key
    for i in ingredientes:
        d[i] = d.get(i,[]) +[dish]

d= {k:v for k,v in d.items() if len(v)>=2} #rewrite the dict deleting the once that has list<2

lista = [] # final output list
for i in d:
    lista.append([i]+sorted(d[i])) # append and sort ingredients

lista.sort() #sort by dish

for i in lista: # just print the output
    print(i)


#in a method
'''
def groupingDishes(dishes):
    d={}
    for dish,*ingredientes in dishes: #create a dict with the ingredients as key
        for i in ingredientes:
            d[i] = d.get(i,[]) +[dish]

    d= {k:v for k,v in d.items() if len(v)>=2} #rewrite the dict deleting the once that has list<2

    lista = [] # final output list
    for i in d:
        lista.append([i]+sorted(d[i])) # append and sort ingredients

    lista.sort() #sort by dish
    return lista
    
'''    
