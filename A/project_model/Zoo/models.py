from django.db import models

# Create your models here.

class Hewan(models.Model):
    Nama = models.CharField(max_length=200, default="")
    Species = models.CharField(max_length=12, default="")
    Berat = models.IntegerField (default=0)
    Umur = models.IntegerField(default=0)

    def __str__ (self):
        return f'Nama Hewan {self.Nama}, Species: {self.Species} dengan berat {self.Berat} kg'

class Kandang(models.Model):
    Nama = models.CharField(max_length=200, default="")
    Isi_Kandang = models.TextField(default="")
    Luas_Kandang = models.PositiveSmallIntegerField(default=0)

    def __str__ (self):
        return f'Nama Kandang: {self.Nama}, Luas {self.Luas_Kandang} meter persegi dan Penghuni Kandang: {self.Isi_Kandang}'


class Penjaga(models.Model):
    Nama = models.CharField(max_length=200)
    Nomor_Telepon = models.CharField(max_length=12)
    Jadwal_Jaga = models.DateTimeField('Jadwal Jaga')

    def __str__ (self):
        return f'Nama Penjaga: {self.Nama}, Jadwal Jaga: {self.Jadwal_Jaga}'


class Pengunjung(models.Model):
    Nama = models.CharField(max_length=200)
    Nomor_Telepon = models.CharField(max_length=12)
    Hari_Berkunjung = models.DateTimeField('Hari Berkunjung')

    def __str__ (self):
        return f'Nama Pengunjung: {self.Nama} dan Jadwal Berkunjung: {self.Hari_Berkunjung}'