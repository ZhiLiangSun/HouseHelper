from django.db import models
from django.utils.encoding import smart_text
import csv
import os


# Create your models here.

class H_Manager(models.Manager):
    def create_hdata(self, section, h_amount, h_score):
        data = self.create(
            section=section,
            h_amount=h_amount,
            h_score=h_score
        )
        return data


class Hospital(models.Model):
    section = models.CharField(max_length=30)
    h_amount = models.IntegerField()
    h_score = models.IntegerField()

    objects = H_Manager()

    def __str__(self):
        return smart_text(self.section)


def get_hdata():
    workpath = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(workpath, 'complete_hospital.csv')
    with open(c) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['section'], row['h_amount'], row['h_score'])
            Hospital.objects.create_hdata(
                row['section'],
                row['h_amount'],
                row['h_score']
            )
    return reader


class A_Manager(models.Manager):
    def create_adata(self, section, a_amount, a_score):
        data = self.create(
            section=section,
            a_amount=a_amount,
            a_score=a_score
        )
        return data


class Accident(models.Model):
    section = models.CharField(max_length=30)
    a_amount = models.IntegerField()
    a_score = models.IntegerField()

    objects = A_Manager()

    def __str__(self):
        return smart_text(self.section)


def get_adata():
    workpath = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(workpath, 'complete_accident.csv')
    with open(c) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['section'], row['h_amount'], row['h_score'])
            Accident.objects.create_adata(
                row['section'],
                row['a_amount'],
                row['a_score']
            )
    return reader


class S_Manager(models.Manager):
    def create_sdata(self, section, s_amount, s_score):
        data = self.create(
            section=section,
            s_amount=s_amount,
            s_score=s_score
        )
        return data


class Stolen(models.Model):
    section = models.CharField(max_length=30)
    s_amount = models.IntegerField()
    s_score = models.IntegerField()

    objects = S_Manager()

    def __str__(self):
        return smart_text(self.section)


def get_sdata():
    workpath = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(workpath, 'complete_stolen.csv')
    with open(c) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['section'], row['h_amount'], row['h_score'])
            Stolen.objects.create_sdata(
                row['section'],
                row['s_amount'],
                row['s_score']
            )
    return reader


class M_Manager(models.Manager):
    def create_mdata(self, section, m_amount, m_score):
        data = self.create(
            section=section,
            m_amount=m_amount,
            m_score=m_score
        )
        return data


class Market(models.Model):
    section = models.CharField(max_length=30)
    m_amount = models.IntegerField()
    m_score = models.IntegerField()

    objects = M_Manager()

    def __str__(self):
        return smart_text(self.section)


def get_mdata():
    workpath = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(workpath, 'complete_market.csv')
    with open(c) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['section'], row['h_amount'], row['h_score'])
            Market.objects.create_mdata(
                row['section'],
                row['m_amount'],
                row['m_score']
            )
    return reader


class L_Manager(models.Manager):
    def create_ldata(self, section, l_amount, l_score):
        data = self.create(
            section=section,
            l_amount=l_amount,
            l_score=l_score
        )
        return data


class Library(models.Model):
    section = models.CharField(max_length=30)
    l_amount = models.IntegerField()
    l_score = models.IntegerField()

    objects = L_Manager()

    def __str__(self):
        return smart_text(self.section)


def get_ldata():
    workpath = os.path.dirname(os.path.abspath(__file__))
    c = os.path.join(workpath, 'complete_library.csv')
    with open(c) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['section'], row['h_amount'], row['h_score'])
            Library.objects.create_ldata(
                row['section'],
                row['l_amount'],
                row['l_score']
            )
    return reader


    # get_hdata()
    # get_adata()
    # get_sdata()
    # get_mdata()
    # get_ldata()
