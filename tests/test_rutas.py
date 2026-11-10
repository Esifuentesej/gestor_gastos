def test_ruta_inicio_anonimo(client):
    r = client.get('/')
    assert r.status_code == 200

def test_login_correcto(client):
    r = client.post('/login', data={'usuario': 'admin', 'clave': '123'})
    # Redirige exitosamente al panel
    assert r.status_code == 302
    assert '/panel' in r.headers['Location']

def test_login_incorrecto(client):
    r = client.post('/login', data={'usuario': 'admin', 'clave': 'error'})
    # Redirige de vuelta al inicio
    assert r.status_code == 302
    assert '/' in r.headers['Location']

def test_acceso_protegido_sin_sesion(client):
    r = client.get('/panel')
    # Protege la ruta redirigiendo al login
    assert r.status_code == 302

