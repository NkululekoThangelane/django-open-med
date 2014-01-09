# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomUser'
        db.create_table('auth_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=('username',), max_length=50, populate_from='username')),
            ('org', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['organizations.Organization'], unique=True, null=True)),
        ))
        db.send_create_signal(u'users', ['CustomUser'])

        # Adding M2M table for field groups on 'CustomUser'
        m2m_table_name = db.shorten_name('auth_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'users.customuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'CustomUser'
        m2m_table_name = db.shorten_name('auth_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customuser', models.ForeignKey(orm[u'users.customuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customuser_id', 'permission_id'])

        # Adding model 'Patient'
        db.create_table(u'users_patient', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.CustomUser'], unique=True, primary_key=True)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Physician'])),
        ))
        db.send_create_signal(u'users', ['Patient'])

        # Adding model 'Client'
        db.create_table(u'users_client', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.CustomUser'], unique=True, primary_key=True)),
            ('guardian', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Guardian'], null=True, blank=True)),
            ('guardian_relation', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('ssn', self.gf('encrypted_fields.fields.EncryptedCharField')(max_length=25, null=True)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Address'])),
            ('insurance', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='client_insurance', null=True, to=orm['insurance.InsuranceData'])),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.EmployerData'], null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['Client'])

        # Adding model 'Guardian'
        db.create_table(u'users_guardian', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.CustomUser'], unique=True, primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Address'])),
            ('insurance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insurance.InsuranceData'], null=True, blank=True)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.EmployerData'], null=True, blank=True)),
        ))
        db.send_create_signal(u'users', ['Guardian'])

        # Adding model 'Employee'
        db.create_table(u'users_employee', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.CustomUser'], unique=True, primary_key=True)),
            ('manager', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'users', ['Employee'])

        # Adding model 'Physician'
        db.create_table(u'users_physician', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.CustomUser'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'users', ['Physician'])

        # Adding model 'Therapist'
        db.create_table(u'users_therapist', (
            (u'customuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['users.CustomUser'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'users', ['Therapist'])

        # Adding model 'Address'
        db.create_table(u'users_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='id')),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('postal_code', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'users', ['Address'])


    def backwards(self, orm):
        # Deleting model 'CustomUser'
        db.delete_table('auth_user')

        # Removing M2M table for field groups on 'CustomUser'
        db.delete_table(db.shorten_name('auth_user_groups'))

        # Removing M2M table for field user_permissions on 'CustomUser'
        db.delete_table(db.shorten_name('auth_user_user_permissions'))

        # Deleting model 'Patient'
        db.delete_table(u'users_patient')

        # Deleting model 'Client'
        db.delete_table(u'users_client')

        # Deleting model 'Guardian'
        db.delete_table(u'users_guardian')

        # Deleting model 'Employee'
        db.delete_table(u'users_employee')

        # Deleting model 'Physician'
        db.delete_table(u'users_physician')

        # Deleting model 'Therapist'
        db.delete_table(u'users_therapist')

        # Deleting model 'Address'
        db.delete_table(u'users_address')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'data.employerdata': {
            'Meta': {'object_name': 'EmployerData'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.CustomUser']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizations.Organization']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'id'"})
        },
        u'insurance.insurancebase': {
            'Meta': {'object_name': 'InsuranceBase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'id'"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'insurance.insurancecompany': {
            'Meta': {'object_name': 'InsuranceCompany', '_ormbases': [u'insurance.InsuranceBase']},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Address']"}),
            u'insurancebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['insurance.InsuranceBase']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'insurance.insurancedata': {
            'Meta': {'object_name': 'InsuranceData', '_ormbases': [u'insurance.InsuranceBase']},
            'copay': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'group_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'insurancebase_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['insurance.InsuranceBase']", 'unique': 'True', 'primary_key': 'True'}),
            'policy_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insurance.InsuranceCompany']"}),
            'subscriber_data': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subscriber_data'", 'to': u"orm['users.CustomUser']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True'})
        },
        u'organizations.organization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Organization'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '200', 'separator': "u'-'", 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['users.CustomUser']", 'through': u"orm['organizations.OrganizationUser']", 'symmetrical': 'False'})
        },
        u'organizations.organizationuser': {
            'Meta': {'ordering': "['organization', 'user']", 'unique_together': "(('user', 'organization'),)", 'object_name': 'OrganizationUser'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organization_users'", 'to': u"orm['organizations.Organization']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'organization_users'", 'to': u"orm['users.CustomUser']"})
        },
        u'users.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'id'"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.client': {
            'Meta': {'object_name': 'Client', '_ormbases': [u'users.CustomUser']},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Address']"}),
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.EmployerData']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'guardian': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Guardian']", 'null': 'True', 'blank': 'True'}),
            'guardian_relation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'insurance': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'client_insurance'", 'null': 'True', 'to': u"orm['insurance.InsuranceData']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'ssn': ('encrypted_fields.fields.EncryptedCharField', [], {'max_length': '25', 'null': 'True'})
        },
        u'users.customuser': {
            'Meta': {'object_name': 'CustomUser', 'db_table': "'auth_user'"},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'org': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['organizations.Organization']", 'unique': 'True', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('username',)", 'max_length': '50', 'populate_from': "'username'"}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'users.employee': {
            'Meta': {'object_name': 'Employee', '_ormbases': [u'users.CustomUser']},
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'users.guardian': {
            'Meta': {'object_name': 'Guardian', '_ormbases': [u'users.CustomUser']},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Address']"}),
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.EmployerData']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'insurance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insurance.InsuranceData']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'users.patient': {
            'Meta': {'object_name': 'Patient', '_ormbases': [u'users.CustomUser']},
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Physician']"})
        },
        u'users.physician': {
            'Meta': {'object_name': 'Physician', '_ormbases': [u'users.CustomUser']},
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'users.therapist': {
            'Meta': {'object_name': 'Therapist', '_ormbases': [u'users.CustomUser']},
            u'customuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['users.CustomUser']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['users']