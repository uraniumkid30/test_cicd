from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Resources(models.Model):
    # foreign key, is a relationship between the resources table and the user table in the app user
    user = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    cat = models.ForeignKey(
        "resources.Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    # automatically django cat---> cat_id

    # user app name---> User is the class name

    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500, unique=True)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")

    class Meta:
        # to modify the name of the table (in django admin is customized)
        verbose_name_plural = "Resources"

    def __str__(self):
        # return f"{self.user.username} - {self.title}" #in my Adjango Admin username-title of the resource
        return self.user.username if self.user else "No user"

    # If I remove the user --> the user is gone but the resource stays there but has no user
    # with cascade instead user and resources all goes away
    @property
    def username(self):
        return self.user.username

    def all_tags(self):
        return ",".join([tag.name for tag in self.tags.all()])


class ResourcesTag(models.Model):
    # Many-to-many relationship has two foreign key
    resources = models.ForeignKey("resources.Resources", on_delete=models.CASCADE)
    tag = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["resources", "tag"],  # field names
                name="resource_tag_unique",  # the name of the constraint
                violation_error_message="Tag already exist for resource",  # Custom error message
            )
        ]


# resource1: Python development #python #python X
# resources1: Python development #python #backend ok


class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name


# add a category table that I have decided to be the ONE the parent in my resource model
# we already have existent resources inserted in our table without a category
# Before I create a foreign key, makemigrations and migrate
# after that I go in my insert_cat.py in queries and I create a default category
# I created the cat foreign key in my resource model
# makemigrations and migrate again
# and then I go again in insert_cat.py
