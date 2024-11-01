from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        users_list = [
            {'email': 'user1@gmail.com'},
            {'email': 'user2@gmail.com'},
            {'email': 'user3@gmail.com'},
            {'email': 'user4@gmail.com'}
        ]

        users_for_create = []
        for users_item in users_list:
            users_for_create.append(
                User(**users_item)
            )
        User.objects.bulk_create(users_for_create)
