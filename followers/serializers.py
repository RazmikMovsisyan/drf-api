from rest_framework import serializers
from .models import Follower
from profiles.models import Profile


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    # accept a Profile ID as input
    followed_profile = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), write_only=True
    )

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_at',
            'followed_profile',  # profile ID input
            'followed',          # user ID (internal)
            'followed_name'
        ]
        read_only_fields = ['followed']

    def create(self, validated_data):
        profile = validated_data.pop('followed_profile')
        validated_data['followed'] = profile.owner  # convert profile → user
        return super().create(validated_data)
