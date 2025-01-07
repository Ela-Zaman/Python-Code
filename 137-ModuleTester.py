
from ModuleUser import User
from ModulePrivilegesAdmin import Admin , Privileges

ela= Admin("Ovro", "Sazid", 26, "B+","can dance","can walk")
ela.privileges.show_privileges()

new_priviliges=Privileges("can dance","can walk")
new_priviliges.show_privileges()