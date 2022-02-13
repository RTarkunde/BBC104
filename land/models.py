from django.db import models

# Create your models here.
class Testimonials(models.Model):
    testimonial = models.TextField(max_length=200)

    def __str__(self):
        return self.testimonial
