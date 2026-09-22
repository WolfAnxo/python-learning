def obtener_todas(conexion, usuario_id):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas WHERE usuario_id = %s", (usuario_id,))
    listado = cursor.fetchall()
    return listado

def obtener_por_prioridad(prioridad, conexion, usuario_id):
     cursor = conexion.cursor()
     cursor.execute(
            "SELECT * FROM tareas WHERE prioridad = %s AND usuario_id = %s",
            (prioridad,usuario_id,)
            )
     tarea_prioridad = cursor.fetchall()
     return tarea_prioridad

def obtener_por_id(id, conexion, usuario_id):
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM tareas WHERE id = %s AND usuario_id = %s",
                            (id,usuario_id,))
     tarea_buscada = cursor.fetchone()
     return tarea_buscada
def crear_tarea(tarea,usuario_id, conexion):
     cursor = conexion.cursor()
     cursor.execute("INSERT INTO tareas (titulo, prioridad,usuario_id) VALUES(%s,%s,%s) RETURNING *",
                    (tarea.titulo, tarea.prioridad,usuario_id)                            )
     nueva_tarea = cursor.fetchone()
     conexion.commit()
     return nueva_tarea
def actualizar_tarea(id, titulo, prioridad, conexion, usuario_id):
     cursor = conexion.cursor()
     cursor.execute( "UPDATE tareas SET titulo = %s, prioridad = %s WHERE id = %s AND usuario_id = %s RETURNING *",
                        (titulo,prioridad,id, usuario_id)
             )
     tareaactualizada = cursor.fetchone()
     conexion.commit()
     return tareaactualizada
def eliminar_tarea(id, conexion,usuario_id):
     cursor = conexion.cursor()
     cursor.execute("DELETE FROM tareas WHERE id = %s AND usuario_id = %s RETURNING *",
                                    (id,usuario_id))
     tarea_borrada = cursor.fetchone()
     conexion.commit()
     return tarea_borrada