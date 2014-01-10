# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'CustomUser', fields ['org']
        db.delete_unique('auth_user', ['org_id'])


        # Changing field 'CustomUser.org'
        db.alter_column('auth_user', 'org_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['organizations.Organization'], null=True))

    def backwards(self, orm):

        # Changing field 'CustomUser.org'
        db.alter_column('auth_user', 'org_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['organizations.Organization'], unique=True, null=True))
        # Adding unique constraint on 'CustomUser', fields ['org']
        db.create_unique('auth_user', ['org_id'])


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
            'org': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['organizations.Organization']", 'null': 'True'}),
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