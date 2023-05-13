# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agendamiento(models.Model):
    hora = models.IntegerField(primary_key=True, db_comment='guarda la hora de la cita \n')
    lugar = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda la ubicacion de la cita ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre de quien cita ')

    class Meta:
        managed = True
        db_table = 'agendamiento'


class Cateserv(models.Model):
    idcateserv = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cateserv'


class Contrato(models.Model):
    idcontrato = models.IntegerField(primary_key=True, db_comment='guarda registro de contrato que realiza la empresa ')
    descripcion = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda los terminos y condiciones de cada contrato ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre del contrato ')
    servicio_idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_idservicio')
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = True
        db_table = 'contrato'


class Ctaller(models.Model):
    ctaller = models.IntegerField(primary_key=True, db_comment='guarda el registro de cada taller ')
    descripcion = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el servicio que a prestar ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre de cada taller ')

    class Meta:
        managed = True
        db_table = 'ctaller'


class Cuerpo(models.Model):
    idcuerpo = models.IntegerField(primary_key=True)
    idcabeza = models.CharField(max_length=45, blank=True, null=True)
    cantidad = models.CharField(max_length=45, blank=True, null=True)
    valorunitariol = models.CharField(max_length=45, blank=True, null=True)
    valortotal = models.CharField(max_length=45, blank=True, null=True)
    factcabeza_idfactura = models.ForeignKey('Factcabeza', models.DO_NOTHING, db_column='factcabeza_idfactura')
    scripcion_idscripcion = models.ForeignKey('Scripcion', models.DO_NOTHING, db_column='scripcion_idscripcion')

    class Meta:
        managed = True
        db_table = 'cuerpo'


class Departamento(models.Model):
    iddepartamento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='municipio_idmunicipio')

    class Meta:
        managed = True
        db_table = 'departamento'


class Empresa(models.Model):
    idempresa = models.IntegerField(primary_key=True, db_comment='guarda el numero de registro de la empresa')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre de la empresa ')
    direccion = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda la direccion de la empresa ')
    telefono = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el contacto de la empresa ')
    correo = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el correo de la empresa ')
    razonsocial = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre juridico de la empresa')
    catgtall = models.ForeignKey(Ctaller, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'empresa'

class Factcabeza(models.Model):
    idfactura = models.IntegerField(primary_key=True, db_comment='guarda registro de factura ')
    cliente = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.CharField(max_length=45, blank=True, null=True)
    valor_unitario = models.CharField(db_column='valor unitario', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    valortotal = models.CharField(max_length=45, blank=True, null=True)
    pagos_tarjetacredito = models.IntegerField()
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')

    class Meta:
        managed = True
        db_table = 'factcabeza'


class Listadoempresaservicio(models.Model):
    idlistadoempresaservicio = models.IntegerField(primary_key=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    servicio_idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_idservicio')

    class Meta:
        managed = True
        db_table = 'listadoempresaservicio'


class Municipio(models.Model):
    idmunicipio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    ciudad_idciudad = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'municipio'


class Persona(models.Model):
    idpersona = models.AutoField(primary_key=True, db_comment='guarda  identificando individualmente el registro de cada persona.\n')  # The composite primary key (idpersona, tipersona_idtipersona, tipersona_idtipersona1) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=45, db_comment='guarda el nombre del usuario ')
    apellido = models.CharField(max_length=45, db_comment='guarda el apellido del usuario')
    telefono = models.CharField(max_length=45, db_comment='guardara el contacto del usuario ')
    correo = models.CharField(max_length=45, db_comment='guardara el correo del usuario')
    contrasena = models.CharField(max_length=45, db_comment='guarda la contrase�a del usuario')
    municipio_idmunicipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='municipio_idmunicipio')
    genero = models.CharField(max_length=45, blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)
    tdoc_idtdoc = models.ForeignKey('Tdoc', models.DO_NOTHING, db_column='tdoc_idtdoc')
    tipersona_idtipersona = models.IntegerField()
    tipersona_idtipersona1 = models.ForeignKey('Tipersona', models.DO_NOTHING, db_column='tipersona_idtipersona1')

    class Meta:
        managed = True
        db_table = 'persona'
        unique_together = (('idpersona', 'tipersona_idtipersona', 'tipersona_idtipersona1'),)


class Pgos(models.Model):
    idpgos = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    factcabeza_idfactura = models.ForeignKey(Factcabeza, models.DO_NOTHING, db_column='factcabeza_idfactura')

    class Meta:
        managed = True
        db_table = 'pgos'


class Planes(models.Model):
    idplanes = models.IntegerField(primary_key=True, db_comment='guarda registro de cada plan \n')
    descripcion = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda las promociones de cada taller \n')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre del plan ')
    servicio_idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_idservicio')

    class Meta:
        managed = True
        db_table = 'planes'


class Scripcion(models.Model):
    idscripcion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    valor = models.CharField(max_length=45, blank=True, null=True)
    fecha = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scripcion'


class Servicio(models.Model):
    idservicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    cateserv_idcateserv = models.ForeignKey(Cateserv, models.DO_NOTHING, db_column='cateserv_idcateserv')

    class Meta:
        managed = True
        db_table = 'servicio'


class Tdoc(models.Model):
    idtdoc = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tdoc'


class Tipersona(models.Model):
    idtipersona = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipersona'