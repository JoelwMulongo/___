#ORM Data manipulation (CRUD)

# Create
article = Article(name='Item 1', price=19.95)

# Save
article.save()

# One line create and save
Article.objects.create(name='Item 1', price=19.95) 

# Read all
Article.objects.all()

# Read one
Article.objects.get(id=1) 

# Select Related (to avoid n+1 query)
posts = Post.objects.select_related('user', 'category').all()

# Read or 404 
articles = Article.get_object_or_404(Article, id=502)    # render template/404.html

# Filter 
Article.objects.filter(model='dyson', name__icontains='dyson') # __icontains    
Article.objects.filter(year__gt=2016) # __gt = greater than

# Ordering 
Article.objects.order_by('name')     # ascending
Article.objects.order_by('-name')   # descending

# Slicing return first
Article.objects.all().order_by('name')[0]

# Slicing return last
Article.objects.all().order_by('-name')[0]

# Slicing limit/offset
Article.objects.all().order_by('name')[1..10]

# Updating
article = Article.objects.first()
article.name = 'new name'
article.save()

# One line update
Article.objects.filter(id=4).update(name='new name')

# Deleting
article = Article.objects.first()
article..delete()

# One line delete
article.objects.get(id=1).delete()

# Delete all
Article.objects.all().delete()

# Set ForeignKey field value
model1 = Model(name='dyson')
article.model = model1

# Get ForeignKey value
article1.model.name
model1.article_set.all()

# Add Many-to-Many
article1.tags.add(tag1) 
article1.tags.all()
tag1.articles_set.all()