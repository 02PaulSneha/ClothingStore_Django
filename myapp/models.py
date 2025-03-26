from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class DressVerity(models.Model):  # If you intended to name it "DressVerity," update this here and in the code.
    DRESS_TYPE_CHOICES = [
        ('WD', 'WEDDING'),
        ('PR', 'PROFESSIONAL'),
        ('CS', 'CASUAL'),
        ('BC', 'BEACH'),
        ('PA', 'PARTY'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myapp/')  # Ensure MEDIA_ROOT is configured in settings.
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=DRESS_TYPE_CHOICES)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
# One to Many(always take FOREIGN KEY)

class DressReview(models.Model):
    dress = models.ForeignKey(DressVerity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        # Handles cases where user or dress could be missing to avoid AttributeError.
        return f"Review by {self.user.username if self.user else 'Unknown User'} for {self.dress.name if self.dress else 'Unknown Dress'}"

 # Many to Many
 
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dress_varieties = models.ManyToManyField(DressVerity, related_name='stores')
    
    def __str__(self):
        return self.name
    
# One to One

class DressCertificate(models.Model):
    dress = models.OneToOneField(DressVerity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f"Certificate for {self.dress.name if self.dress else 'Unknown Dress'}"