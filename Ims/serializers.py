from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from Ims.models import Course, Lesson
from Ims.validators import validate_video_url


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    video_url = serializers.URLField(validators=[validate_video_url])

    class Meta:
        model = Lesson
        fields = "__all__"


class LessonDetailSerializer(ModelSerializer):
    course_info = SerializerMethodField()

    def get_course_info(self, lesson):
        if lesson.course.id:
            return {
                "course_name": lesson.course.name,
                "course_id": lesson.course.id,
            }
        return None

    class Meta:
        model = Lesson
        fields = (
            "name",
            "description",
            "video_url",
            "course_info",
        )


class CourseDetailSerializer(ModelSerializer):
    lesson_count_in_course = SerializerMethodField()
    lessons = SerializerMethodField()
    owner_info = SerializerMethodField()

    def get_owner_info(self, course):
        if course.owner:
            return {
                "email": course.owner.email,
                "id": course.owner.id,
            }
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
            "owner_info",
            "lesson_count_in_course",
            "lessons",
        )
