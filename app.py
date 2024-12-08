from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa CORS
import psycopg2

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    'dbname': 'hospital_ejercicio_xyz',
    'user': 'postgres',
    'password': '123456789',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

# Crear un nuevo paciente
@app.route('/api/pacientes', methods=['POST'])
def create_paciente():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Pacientes ( nombre, direccion, telefono, codigo_postal, nif, num_seguridad_social, medico_id )
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING paciente_id;
    """, (        data['nombre'], 
        data['direccion'], 
        data['telefono'], 
        data.get('codigoPostal'), 
        data['nif'], 
        data['numSeguridadSocial'], 
        data['medicoId']
))
    paciente_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'id': paciente_id, 'message': 'Paciente creado exitosamente'}), 201

# Leer todos los pacientes
@app.route('/api/pacientes', methods=['GET'])
def get_pacientes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes;")
    pacientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([
        {
            'paciente_id': p[0],
            'nombre': p[1],
            'direccion': p[2],
            'telefono': p[3],
            'medico_id': p[7],
            'codigo_postal': p[4],
            'nif': p[5],
            'num_seguridad_social': p[6]
        } for p in pacientes
    ])

# Leer un paciente por ID
@app.route('/api/pacientes/<int:id>', methods=['GET'])
def get_paciente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes WHERE paciente_id = %s;", (id,))
    paciente = cursor.fetchone()
    cursor.close()
    conn.close()
    if paciente:
        return jsonify({
            'paciente_id': paciente[0],
            'nombre': paciente[1],
            'direccion': paciente[2],
            'telefono': paciente[3],
            'medico_id': paciente[7],
            'codigo_postal': paciente[4],
            'nif': paciente[5],
            'num_seguridad_social': paciente[6]
        })
    else:
        return jsonify({'error': 'Paciente no encontrado'}), 404

# Obtener empleados que son médicos
@app.route('/api/empleados/medicos', methods=['GET'])
def get_medicos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM empleados WHERE tipo_empleado = 'medico';")
    empleados = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([
        {
            'empleado_id': e[0],
            'nombre': e[1],
            'direccion': e[2],
            'telefono': e[3],
            'tipo_empleado': e[4]
        } for e in empleados
    ])


# Actualizar un paciente
@app.route('/api/pacientes/<int:id>', methods=['PUT'])
def update_paciente(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Pacientes
        SET nombre = %s, direccion = %s, telefono = %s, codigo_postal = %s, nif = %s, num_seguridad_social = %s, medico_id = %s
        WHERE paciente_id = %s;
    """, (data['nombre'], data['direccion'], data['telefono'], data['codigo_postal'], data['nif'], data['num_seguridad_social'], data['medico_id'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Paciente actualizado exitosamente'})

# Eliminar un paciente
@app.route('/api/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pacientes WHERE paciente_id = %s;", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Paciente eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)
