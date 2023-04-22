from django.core.management.base import BaseCommand
from django.contrib.auth import Group, Permission

class command(BaseCommand):
    args = '<None>'
    help = 'Nothing to help here yet'

    def _create_tags(self):
        adminG = Group.object.get_or_create(name='admin')
        approverG = Group.object.get_or_create(name='approver')
        reviewerG = Group.object.get_or_create(name='reviewer')

        for permission in Permission.objects.all():
            adminG.permission.add(permission)

        reviewerG.permission.add(Permission.object.get(codename='view_actor'))

    def handle(self,*args,**options):
        self._create_tags()
