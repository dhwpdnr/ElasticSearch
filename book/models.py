from django.db import models


class Publisher(models.Model):
    """Publisher Model Definition"""

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

    class Meta:
        """Meta options."""

        ordering = ["id"]

    def __str__(self):
        return self.name


class Author(models.Model):
    """Author Model Definition"""

    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    email = models.EmailField()

    class Meta:
        """Meta options."""

        ordering = ["id"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Tag Model Definition"""

    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Book(models.Model):
    """Book."""

    class BookPublishingStatusChoices(models.TextChoices):
        PUBLISHED = ("published", "Published")
        NOT_PUBLISHED = ("not_published", "Not published")
        IN_PROGRESS = ("in_progress", "In progress")
        CANCELLED = ("cancelled", "Cancelled")
        REJECTED = ("rejected", "Rejected")

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    state = models.CharField(max_length=100,
                             choices=BookPublishingStatusChoices.choices,
                             default=BookPublishingStatusChoices.PUBLISHED)
    isbn = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField(default=200)
    stock_count = models.PositiveIntegerField(default=30)
    tags = models.ManyToManyField(Tag,
                                  related_name='books',
                                  blank=True)

    class Meta:
        """Meta options."""

        ordering = ["isbn"]

    def __str__(self):
        return self.title

    @property
    def publisher_indexing(self):
        """Publisher for indexing.

        Used in Elasticsearch indexing.
        """
        if self.publisher is not None:
            return self.publisher.name

    @property
    def tags_indexing(self):
        """Tags for indexing.

        Used in Elasticsearch indexing.
        """
        return [tag.title for tag in self.tags.all()]
