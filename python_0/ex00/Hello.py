ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# ft_list : Tableau avec changement du deuxieme element du tableau
ft_list[1] = "World!"

# ft_tuple : Tableau immuable donc non modifiable on recup le premier elem et on cree le deuxieme
ft_tuple = (ft_tuple[0], "France!")

# ft_set : Tableau avec objet muables cependant impossible de modifier un objet donc ajout et suppression OK
ft_set.add("Perpignan!")
ft_set.remove("tutu!")

# ft_dict : Tableau avec une cle et une valeur, possible changement valeur en mentionnant la cle
ft_dict ["Hello"] = "42PerpignanOccitanie!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)