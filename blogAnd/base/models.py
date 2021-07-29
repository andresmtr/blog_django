from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False ,auto_now_add=True)
    fecha_modificacion = models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)
    fecha_eliminacion = models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)

    class  Meta:
        abstract = True

class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la categoria', max_length=100, unique=True)
    imagen_referencial = models.ImageField('Imagen referencial', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(ModeloBase):
    nombre = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=120)
    email = models.EmailField('Correo electronico', max_length=200, unique = True) 
    descripcion = models.TextField('Descripción')
    imagen_referencial = models.ImageField('Imagen referencial', null=True, blank=True, upload_to= 'autores/')
    web = models.URLField('Web', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    github = models.URLField('Github', null=True, blank=True)
    linkedin = models.URLField('Linkedin', null=True, blank=True)

    class  Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0} {1}'.format(self.nombre,self.apellidos)

class Post(ModeloBase):
    titulo = models.CharField('Titlulo del Post', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripción')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField('Imagen referencial', upload_to='imagenes/', max_length=255)
    publicado = models.BooleanField('Publicado / No publicado', default=False)
    fecha_publicacion = models.DateField('Fecha de publicación')

    class  Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

class Web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    email = models.EmailField('Correo Electronico', max_length=200)
    

    class meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros

class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter')
    instagram = models.URLField('Instagram')
    github = models.URLField('Github')
    linkedin = models.URLField('Linkedin')

    class  Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook

class Contacto (ModeloBase):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=150)
    correo = models.EmailField('Correo electronico', max_length=200, unique=True)
    asunto = models.CharField('Asunto', max_length=100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto





