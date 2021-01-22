from django.core.management.base import BaseCommand

from COVID_19_Tracker.utils import indiaData, globalData


class Command(BaseCommand):
    help = "pull the latest covid data"

    def handle(self, *args, **options):
        indiaData()
        globalData()
        print("Updation or creation done")

# to run this perticular file run in terminal
# python manage.py pull_latest_data
