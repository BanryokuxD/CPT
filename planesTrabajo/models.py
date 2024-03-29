# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppcptActividaddocente(models.Model):
    numero_estudiantes = models.IntegerField()
    horas_curso = models.IntegerField()
    tutorias_estudiantes_horas = models.IntegerField()
    preparacion_horas = models.IntegerField()
    evaluacion_horas = models.IntegerField()
    centro_costos = models.ForeignKey('AppcptCentrocostos', models.DO_NOTHING)
    curso = models.ForeignKey('AppcptCurso', models.DO_NOTHING)
    nivel = models.ForeignKey('AppcptNivel', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('AppcptPeriodoacademico', models.DO_NOTHING)
    profesor = models.ForeignKey('AppcptProfesor', models.DO_NOTHING)
    proyecto_curricular = models.ForeignKey('AppcptProyectocurricular', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_actividaddocente'


class AppcptActividadextension(models.Model):
    titulo = models.CharField(max_length=100)
    coidgo = models.IntegerField()
    horas_semanales = models.IntegerField()
    centro_costos = models.ForeignKey('AppcptCentrocostos', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('AppcptPeriodoacademico', models.DO_NOTHING)
    profesor = models.ForeignKey('AppcptProfesor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_actividadextension'


class AppcptActividadgestion(models.Model):
    actividad_gestion = models.IntegerField()
    horas_semana = models.IntegerField()
    centro_costos = models.ForeignKey('AppcptCentrocostos', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('AppcptPeriodoacademico', models.DO_NOTHING)
    profesor = models.ForeignKey('AppcptProfesor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_actividadgestion'


class AppcptActividadinvestigativa(models.Model):
    funcion = models.CharField(max_length=45)
    acta_facultad = models.CharField(max_length=15)
    titulo_proyecto = models.CharField(max_length=200)
    horas_semanales = models.IntegerField()
    centro_costos = models.ForeignKey('AppcptCentrocostos', models.DO_NOTHING)
    nivel = models.ForeignKey('AppcptNivel', models.DO_NOTHING)
    periodo_academico = models.ForeignKey('AppcptPeriodoacademico', models.DO_NOTHING)
    profesor = models.ForeignKey('AppcptProfesor', models.DO_NOTHING)
    proyecto_curricular = models.ForeignKey('AppcptProyectocurricular', models.DO_NOTHING)
    tipo_actividad_investigativa = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appcpt_actividadinvestigativa'


class AppcptCentrocostos(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_centrocostos'


class AppcptCurso(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    codigo = models.IntegerField()
    numero_horas = models.DecimalField(max_digits=20, decimal_places=0)
    nivel = models.CharField(max_length=60)
    proyecto_curricular = models.CharField(max_length=45)
    grupo = models.IntegerField()
    semestre = models.IntegerField()
    estado = models.IntegerField()
    horario = models.CharField(max_length=90)
    departamento = models.ForeignKey('AppcptDepartamento', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_curso'


class AppcptDepartamento(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_departamento'


class AppcptFacultad(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_facultad'


class AppcptNivel(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_nivel'


class AppcptPeriodoacademico(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'appcpt_periodoacademico'


class AppcptProfesor(models.Model):
    id = models.IntegerField(primary_key=True)
    dedicacion = models.IntegerField(blank=True, null=True)
    usuario = models.ForeignKey('AppcptUsuario', models.DO_NOTHING)
    vinculacion = models.ForeignKey('AppcptVinculacion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_profesor'


class AppcptProyectocurricular(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_proyectocurricular'


class AppcptRol(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_rol'


class AppcptUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    cedula = models.CharField(max_length=45)
    departamento = models.ForeignKey(AppcptDepartamento, models.DO_NOTHING, blank=True, null=True)
    facultad = models.ForeignKey(AppcptFacultad, models.DO_NOTHING, blank=True, null=True)
    rol = models.ForeignKey(AppcptRol, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appcpt_usuario'


class AppcptUsuarioGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(AppcptUsuario, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_usuario_groups'
        unique_together = (('usuario', 'group'),)


class AppcptUsuarioUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(AppcptUsuario, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'appcpt_usuario_user_permissions'
        unique_together = (('usuario', 'permission'),)


class AppcptVinculacion(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appcpt_vinculacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AppcptUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
