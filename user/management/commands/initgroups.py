from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


GROUPS_PERMISSIONS = {
    'admin' : {
        #TOKEN : ['add', 'view', 'change', 'delete'],
        #Data : [],
    },
    'approver' :{

    },
}

class command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(command, self).__init__(*args, **kwargs)
    
    def handle(self, *args, **options):
        #loop group
        for group_name in GROUPS_PERMISSIONS:

            #get or create project
            group, created = Group.objects.get_or_create(name=group_name)

            #start with a clean slate
            if not created:
                group.permissions.clear()
            
            #loop models in group
            for model_cls in GROUPS_PERMISSIONS[group_name]:
                #loop permission in group/model
                for perm_name in GROUPS_PERMISSIONS[group_name][model_cls]:

                    #generate permission name as django would generate it
                    codename = perm_name + "_"+model_cls._meta.model_name

                    try:
                        #find permission object and add to group
                        perm = Permission.objects.get(codename=codename)
                        group.permissions.add(perm)
                        self.stdout.write("Adding "+ codename+" to group "+ group.__str__())
                    except Permission.DoesNotExist:
                        self.stdout.write(codename + " not found")

