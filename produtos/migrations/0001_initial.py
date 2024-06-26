# Generated by Django 4.2 on 2024-06-21 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da categoria')),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Embalagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome da embalagem')),
                ('sigla', models.CharField(max_length=3, verbose_name='Sigla da embalagem')),
            ],
            options={
                'db_table': 'embalagens',
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome_social', models.CharField(max_length=100, verbose_name='Razão social do fornecedor')),
                ('nome_fantasia', models.CharField(max_length=50, verbose_name='Nome fantasia do fornecedor')),
            ],
            options={
                'db_table': 'fornecedores',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do local armazenado')),
                ('tipo', models.CharField(choices=[('F', 'Fisico'), ('D', 'Digital')], max_length=1, verbose_name='Tipo do local movimentado')),
            ],
            options={
                'db_table': 'locais',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do produto')),
                ('estoque_minimo', models.FloatField(verbose_name='Estoque mínimo do produto')),
                ('estoque_maximo', models.FloatField(verbose_name='Estoque máximo do produto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria', verbose_name='Categoria de produto')),
                ('embalagens', models.ManyToManyField(to='produtos.embalagem', verbose_name='Embalagem do produto')),
            ],
            options={
                'db_table': 'produtos',
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('preco', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Preço do produto na movimrntação')),
                ('codigo_fabricante', models.CharField(max_length=20, verbose_name='Código do fabricante')),
                ('quantidade', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Quantidade movimentada')),
                ('tipo', models.IntegerField(choices=[('1', 'Entrada'), ('-1', 'Saída')], verbose_name='Tipo de movimentação')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.fornecedor', verbose_name='Fornecedor do produto movimentado')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.local', verbose_name='Local de movimentação')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto', verbose_name='Produto da movimentação')),
            ],
            options={
                'db_table': 'movimentacoes',
            },
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='produtos',
            field=models.ManyToManyField(to='produtos.produto', verbose_name='Produtos do Fornecedor'),
        ),
    ]
