# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SyncChargedObject'
        db.create_table('django_ya_stripe_syncchargedobject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stripes_charges_synced_objects', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('stripe_charge_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount_charged', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('amount_refunded', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=9, decimal_places=2)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('django_ya_stripe', ['SyncChargedObject'])


    def backwards(self, orm):
        
        # Deleting model 'SyncChargedObject'
        db.delete_table('django_ya_stripe_syncchargedobject')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'django_ya_stripe.syncchargedobject': {
            'Meta': {'object_name': 'SyncChargedObject'},
            'amount_charged': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'amount_refunded': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '9', 'decimal_places': '2'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stripes_charges_synced_objects'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'stripe_charge_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['django_ya_stripe']
