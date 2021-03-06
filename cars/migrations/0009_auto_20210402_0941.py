# Generated by Django 3.1.7 on 2021-04-02 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20210331_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('LA', 'Ladakhk'), ('MZ', 'Mizoram'), ('DL', 'Delhi'), ('ML', 'Meghalaya'), ('HR', 'Haryana'), ('SK', 'Sikkim'), ('UK', 'Uttarakhand'), ('OD', 'Odisha'), ('GA', 'Goa'), ('CG', 'Chhattisgarh'), ('JH', 'Jharkhand'), ('TS', 'Telangana'), ('AN', 'Andaman and Nicobar Islands'), ('GJ', 'Gujarat'), ('KA', 'Karnataka'), ('PB', 'Punjab'), ('MP', 'Madhya Pradesh'), ('UP', 'Uttar Pradesh'), ('JK', 'Jammu and Kashmir'), ('AR', 'Arunachal Pradesh'), ('WB', 'West Bengal'), ('HP', 'Himachal Pradesh'), ('NL', 'Nagaland'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('RJ', 'Rajasthan'), ('PY', 'Puducherry'), ('MH', 'Maharashtra'), ('TN', 'Tamil Nadu'), ('TR', 'Tripura'), ('DD', 'Dadra and Nagar Haveli and Daman and Diu'), ('LD', 'Lakshadweep'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('AS', 'Assam')], max_length=100),
        ),
    ]
