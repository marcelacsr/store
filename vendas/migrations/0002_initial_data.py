# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Categoria = apps.get_model("vendas", "Categoria")
    db_alias = schema_editor.connection.alias
    Categoria.objects.using(db_alias).bulk_create([
        Categoria(nome="Livros", slug="livros"),
        Categoria(nome="Camisetas", slug="camisetas")
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Categoria = apps.get_model("vendas", "Categoria")
    db_alias = schema_editor.connection.alias
    Categoria.objects.using(db_alias).filter(nome="Livros", slug="livros").delete()
    Categoria.objects.using(db_alias).filter(nome="Camisetas", code="camisetas").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]