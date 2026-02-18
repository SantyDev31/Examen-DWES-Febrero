from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    
    
    class Meta:
        ordering = ['apellidos', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Publicacion(models.Model):
    TIPO_PUBLICACION = [
        ('libro', 'Libro'),
        ('articulo', 'Artículo'),
    ]
    
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=300)
    autores = models.ManyToManyField(Autor, related_name='publicaciones')
    tipo_publicacion = models.CharField(max_length=10, choices=TIPO_PUBLICACION)
    año_publicacion = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    editorial = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['titulo']
    
    def __str__(self):
        return self.titulo
    
    @property
    def total_unidades(self):
        return self.unidades.count()
    
    @property
    def unidades_disponibles(self):
        return self.unidades.exclude(estado='a_retirar').count()

class Unidad(models.Model):
    ESTADOS_UNIDAD = [
        ('nueva', 'Nueva'),
        ('usada', 'Usada'),
        ('deteriorada', 'Deteriorada'),
        ('retirar', 'A retirar'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_UNIDAD)
    def __str__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(max_length=300)
    FORMATOS = [
        ("VHS" , "VHS"),
        ("CD", "CD"),
        ("DVD", "DVD")
    ]
    formato = models.CharField(max_length=4, choices=FORMATOS)
    año = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    duracion_minutos = models.FloatField()
    genero = models.CharField(max_length=300)
    sinopsis = models.CharField(max_length=300)

    def __str__(self):
            return self.titulo
    
class Disco(models.Model):
    titulo = models.CharField(max_length=300)
    FORMATOS = [
        ("vinilo","Vinilo"),
        ("CD", "CD"),
        ("Cassette", "Cassette")
    ]
    formato = models.CharField(max_length=20, choices=FORMATOS)
    año = models.IntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )
    discografica = models.CharField(max_length= 300)
    num_pistas = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    genero = models.CharField(max_length=300)

    def __str__(self):
            return self.titulo

class Autor_Video (models.Model):
    autor_id = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL) 
    video_id = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL) 
    ROLES = [
         ("Director","Director"),
         ("Guionista","Guionista"),
         ("Guionista","Guionista"),
    ]
    rol = models.CharField(100, choices=ROLES)

class Autor_Disco (models.Model):
    autor_id = models.ForeignKey(Autor, null=True, on_delete=models.SET_NULL) 
    disco_id = models.ForeignKey(Disco, null=True, on_delete=models.SET_NULL) 
    ROLES = [
         ("Artista","Artista"),
         ("Productor","Productor"),
         ("Compositor","Compositor"),
    ]
    rol = models.CharField(100, choices=ROLES)