from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from Ims.models import Course, Lesson


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

    def get_lesson_count_in_course(self, obj):
        return obj.lesson_set.count()

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "lesson_count_in_course",
            "lessons",
        )  # Добавлено поле lessons
