from django.core.management.base import BaseCommand
from apps.logger_middleware.models import RequestsLogger
from logging import getLogger


class Command(BaseCommand):
    help = "Delete all RequestsLogger records"

    def handle(self, *args, **options):
        logger = getLogger("django")
        queryset = RequestsLogger.objects.all()

        logger.info(f"Current amount of RequestsLogger_records -before- {queryset.count()}")
        queryset_for_delete = queryset
        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"total deleted: {total_deleted}, details: {details}")
        logger.info(f"Current amount of RequestsLogger_records -after- {queryset.count()}")
        print()
