from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_counter = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)


    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_counter(self, course):
        return Lesson.objects.filter(course_id=course.id).count()