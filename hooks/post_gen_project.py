import os
import shutil

REMOVE_PATHS = [
    '{% if not cookiecutter.type == "starlette" %} examples/demo.py {% endif %}',
    '{% if not cookiecutter.type == "starlette" %} examples/templates/ {% endif %}',
    '{% if not cookiecutter.type == "starlette" %} .idea/runConfigurations/uvicorn_server.xml {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)

os.rename('.gitignore.template', '.gitignore')
