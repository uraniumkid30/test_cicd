from apps.user.models import User
from apps.resources.models import Resources, Tag, ResourcesTag


# Sample tags
tags = ["Django", "Python", "Machine Learning", "Flask",
        "AI", "Data Science", "JavaScript", "React"]
# self-study try to insert the following tags

# Fecth existing resources
resources_data = [
    {"title": "Django Development", "tags": ["Django", "Python"]},
    {"title": "Python Tutorial", "tags": ["Python"]},
    {"title": "AI Basics", "tags": ["AI", "Data Science"]},


]

# for resource_data in resources_data:
#     #fect the resources by title
#     try:
#         resource = Resources.objects.get(title=resource_data["title"])
#         #for each tag in the list, fetch the Tag object and add it to the resource
#         for tag_name in resource_data["tags"]:
#             tag, created = Tag.objects.get_or_create(name=tag_name) #tag (is the existing or newly created tag,
#             #created isthe True Or False boolean flag for telling if the object was already existing)
#             #add the tag to the resources
#             resource.tags.add(tag) #automatically is created the association n the intermediate table
#         print(f"Added tags to {resource.title}")

#     except Resources.DoesNotExist:
#         print(f"Resource '{resource_data['title']}' does not exist.")

# print("Tags added successflully to existing resources!")


# you want to see all the tags associated to a specific resource
resource = Resources.objects.get(title="Django Development")
# fetch all related tags---> forward
tags = resource.tags.all()
print(f"Resource: {resource.title}")
print(f"Tags:", [tag.name for tag in tags])  # --> print all the tags name

# backaward relationship model_set

tag = Tag.objects.get(name="Python")
resources = tag.resources_set.all()  # get all the resources linked to Python

for resource in resources:
    print(resource.title)

# intermediate table is ResourcesTag
# get all the relationships between resources and tags

relationships = ResourcesTag.objects.all()

for relationship in relationships:
    print(
        f"Resource: {relationship.resources.title}, Tag: {relationship.tag.name}")


# many to many relationships always work with the related managers
# we can query direclty on the intermediate table
# When a resource is deleted, its related rows in the intermediate table is deleted as well.
# The tag itself is NOT deleted, only the connection between the resource and the tag

# Self-study
# - remove the resource
# - automatically in the intermediate table the connection, the row goes away
# -the tag in the tag table is not deleted so that can be used for other resources

