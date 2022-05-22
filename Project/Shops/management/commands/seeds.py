from datetime import datetime

from django.core.management.base import BaseCommand

from Shops.models import Shop, City, Street


class Command(BaseCommand):
    """Django command to prepare usual models City, Street and Shop."""

    def handle(self, *args, **options):
        """Check if objects exist, if not, then create them."""
        is_db_full = Street.objects.exists() and \
            City.objects.exists() and \
            Shop.objects.exists()

        if not is_db_full:
            cities = City.objects.bulk_create([
                City(name='Moscow'),
                City(name='Saint-Petersburg'),
                City(name='Vyborg'),
            ])

            universal_street_names = ['Leningradsky Avenue', 'Moscowsky Avenue']
            street_list = []
            for city in cities:
                for name in universal_street_names:
                    street_list.append(
                        Street(name=name + f' ({city.name})', city=city)
                    )

            streets = Street.objects.bulk_create(street_list)

            time_sample = datetime.now().time().replace(
                minute=0, second=0, microsecond=0)

            Shop.objects.bulk_create([
                Shop(name='Morning_Shop', city=cities[0], street=streets[0],
                     house='12k3', open_time=time_sample.replace(hour=5),
                     close_time=time_sample.replace(hour=15)),

                Shop(name='Day_Shop', city=cities[0], street=streets[1],
                     house='12k4', open_time=time_sample.replace(hour=9),
                     close_time=time_sample.replace(hour=18)),

                Shop(name='Evening_Shop', city=cities[1], street=streets[2],
                     house='52', open_time=time_sample.replace(hour=19),
                     close_time=time_sample.replace(hour=23)),

                Shop(name='Night_Shop', city=cities[1], street=streets[3],
                     house='75', open_time=time_sample.replace(hour=21),
                     close_time=time_sample.replace(hour=7)),

                Shop(name='Tricky_Shop', city=cities[1], street=streets[3],
                     house='75', open_time=time_sample.replace(hour=9),
                     close_time=time_sample.replace(hour=3)),
            ])
