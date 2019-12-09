from django.db import models

# Create your models here.

class Dokter(models.Model):
    Nama = models.CharField(max_length=200, default="")
    Nomor_Telepon = models.CharField(max_length=12, default="")
    Bidang = models.CharField (max_length=200, default="")
    Jadwal_Praktek = models.DateTimeField('jadwal praktek')

    def __str__ (self):
        return f'Nama Dokter: {self.Nama} dengan Bidang: {self.Bidang}'

class Pasien(models.Model):
    Nama = models.CharField(max_length=200, default="")
    Nomor_Telepon = models.CharField(max_length=12, default="")
    Alamat = models.CharField (max_length=200, default="")
    Keluhan = models.TextField(max_length=200, default="")

    def __str__ (self):
        return f'Nama Pasien: {self.Nama}, Alamat: {self.Alamat}'


class Resep(models.Model):
    Nama = models.CharField(max_length=200, default="")
    Total_Harga = models.PositiveIntegerField(default=0)
    Kumpulan_Obat = models.CharField (max_length=200, default="")

    def __str__ (self):
        return f'Nama Pasien: {self.Nama} dengan Total Harga: {self.Total_Harga}'


class Obat(models.Model):
    Nama = models.CharField(max_length=200)
    Kandungan = models.CharField(max_length=200)
    Khasiat = models.TextField (max_length=200)

    def __str__ (self):
        return f'Nama Obat: {self.Nama} dengan Khasiat: {self.Khasiat}'

