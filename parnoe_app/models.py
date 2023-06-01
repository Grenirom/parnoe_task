from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


# print(Product.objects.filter(category_id=3), '!!!!!!!!!!!!!!!')
