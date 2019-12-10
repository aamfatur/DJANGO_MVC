# Generated by Django 3.0 on 2019-12-09 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Lengkap', models.CharField(max_length=200)),
                ('Nomor_Telepon', models.CharField(max_length=12)),
                ('Jabatan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Pelajaran', models.CharField(max_length=200)),
                ('Jadwal_Awal', models.DateTimeField(verbose_name='Jadwal Awal')),
                ('Jadwal_Akhir', models.DateTimeField(verbose_name='Jadwal Akhir')),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Lengkap', models.CharField(max_length=200)),
                ('Nomor_Telepon', models.CharField(max_length=12)),
                ('Nomor_Absen', models.PositiveIntegerField(default=0)),
                ('Nilai_rata_rata', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Chellenge', models.CharField(max_length=200)),
                ('Nomer_Telepon', models.CharField(max_length=12)),
                ('Mata_Pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='LiveCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Live_Code', models.CharField(max_length=200)),
                ('Banyak_Soal', models.PositiveSmallIntegerField(default=0)),
                ('Bobot_Nilai', models.FloatField(default=0)),
                ('Tanggal_Pelaksanaan', models.DateTimeField(verbose_name='Tanggal Pelaksanaan')),
                ('Mata_Pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama_Chellenge', models.CharField(max_length=200)),
                ('Banyak_Soal', models.PositiveSmallIntegerField(default=0)),
                ('Bobot_Nilai', models.FloatField(default=0)),
                ('Mata_Pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ATA.MataPelajaran')),
            ],
        ),
    ]