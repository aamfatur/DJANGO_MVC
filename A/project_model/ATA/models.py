from django.db import models

# Create your models here.

class Direksi(models.Model):
    Nama_Lengkap = models.CharField(max_length=200)
    Nomor_Telepon = models.CharField(max_length=12)
    Jabatan = models.CharField (max_length=200)

    def __str__ (self):
        return f'Nama Direksi: {self.Nama_Lengkap} Jabatan: {self.Jabatan}'

class Mentee(models.Model):
    Nama_Lengkap = models.CharField(max_length=200)
    Nomor_Telepon = models.CharField(max_length=12)
    Nomor_Absen = models.PositiveIntegerField(default=0)
    Nilai_rata_rata = models.FloatField(default=0)

    def __str__ (self):
        return f'Nama Mentee: {self.Nama_Lengkap} dan Nomor Absen: {self.Nomor_Absen}'

class MataPelajaran(models.Model):
    Nama_Pelajaran = models.CharField(max_length=200)
    Jadwal_Awal = models.DateTimeField('Jadwal Awal')
    Jadwal_Akhir = models.DateTimeField('Jadwal Akhir')

    def __str__ (self):
        return f'Nama Pelajaran: {self.Nama_Pelajaran}'


class Mentor(models.Model):
    Nama_Lengkap = models.CharField(max_length=200)
    Nomer_Telepon = models.CharField(max_length=12)
    Mata_Pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__ (self):
        return f'Nama Mentor: {self.Nama_Lengkap}'


class Challenge(models.Model):
    Nama_Chellenge = models.CharField(max_length=200)
    Banyak_Soal = models.PositiveSmallIntegerField(default=0)
    Bobot_Nilai = models.FloatField(default=0)
    Mata_Pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__ (self):
        return f'Nama Challenge: {self.Nama_Chellenge} untuk Pelajaran: {self.Mata_Pelajaran}'

class LiveCode(models.Model):
    Nama_Live_Code = models.CharField(max_length=200)
    Banyak_Soal = models.PositiveSmallIntegerField(default=0)
    Bobot_Nilai = models.FloatField(default=0)
    Tanggal_Pelaksanaan = models.DateTimeField('Tanggal Pelaksanaan')
    Mata_Pelajaran = models.ForeignKey(MataPelajaran, on_delete = models.CASCADE)

    def __str__ (self):
        return f'Nama Live Code: {self.Nama_Live_Code} untuk Pelajaran: {self.Mata_Pelajaran} dilaksanakan pada tanggal {self.Tanggal_Pelaksanaan}'

