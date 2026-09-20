from conexion import conectar


def obtener_todas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tareas")
    listado = cursor.fetchall()
    conexion.close()
    return listado

def obtener_por_prioridad(prioridad):
     conexion = conectar()
     cursor = conexion.cursor()
     cursor.execute(
            "SELECT * FROM tareas WHERE prioridad = %s",
            (prioridad,)
            )
     tarea_prioridad = cursor.fetchall()
     conexion.close()
     return tarea_prioridad

def obtener_por_id(id):
     conexion=conectar()
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM tareas WHERE id = %s",
                            (id,))
     tarea_buscada = cursor.fetchone()
     conexion.close()
     return tarea_buscada
def crear_tarea(tarea):
     conexion = conectar()
     cursor = conexion.cursor()
     cursor.execute("INSERT INTO tareas (titulo, prioridad) VALUES(%s,%s) RETURNING *",
                    (tarea.titulo, tarea.prioridad,)                            )
     nueva_tarea = cursor.fetchone()
     conexion.commit()
     conexion.close()
     return nueva_tarea
def actualizar_tarea(id, titulo, prioridad):
     conexion = conectar()
     cursor = conexion.cursor()
     cursor.execute( "UPDATE tareas SET titulo = %s, prioridad = %s WHERE id = %s RETURNING *",
                        (titulo,prioridad,id)
             )
     tareaactualizada = cursor.fetchone()
     conexion.commit()
     conexion.close()
     return tareaactualizada
def eliminar_tarea(id):
     conexion = conectar()
     cursor = conexion.cursor()
     cursor.execute("DELETE FROM tareas WHERE id = %s RETURNING *",
                                    (id,))
     tarea_borrada = cursor.fetchone()
     conexion.commit()
     conexion.close()
     return tarea_borrada