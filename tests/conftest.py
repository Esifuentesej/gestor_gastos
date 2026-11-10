import os
import tempfile
import pytest
from app import app, init_db

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app.config['DATABASE'] = db_path
    app.config['TESTING'] = True
    
    with app.app_context():
        init_db()
        
    with app.test_client() as client:
        yield client

    # Cerramos el descriptor de archivo de forma segura antes de intentar borrarlo
    try:
        os.close(db_fd)
        if os.path.exists(db_path):
            os.unlink(db_path)
    except OSError:
        pass
