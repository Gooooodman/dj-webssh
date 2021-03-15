from django.db import models

# Create your models here.


from django.db import models
from apps.account.models import User
from apps.setting.utils import AppSetting
from libs.ssh import SSH


class Host(models.Model):
    name = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    port = models.IntegerField()
    username = models.CharField(max_length=50)
    desc = models.CharField(max_length=255, null=True)

    def get_ssh(self, pkey=None):
        pkey = pkey or AppSetting.get('private_key')
        return SSH(self.hostname, self.port, self.username, pkey)

    def __repr__(self):
        return '<Host %r>' % self.name

    class Meta:
        db_table = 'hosts'
        ordering = ('-id',)