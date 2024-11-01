from django.core.management import BaseCommand

from lms.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        payments_list = [
            {'user': User.objects.get(email='user1@gmail.com'), 'course': Course.objects.all()[0], 'lesson': Lesson.objects.all()[0], 'amount': 10000, 'method': 'sbp'},
            {'user': User.objects.get(email='user2@gmail.com'), 'course': Course.objects.all()[0], 'lesson': Lesson.objects.all()[0], 'amount': 20000, 'method': 'cash'},
            {'user': User.objects.get(email='user3@gmail.com'), 'course': Course.objects.all()[0], 'lesson': Lesson.objects.all()[0], 'amount': 15000, 'method': 'sbp'},
            {'user': User.objects.get(email='user4@gmail.com'), 'course': Course.objects.all()[0], 'lesson': Lesson.objects.all()[0], 'amount': 12000, 'method': 'cash'}
        ]

        payments_for_create = []
        for payment_item in payments_list:
            payments_for_create.append(
                Payment(**payment_item)
            )

        Payment.objects.bulk_create(payments_for_create)