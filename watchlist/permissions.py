from rest_framework import permissions

# If use admin - do anything
# Else read only


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            # If user is not admin but method is GET (allow - read only)
            return True
        else:
            # Check permissions for write request
            # Allow access if user is admin (allow anything - all HTTP methods)
            return bool(request.user and request.user.is_staff)
            # Could have used (because we are inheriting IsAdminUser):
            # return super().has_permission(request, view)


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.reviewer == request.user
