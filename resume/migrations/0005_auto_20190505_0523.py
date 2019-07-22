# Generated by Django 2.2.1 on 2019-05-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20190504_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumedata',
            name='aboutme1',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='aboutme2',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='e_end1',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='e_end2',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='e_end3',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='e_start1',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='e_start2',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='e_start3',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='exp1',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='exp2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='exp3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='facebook',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='major1',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='major2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='major3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='position1',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='position2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='position3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='s_end1',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='s_end2',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='s_end3',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='s_start1',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='s_start2',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='s_start3',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='school1',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='school2',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='school3',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skill_level1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skill_level2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skill_level3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skill_type1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skill_type2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='resumedata',
            name='skill_type3',
            field=models.CharField(max_length=20, null=True),
        ),
    ]