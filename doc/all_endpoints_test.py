import random
import requests
import json

def main():
    url_base = "https://ap2uni9.brunoserrate.repl.co/"
    main_language = "en"

    data_return_key = "data"

    if(main_language == "pt-br"):
        data_return_key = "dados"

    # POST - Registrar usuário
    # url_base/api/users/register
    '''json:
        name,
        email,
        password,
        confirm_password
    '''
    strRandomNumber = random.randint(1, 999).__str__()
    name = "Bruno Serrate " + strRandomNumber
    email = "bruno.serrate_" + strRandomNumber + "@gmail.com"
    password = "123456789"

    register = requests.post(
        url_base + "api/users/register",
        json={
            "name": name,
            "email": email,
            "password": password,
            "confirm_password": password,
        },
        headers={
            "Accept-Language": main_language
        }
    )

    result = json.loads(register.content.decode("utf-8"))

    print("Retorno do registro:\n")
    print(json.dumps(result, indent=4))
    print("\n")

    userId = result[data_return_key]["id"]

    # POST - Login
    # url_base/api/users/login
    '''json:
        email,
        password
    '''
    login = requests.post(
        url_base + "api/users/login",
        json={
            "email": email,
            "password": password,
        },
        headers={
            "Accept-Language": main_language
        }
    )

    result = json.loads(login.content.decode("utf-8"))

    print("Retorno do login:\n")
    print(json.dumps(result, indent=4))
    print("\n")

    token = result[data_return_key]["token"]

    # Get - Password Generator
    # url_base/api/password_generator
    '''
        header: Authorization => token

        json:
            length => int
            samples => int
            useLowerCase => bool
            useUpperCase => bool
            useNumbers => bool
            useSymbols => bool
            useSimilarCharacters => bool
            uniqueCharacters => bool
    '''
    generatePassword = requests.get(
        url_base + "api/password_generator",
        json={
            "length": 20,
            "samples": 20,
            "useSimilarCharacters": True
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(generatePassword.content.decode("utf-8"))

    print("Retorno da(s) senha(s) gerada(s):\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Get - Password Generator 2
    # url_base/api/password_generator
    '''
        header: Authorization => token

        json:
            length => int
            samples => int
            useLowerCase => bool
            useUpperCase => bool
            useNumbers => bool
            useSymbols => bool
            useSimilarCharacters => bool
            uniqueCharacters => bool
    '''
    generatePassword = requests.get(
        url_base + "api/password_generator",
        json={
            "length": 30,
            "samples": 10,
            "useSymbols": True,
            "useSimilarCharacters": True
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(generatePassword.content.decode("utf-8"))

    print("2º retorno da(s) senha(s) gerada(s):\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Get - Random Numbers
    # url_base/api/random_numbers
    '''
        header: Authorization => token

        json:
            min => int
            max => int
            samples => int
            unique => bool
    '''
    randomNumbers = requests.get(
        url_base + "api/random_numbers",
        json={
            "min": 1,
            "max": 1000,
            "samples": 10,
            "unique": True
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(randomNumbers.content.decode("utf-8"))

    print("Retorno do(s) numero(s) gerado(s):\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Get - Random Numbers 2
    # url_base/api/random_numbers
    '''
        header: Authorization => token

        json:
            min => int
            max => int
            samples => int
            unique => bool
    '''
    randomNumbers = requests.get(
        url_base + "api/random_numbers",
        json={
            "min": 1,
            "max": 50,
            "samples": 100
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(randomNumbers.content.decode("utf-8"))

    print("2º retorno do(s) numero(s) gerado(s):\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Get - Unit Converter
    # url_base/api/unit_converter
    '''
        header: Authorization => token

        json:
            type => string
            from => string
            to => string
            value => float
    '''
    unitConverter = requests.get(
        url_base + "api/random_numbers",
        json={
            "type": "temperature",
            "from": "celsius",
            "to": "fahrenheit",
            "value": 30
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(unitConverter.content.decode("utf-8"))

    print("Retorno da conversão de unidade:\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Get - User
    # url_base/api/users/read
    '''
        header: Authorization => token

        json:
            id => int
            name => string
            email => string
            limit => int
    '''
    users = requests.get(
        url_base + "api/users/read",
        json={
            'id': userId,
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(users.content.decode("utf-8"))

    print("Retorno da leitura de usuario(s):\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Get - User
    # url_base/api/users/read
    '''
        header: Authorization => token

        json:
            id => int
            name => string
            email => string
            limit => int
    '''
    users = requests.get(
        url_base + "api/users/read",
        json={
            'name': 'email.inexistente@gmail.com',
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(users.content.decode("utf-8"))

    print("2º retorno da leitura de usuario(s):\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Update - User
    # url_base/api/user/update
    '''
        header: Authorization => token

        json:
            name => string
    '''
    userUpdated = requests.put(
        url_base + "api/users/update",
        json={
            'name': 'Bruno Serrate 2'
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(userUpdated.content.decode("utf-8"))

    print("Retorno da atualização de usuário:\n")
    print(json.dumps(result, indent=4))
    print("\n")

    users = requests.get(
        url_base + "api/users/read",
        json={
            'id': userId,
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(users.content.decode("utf-8"))

    print("Usuário após os dados atualizados:\n")
    print(json.dumps(result, indent=4))
    print("\n")

    # Delete - User
    # url_base/api/user/delete
    '''
        header: Authorization => token

        json:
            id => int
    '''
    userDelete = requests.delete(
        url_base + "api/users/delete",
        json={
            'id': userId
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(userDelete.content.decode("utf-8"))

    print("Retorno da exclusão de usuário:\n")
    print(json.dumps(result, indent=4))
    print("\n")

    users = requests.get(
        url_base + "api/users/read",
        json={
            'id': userId,
        },
        headers={
            "Authorization": token,
            "Accept-Language": main_language
        }
    )

    result = json.loads(users.content.decode("utf-8"))

    print("Usuário após a exclusão:\n")
    print(json.dumps(result, indent=4))
    print("\n")

if __name__ == "__main__":
    main()
