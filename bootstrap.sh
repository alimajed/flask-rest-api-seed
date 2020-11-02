#!/bin/sh
export FLASK_APP=app
export FLASK_ENV=development

case $1 in 
    init)
            flask db init
        ;;
    migrate)
            flask db migrate
        ;;
    upgrade)
            flask db upgrade
        ;;
    *)
            flask run
        ;;
esac