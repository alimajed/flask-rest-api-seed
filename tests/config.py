import pytest

from app import create_app, db


@pytest.fixture(scope="module")
def app_inst():
    app = create_app()
    app.app_context().push()
    db.create_all()
    yield app
    
    db.session.remove()
    db.drop_all()
