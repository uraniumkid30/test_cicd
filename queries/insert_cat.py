from apps.resources.models import Resources, Category


#Our first query crate a category if does not exist 
category, created = Category.objects.get_or_create(cat_name = "Uncategorized")

print(f"Category ID: {category.id}")

# #next step let's add the foreign key to the resource model 

# #Update all the existing resources that have NULL cat field---> pass from NULL to category UNCATEGORIZED

# #
resources = Resources.objects.filter(cat__isnull=True).update(cat=category)
#Django behind the scene is basically connecting it to category.id 
#ORM works with object 

print(f"Updated {resources} resources")

#fecth the updated resources 

updated_resources = Resources.objects.filter(cat=category)

for resource in updated_resources:
    print(f"Resource Title: {resource.title}, Category: {resource.cat.cat_name}")


# #Create a new categories

# python_category1, created = Category.objects.get_or_create(cat_name="Django")
# python_category2, created = Category.objects.get_or_create(cat_name="Python")
# python_category3, created = Category.objects.get_or_create(cat_name="AWS")

# #get the resource
# resource = Resources.objects.get(title="Python Tutorial")
# #assign the resource to the Python category
# resource.cat = python_category2

# #save the changes
# resource.save()

# print(f"Updated resource '{resource.title}' with category:  {resource.cat.cat_name}")

# #self-study:
# #when you will create now new resources you can add directly the category
# #for the existing resources you can updated them 







