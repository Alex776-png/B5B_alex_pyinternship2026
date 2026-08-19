admin_permissions = {
    "read",
    "write",
    "delete",
    "manage_users"
}

editor_permissions = {
    "read",
    "write"
}

# An editor user has only editor permissions
user_permissions = editor_permissions

required_permissions = {"delete", "manage_users"}

if required_permissions.issubset(user_permissions):
    print("User can perform the admin action.")
else:
    print("Access denied: admin permissions are required.")
