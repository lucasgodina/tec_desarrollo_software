# Escribir un programa que pregunte el
# correo electrónico del usuario en la
# consola y muestre por pantalla otro
# correo electrónico con el mismo
# nombre (la parte delante de la arroba
# @) pero con dominio crui.edu
mail = input("Ingrese su mail: ")
print(mail.split("@")[0] + "@crui.edu")
