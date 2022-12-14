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


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug = fake.lexify(text="prod_slug_??????")
    name = fake.lexify(text="prod_name_??????")
    description = fake.text()
    is_active = True
    created_at = "2021-09-04 22:14:18:279092"
    updated_at = "2021-09-04 22:14:18:279092"

    @factory.post_generation
    def category(self, crete, extracted, **kwargs):
        if not crete or not extracted:
            return

        if extracted:
            for cat in extracted:
                self.category.add(cat)


register(CategoryFactory)
register(ProductFactory)
