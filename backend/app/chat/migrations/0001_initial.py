# Generated by Django 3.2 on 2021-08-04 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='삭제일시')),
            ],
            options={
                'verbose_name': '채팅',
                'verbose_name_plural': '채팅',
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제여부')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일시')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='삭제일시')),
                ('text', models.TextField(blank=True, null=True, verbose_name='텍스트')),
                ('image', models.URLField(blank=True, null=True, verbose_name='이미지')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat', verbose_name='채팅')),
            ],
            options={
                'verbose_name': '메세지',
                'verbose_name_plural': '메세지',
                'ordering': ['-created'],
            },
        ),
    ]
