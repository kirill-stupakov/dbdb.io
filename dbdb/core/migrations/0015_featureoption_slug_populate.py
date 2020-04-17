# Generated by Django 2.0.9 on 2018-12-04 11:31

from django.db import migrations


def populate(apps, schema_editor):
    from django.utils.text import slugify

    FeatureOption = apps.get_model('core', 'FeatureOption')

    pairs = set()

    for fo in FeatureOption.objects.all():
        fo.slug = slugify( fo.value )

        pair = ( fo.feature_id , fo.slug )

        if pair in pairs:
            fo.delete()
        else:
            fo.save()
            pairs.add(pair)
        pass

    return

def depopulate(apps, schema_editor):
    return


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_featureoption_slug'),
    ]

    operations = [
        migrations.RunPython(populate, depopulate),
    ]
