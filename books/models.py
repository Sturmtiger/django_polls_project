from django.db import models

# Create your models here.


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('title')

    def author1(self):
        return self.get_queryset().filter(author__first_name='author')


## Abstract inheritance

# class User(models.Model):
#     last_name = models.CharField(max_length=64)

#     class Meta:
#         abstract = True  # wont be saved to DB
#         ordering = ['last_name']


## Multi-table inheritance

# class User(models.Model):
#     last_name = models.CharField(max_length=64)

#     class Meta:
#         ordering = ['last_name']


class Author(models.Model):
    first_name = models.CharField(max_length=64, primary_key=True)

    # class Meta:
    #     verbose_name = 'Author',
    #     verbose_name = 'Authors'
    #     ordering = ['-first_name']
    #     db_table = f'{app_name}_{model_name}'  #  for existing table
    #     unique_together = ('first_name', 'last_name')  #  multiple key


## Proxy inheritance
class UaAuthor(Author):
    # cant overrive parent's attributes
    class Meta:
        proxy = True


class Ganre(models.Model): 
    name = models.CharField(max_length=64)


class Book(models.Model):
    title = models.CharField(max_length=64, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,
        related_name='active_books'
        )
    ganres = models.ManyToManyField(Ganre, related_name='books', through='BookGanre')

    man = BookManager()


class BookGanre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ganre = models.ForeignKey(Ganre, on_delete=models.CASCADE)

    date_add = models.DateField(auto_now_add=True)

    # type1 = models.OneTo
