from faker import Faker
import random

fake = Faker()

with open("usuarios.txt", "w") as f:
    for i in range(10000):
        cui = str(random.randint(1000000000000, 9999999999999))
        nombre_completo = fake.name().replace(',', '')
        centro_de_votacion = fake.address().replace(',', '').replace('\n', '')
        departamento = fake.city().replace(',', '')
        municipio = fake.state().replace(',', '')
        f.write("{},{},{},{},{}\n".format(cui, nombre_completo, centro_de_votacion, departamento, municipio))
