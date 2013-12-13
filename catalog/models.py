from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True,
        help_text='Unique value for product page URL, created from name.')
    description=models.TextField()
    is_active=models.BooleanField(default=True)
    meta_keywords=models.CharField("Meta Keywords",max_length=255,
        help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description=models.CharField("Meta Description",max_length=255,
        help_text='Content for description meta tag')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    parent_category=models.ForeignKey('self')
    #created_by (to be added after the user model is defined)
    #updated_by (to be added after the user model is defined)
    
    class Meta:
        db_table='categories'
        ordering=['-created_at']
        verbose_name_plural='Categories'
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category',(),{'category_slug':self.slug})

class Product(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True,
        help_text='Unique value for product-deal page URL, created from name.')
    #shop (to be added after shop model is defined)
    brand=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    old_price=models.DecimalField(max_digits=9,decimal_places=2,
        blank=True,default=0.00)
    image=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    #quantity=models.IntegerField()
    product_description=models.TextField()
    deal_description=models.TextField()
    deal_weeknumber=models.IntegerField()
    meta_keywords=models.CharField("Meta Keywords",max_length=255,
        help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description=models.CharField("Meta Description",max_length=255,
        help_text='Content for description meta tag')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField(Category)
    #created_by (to be added after the user model is defined)
    #updated_by (to be added after the user model is defined)    
    
    class Meta:
        db_table='products'
        ordering=['-created_at']
        
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product',(),{'product_slug':self.slug})

        