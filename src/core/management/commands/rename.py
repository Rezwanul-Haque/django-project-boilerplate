import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')


    def handle(self, *args, **kwargs):

        new_project_name = kwargs['new_project_name']

        # bit of logic to rename the project
        current_project_name = os.environ.get("DJANGO_SETTINGS_MODULE").split('.')[0]
        # print('current project name: %s' %current_project_name)
        files_to_rename = [f'{current_project_name}/settings/base.py', f'{current_project_name}/wsgi.py', 'manage.py']
        # print('files to rename: %s' %files_to_rename)

        folder_to_rename = current_project_name
        # print('folder to rename: %s' %folder_to_rename)

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace(current_project_name, new_project_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)

        self.stdout.write(self.style.SUCCESS('Project has been renamed to %s' % new_project_name))
