from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import AdvertisementStatusChoices


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS or request.user.is_staff:
            return True
        return obj.creator == request.user


class IsDraftStatus(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.creator == request.user:
            return True
        if obj.status == AdvertisementStatusChoices.DRAFT and request.user == obj.creator:
            return True
        if request.method in SAFE_METHODS and obj.status != AdvertisementStatusChoices.DRAFT:
            return True
        return False