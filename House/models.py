from django.db import models
from django.utils.encoding import smart_text
import csv
import os


class House_Manager(models.Manager):
    def create_data(self, title, section, price, structure, photo, link):
        data = self.create(
            title=title,
            section=section,
            price=price,
            structure=structure,
            photo=photo,
            link=link
        )
        return data


class House(models.Model):
    title = models.CharField(max_length=30)
    section = models.CharField(max_length=30)
    price = models.CharField(max_length=15)
    structure = models.CharField(max_length=30)
    photo = models.URLField(blank=True)
    link = models.URLField(blank=True)

    objects = House_Manager()

    def __str__(self):
        return smart_text(self.title)


def get_data():
    workpath = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(workpath, 'house.csv')
    with open(c, "r", encoding='utf8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['\ufefftitle'], row['section'], row['price'], row['structure'], row['photo'], row['link'])
            House.objects.create_data(
                row['\ufefftitle'],
                row['section'],
                row['price'],
                row['structure'],
                row['photo'],
                row['link']
            )
    return reader


class Message(models.Model):
    h_fk = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    publication_date = models.DateTimeField()

    def __str__(self):
        return "\"" + self.user + "\"" + "留言說" + "\"" + self.comment + "\""

# get_data()
