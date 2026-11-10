# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)
app.secret_key = 'clave_secreta_examen_web'

DATABASE = 'gastos.db'

def get_db():
    """Conexion limpia e independiente a la base de datos."""
    db_file = app.config.get('DATABASE', DATABASE)
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Crea la tabla de gastos si no existe."""
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                monto REAL NOT NULL
            )
        ''')
        conn.commit()

def validar_monto(monto_str):
    """Valida que el monto sea un numero mayor a cero."""
    try:
        monto = float(monto_str)
        return monto > 0
    except (ValueError, TypeError):
        return False

@app.route('/')
def inicio():
    if 'usuario' in session:
        return redirect(url_for('panel'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')
    clave = request.form.get('clave')
    
    if usuario == 'admin' and clave == '123':
        session['usuario'] = usuario
        return redirect(url_for('panel'))
    else:
        flash('Credenciales invalidas')
        return redirect(url_for('inicio'))

@app.route('/panel')
def panel():
    if 'usuario' not in session:
        return redirect(url_for('inicio'))
        
    conn = get_db()
    gastos = conn.execute('SELECT * FROM gastos ORDER BY fecha DESC').fetchall()
    conn.close()
    return render_template('panel.html', gastos=gastos)

@app.route('/registrar', methods=['POST'])
def registrar():
    if 'usuario' not in session:
        return redirect(url_for('inicio'))
        
    fecha = request.form.get('fecha')
    descripcion = request.form.get('descripcion')
    monto_str = request.form.get('monto')
    
    if not fecha or not descripcion or not validar_monto(monto_str):
        flash('Datos invalidos o monto incorrecto')
        return redirect(url_for('panel'))
        
    conn = get_db()
    conn.execute('INSERT INTO gastos (fecha, descripcion, monto) VALUES (?, ?, ?)',
                 (fecha, descripcion, float(monto_str)))
    conn.commit()
    conn.close()
    
    flash('Gasto registrado con exito')
    return redirect(url_for('panel'))

@app.route('/reporte/json')
def reporte_json():
    if 'usuario' not in session:
        return jsonify({"error": "No autorizado"}), 401
        
    conn = get_db()
    gastos = conn.execute('SELECT * FROM gastos').fetchall()
    conn.close()
    
    lista_gastos = [dict(gasto) for gasto in gastos]
    total = sum(g['monto'] for g in lista_gastos)
    
    return jsonify({
        "total_gastado": total,
        "cantidad_registros": len(lista_gastos),
        "gastos": lista_gastos
    })

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
