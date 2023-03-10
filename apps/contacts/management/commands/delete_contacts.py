from django.core.management.base import BaseCommand
from apps.contacts.models import Contact
from logging import getLogger


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--is-only-auto-generated",
            help="Delete all only auto generated contacts",
            action="store_true",
        )

    def handle(self, *args, **options):
        is_only_auto_generated: bool = options["is_only_auto_generated"]

        logger = getLogger("django")
        queryset = Contact.objects.all()
        logger.info(f"Current amount of contacts -before- {queryset.count()}")

        queryset_for_delete = queryset

        if is_only_auto_generated:
            logger.info("Delete only auto generated contacts")
            queryset_for_delete = queryset_for_delete.filter(is_auto_generated=True)

        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of contacts -after- {queryset.count()}")

        print()
