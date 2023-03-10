from rest_framework import serializers

from apps.user.models import User, UserImage


class UserImageSerializer(serializers.ModelSerializer):
    ''' serializer for profile photo '''
    class Meta:
        model = UserImage
        fields = "__all__"
        read_only_fields = ('user',)


class UsersAvatarSerializer(serializers.ModelSerializer):
    ''' for list of profile photos '''
    class Meta:
        model = UserImage
        fields = ['image']


class UserSerializerList(serializers.ModelSerializer):
    ''' Users  List '''
    user_image = UsersAvatarSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "first_name",
                  "last_name",
                  "last_action",
                  "is_online",
                  "user_image",
                  )
        read_only_fields = ('id', 'last_action', 'is_online')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "first_name",
                  "last_name",
                  'password',

                  )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
