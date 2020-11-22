export FLASK_APP=app
export FLASK_ENV=docker
export FLASK_RUN_PORT=5000

flask db upgrade
flask run --host=0.0.0.0