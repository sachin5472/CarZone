# Generated by Django 3.1.7 on 2021-04-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20210402_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('PB', 'Punjab'), ('BR', 'Bihar'), ('MH', 'Maharashtra'), ('OD', 'Odisha'), ('DD', 'Dadra and Nagar Haveli and Daman and Diu'), ('AP', 'Andhra Pradesh'), ('JH', 'Jharkhand'), ('KL', 'Kerala'), ('AS', 'Assam'), ('UK', 'Uttarakhand'), ('GJ', 'Gujarat'), ('TN', 'Tamil Nadu'), ('CG', 'Chhattisgarh'), ('HP', 'Himachal Pradesh'), ('TR', 'Tripura'), ('MP', 'Madhya Pradesh'), ('KA', 'Karnataka'), ('CH', 'Chandigarh'), ('DL', 'Delhi'), ('JK', 'Jammu and Kashmir'), ('LA', 'Ladakhk'), ('SK', 'Sikkim'), ('AN', 'Andaman and Nicobar Islands'), ('LD', 'Lakshadweep'), ('WB', 'West Bengal'), ('AR', 'Arunachal Pradesh'), ('RJ', 'Rajasthan'), ('TS', 'Telangana'), ('NL', 'Nagaland'), ('GA', 'Goa'), ('MZ', 'Mizoram'), ('PY', 'Puducherry'), ('UP', 'Uttar Pradesh'), ('ML', 'Meghalaya'), ('HR', 'Haryana')], max_length=100),
        ),
    ]
