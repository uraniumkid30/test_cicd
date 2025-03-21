from apps.resources.models import Resources

resource = Resources.objects.get(id=1) #only fecth the resource 1 query
print(resource.cat.cat_name) #it queries the category table 2 query

#only when the results are being accessed, the ORM will execute the database query

#Lazy loading--->(defualt behavior in Django)---> when you do no always need related data 
#disadvantage:
#data is only loaded when accessed (N+1 problem)

#Eager Loading (Using selected_related)
#fecth related data immidiatly in one query
resource = Resources.objects.select_related("cat").get(id=1)

print(resource.cat.cat_name)#No extra query! data is already loaded 

#faster and efficient when you have foreign key relationships (I have one query)
#disadvantage: can load unnecessary data 