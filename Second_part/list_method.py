# Metodos importantes:
# .count(<elem>): permite contar cuantos elementos hay en una lista
# .extend(<list>): permite extender una lista, agregando elementos de otra lista
# .pop(): elimina y retorna un elemento de una lista
# .reverse(): cambia al inverso el orden actual de la lista
# .sort(): ordena la lista en un orden especifico, ascendente o descendente


# Selecciona el valor final de la lista

a = [3, 4, 5, 8]

a.pop()
# Si no le pasamos ningun numero de index de la lista por defecto nos elimina el ultimo elemento

a.reverse()
a.extend([2, 1, 0])

print(a)
