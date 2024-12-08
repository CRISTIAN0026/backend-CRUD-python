# backend-CRUD-python
# API de Gestión de Pacientes y Médicos

Esta aplicación es una API REST desarrollada con Flask para gestionar datos de pacientes y empleados (médicos) de un hospital. Incluye operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la base de datos PostgreSQL.

---

## Funcionalidades

### Pacientes
- **Crear paciente**: Agrega un nuevo paciente a la base de datos.
- **Listar pacientes**: Devuelve la lista de todos los pacientes registrados.
- **Obtener paciente por ID**: Devuelve los datos de un paciente específico según su ID.
- **Actualizar paciente**: Modifica los datos de un paciente existente.
- **Eliminar paciente**: Elimina un paciente específico de la base de datos.

### Médicos
- **Listar médicos**: Devuelve una lista de empleados que tienen el rol de médicos.

---

## Requisitos

- **Python** 3.x
- **PostgreSQL** instalado y en ejecución
- Paquetes de Python:
  - Flask
  - Flask-CORS
  - psycopg2

---

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/api-gestion-pacientes.git
   cd api-gestion-pacientes
