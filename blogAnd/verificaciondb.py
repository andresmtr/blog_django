import pandas as pd
import sqlite3
from .models import Post,Categoria,RedesSociales,Web, Autor

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("db.sqlite3")
df = pd.read_sql_query("SELECT * from base_categoria", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head(9))

con.close()


def generarCategoria(request,nombre_categoria):
    posts = Post.objects.filter(
                        estado = True,
                        publicado = True,
                        categoria = Categoria.objects.get(nombre = nombre_categoria)
                        )
    try:
        categoria = Categoria.objects.get(nombre = nombre_categoria)
    except:
        categoria = None

    paginator = Paginator(posts,3)
    pagina = request.GET.get('page')
    posts = paginator.get_page(pagina)
    contexto = {
        'posts':posts,
        'sociales':obtenerRedes(),
        'web':obtenerWeb(),
        'categoria':categoria,
    }
    return contexto
    print(contexto)