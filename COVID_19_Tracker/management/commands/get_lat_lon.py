from django.core.management.base import BaseCommand
from COVID_19_Tracker.utils import get_India_map,get_global_map


class Command(BaseCommand):
    help="To get Country and India Latitude and Longitude.. run python manage.py get_lat_lon"

    def handle(self, *args, **options):
        get_India_map()
        get_global_map()
        print("Done")

# to run this perticular file run in terminal
# python manage.py pull_latest_data