from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from Ims.models import Course, Lesson
from users.models import User


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_count_in_course = SerializerMethodField()
    lessons = SerializerMethodField()
    owner_email = SerializerMethodField()

    def get_owner_email(self, course):
        if course.owner:
            return course.owner.email
        return None

    def get_lesson_count_in_course(self, obj):
        return obj.lesson_set.count()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "owner_email",
            "lesson_count_in_course",
            "lessons",
        )
