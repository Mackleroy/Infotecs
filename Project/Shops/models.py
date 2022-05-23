from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)  # or TextField if 255 is not enough

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, related_name='streets',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    street = models.ForeignKey(Street, related_name='shops',
                               on_delete=models.CASCADE)
    house = models.CharField(max_length=255)  # CharField for cases like "20k3"
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name
