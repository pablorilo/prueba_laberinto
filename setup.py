from setuptools import setup, find_packages

# Lee el contenido del archivo README.md para usarlo como descripción larga del proyecto
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Lee las dependencias del archivo requirements.txt
with open('requirements.txt', 'r', encoding='utf-8') as f:
    install_requires = f.read().splitlines()

setup(
    name='nombre_del_proyecto',
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires,
    author='Pablo Rilo',
    author_email='prilom@hotmail.com',
    description='App que busca la ruta mas corta para salir de un laberinto',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pablorilo/prueba_laberinto',  # Reemplaza con la URL de tu repositorio en GitHub
   
)
