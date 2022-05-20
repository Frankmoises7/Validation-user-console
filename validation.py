import re

email_defect = 'frank@mail.com'
password_defect = '12345'
credencials = False

asteriscos = '*' * 10

def validate_email(email):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, email)

print(asteriscos, "Bienvenido", asteriscos)
while not credencials:
    email_input = input("Ingrese su email: \n")
    password_input = input("Ingrese su contraseña: \n")

    if validate_email(email_input):
        if email_defect == email_input and password_defect == password_input:
            print(f'Credenciales Validas.\nBienvenido {email_input}')
            credencials = True
        else:
            print('Credenciales Invalidas\n')
    else:
        print('Credenciales Invalidas\n')
