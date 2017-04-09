from django.db import models

# custom models

# TODO category model
# TODO activity model
# TODO supplier model

class Supplier(models.Model):
    supplier_title = models.CharField(max_length=250)
    supplier_description = models.TextField(max_length=2500)
    supplier_cost = models.ManyToManyField('SupplierCosts', related_name='costs')
    supplier_contacts =
    # add user how add

    def __str__(self):
        return str(self.supplier_title)

class SupplierCosts(models.Model):
    CHIP = ('CH', '$')
    MEDIUM = ('MD', '$$')
    EXPENSIVE = ('EX', '$$$')
    __all = (CHIP, MEDIUM, EXPENSIVE)

    supplier_cost = models.CharField(max_length=2, choices=__all)

    def __str__(self):
        return str(self.supplier_cost)

class SupplierContacts(models.Model):
    supplier_email1 = models.EmailField()
    supplier_email2 = models.EmailField()
    supplier_phone = models.IntegerField(max_length=30)
    supplier_skype = models.CharField(max_length=150)
    supplier_telegram = models.CharField(max_length=150)
    supplier_facebook = models.CharField(max_length=250)
    supplier_website = models.CharField(max_length=250)
    __all = (supplier_email1, supplier_email2, supplier_phone, supplier_skype, supplier_telegram, supplier_facebook, supplier_website)

    contacts_id = models.CharField(choices=__all)

    def __str__(self):
        return str(self.contacts_id)