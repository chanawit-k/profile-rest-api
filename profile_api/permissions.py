from rest_framework import permissions  # type: ignore


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """
        เงื่อนไข if request.method in permissions.SAFE_METHODS: จะตรวจสอบว่า request method 
        ที่ใช้เป็น GET, HEAD หรือ OPTIONS หรือไม่ 
        ถ้าเป็นเช่นนั้นจะให้สิทธิ์ผ่านเนื่องจากเป็นการดู/อ่านข้อมูลเท่านั้น ไม่มีการแก้ไขข้อมูล
        """
        if request.method in permissions.SAFE_METHODS:
            print('true')
            return True
        print('false')
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
