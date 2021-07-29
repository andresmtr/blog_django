from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, View, DetailView
from django.core.paginator import Paginator
from .models import Post,Categoria,RedesSociales,Web, Autor
import random
from .forms import ContactoForm

# Create your views here.



def consulta(id):
    try:
        return Post.objects.get(id = id)
    except :
        return None

def obtenerRedes():
    return RedesSociales.objects.filter(
        estado = True,
    ).latest('fecha_creacion')

def obtenerWeb():
    return Web.objects.filter(
        estado = True,
    ).latest('fecha_creacion')

def obtenerAutor():
    return Autor.objects.filter(
        estado = True,
    ).latest('fecha_creacion')

class Inicio(ListView):

    def get (self,request, *args, **kwargs):

        posts = list(Post.objects.filter(
            estado = True,
            publicado = True
            ).values_list('id',flat = True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        Post1 = random.choice(posts)
        posts.remove(Post1)
        Post2 = random.choice(posts)
        posts.remove(Post2)
        Post3 = random.choice(posts)
        posts.remove(Post3)
        Post4 = random.choice(posts)
        posts.remove(Post4)

        try:
            post_ordenadores = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Ordenadores')
                ).latest('fecha_publicacion')
        
        except:

            post_ordenadores = None

        try:
            post_videojuegos = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Videojuegos')
            ).latest('fecha_publicacion')

        except:
            post_videojuegos = None

        try:
            post_programacion = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Programación')
                ).latest('fecha_publicacion')
        
        except:

            post_programacion = None

        try:
            post_apple = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Apple')
            ).latest('fecha_publicacion')

        except:
            post_apple = None


        try:
            post_google = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Google')
                ).latest('fecha_publicacion')
        
        except:

            post_google = None

        try:
            post_microsoft = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Microsoft')
            ).latest('fecha_publicacion')

        except:
            post_microsoft = None


        try:
            post_tutoriales = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Tutoriales')
                ).latest('fecha_publicacion')
        
        except:

            post_tutoriales = None

        try:
            post_tecnologia = Post.objects.filter(
                estado = True,
                publicado = True,
                categoria = Categoria.objects.get(nombre = 'Tecnología')
            ).latest('fecha_publicacion')

        except:
            post_tecnologia = None

        contexto = {
            'principal':principal,
            'post1': consulta(Post1),
            'post2': consulta(Post2),
            'post3': consulta(Post3),
            'post4': consulta(Post4),
            'post_ordenadores': post_ordenadores,
            'post_videojuegos':post_videojuegos,
            'post_programacion':post_programacion,
            'post_apple':post_apple,
            'post_google':post_google,
            'post_microsoft':post_microsoft,
            'post_tutoriales':post_tutoriales,
            'post_tecnologia':post_tecnologia,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'autor':obtenerAutor()
        }

        return render(request, 'index.html', contexto)


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


class Listado(ListView):

    def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        # categoria.html se reemplazara con el nombre de la categoria
        return render(request,'categoria.html',contexto)

class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'contacto.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:index')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto)


class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None


        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))

        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        contexto = {
            # 'categoria':categoria,
            'post':post,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),

        }
        return render(request,'contenido.html',contexto)



