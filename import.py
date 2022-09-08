# Set the file to read over
file = open('file.txt', 'r')
lines = file.readlines()
 
# Set initial values for resource id and import id
resource_id = "null"
import_id = "null"

# Write to the output file
f = open("file-output.txt", "w")
# Loop over line by line searching for wording
for line in lines:
    if "A resource with the ID" in line:
        resource_id = line.split('A resource with the ID "',1)[1]
        resource_id = resource_id.split('" already exists',1)[0]
        print(resource_id)
    if "  with " in line:
        import_id = line.split('  with ',1)[1]
        import_id = import_id.split(',',1)[0]
        print(import_id)
    if resource_id != "null" and import_id != "null":
        tf_import = 'terraform import \'' + import_id + '\' \'' + resource_id + '\''
        f.write(tf_import + '\n')
        resource_id = "null"
        import_id = "null"
f.close()
