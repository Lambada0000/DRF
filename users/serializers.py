from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from Ims.models import Subscription
from users.models import Payments, User


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    subs_info = SerializerMethodField()

    def get_subs_info(self, obj):
        subs = Subscription.objects.filter(user=obj)
        return [{"course": sub.course.name, "id": sub.id} for sub in subs]

    class Meta:
        model = User
        fields = "__all__"
