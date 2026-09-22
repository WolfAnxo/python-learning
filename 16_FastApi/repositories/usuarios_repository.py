def crear_usuario(username, password_hash, conexion):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (username, password_hash) VALUES (%s,%s) RETURNING *", (username, password_hash))
    usuario = cursor.fetchone()
    conexion.commit()
    return usuario

def obtener_por_username(username, conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
    perfil_usuario =cursor.fetchone()
    return perfil_usuario