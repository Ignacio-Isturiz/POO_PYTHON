from .entities.usuario import Usuario
from sqlalchemy import text

class ModelUsuario:
    
    @classmethod
    def consultarUsuario(cls, db, usuario):
        query = text("""
            SELECT username
            FROM usuario
            WHERE username = :usuario
        """)
        
        resultado = db.session.execute(query, {'usuario': usuario}).fetchone()
        return resultado
