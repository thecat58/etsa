# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agendamiento(models.Model):
    hora = models.IntegerField(primary_key=True, db_comment='guarda la hora de la cita \n')
    lugar = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda la ubicacion de la cita ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='guarda el nombre de quien cita ')

    class Meta:
        managed = True
        db_table = 'agendamiento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona')
    servicio_idservicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='servicio_idservicio')

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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


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
    idpersona = models.AutoField(primary_key=True, db_comment='guarda  identificando individualmente el registro de cada persona.\n')
    nombre = models.CharField(max_length=45, db_comment='guarda el nombre del usuario ')
    apellido = models.CharField(max_length=45, db_comment='guarda el apellido del usuario')
    telefono = models.CharField(max_length=45, db_comment='guardara el contacto del usuario ')
    correo = models.CharField(max_length=45, db_comment='guardara el correo del usuario')
