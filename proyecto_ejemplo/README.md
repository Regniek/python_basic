Creando un ambiente virtual con VENV
Creación de ambiente Virtual:

python3 -m venv nombre_venv

Usualmente el nombre del ambiente virtual es venv.
Activación del ambiente virtual:

Windows:
.\venv\Scripts\activate

Unix o MacOS:
source venv/bin/activate

Desactivar el ambiente virtual:

deactivate

Crear un alias en linux/mac:

alias nombre-alias="comando"

`alias avenv=“source venv/bin/activate”``


pip freeze --> revisar los modulos ya instalados

pip install <nombre_modulo> --> asi se instala cualquier modulo con pip

pip freeze > requirements.txt --> guarda dependencias como crear un package o un gemfile

pip install -r requirements.txt --> como utilizar un bundle instal o npm install

otra manejador posible para usar penv