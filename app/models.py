from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField()
    logo = models.CharField()
    color = models.CharField()
    website = models.CharField()
    join_date = models.DateTimeField(auto_now=True)


class Job(models.Model):
    CONTRACT_TYPES = [
        ("FT", "Full Time"),
        ("PT", "Part Time"),
        ("CO", "Contract"),
        ("FR", "Freelance"),
    ]

    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    title = models.CharField()
    description = models.TextField()
    location = models.CharField()  # todo: possibly expand on this later
    contract_type = models.CharField(choices=CONTRACT_TYPES)
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']


class Blurb(models.Model):
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    order = models.IntegerField(null=True)


class BlurbHeading(models.Model):
    blurb = models.ForeignKey("Blurb", on_delete=models.CASCADE)
    text = models.TextField()


class BlurbList(models.Model):
    LIST_TYPES = [
        ("OL", "Ordered List"),
        ("UL", "Unordered List"),
    ]

    heading = models.ForeignKey("Blurb", on_delete=models.CASCADE)
    type = models.CharField(choices=LIST_TYPES)


class BlurbListItem(models.Model):
    blurb_list = models.ForeignKey("BlurbList", on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(null=True)
