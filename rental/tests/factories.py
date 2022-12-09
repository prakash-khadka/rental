import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()
from rental.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category
    """
     name = fake.Sequence(lambda n: "cat_name_%d", % n)
     Also we can do by this way using sequence numbers to create unique cat 
    """
    # name = fake.lexify(text="cat_name_??????") 2:25
    name = factory.Sequence(lambda n: "cat_name_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)


