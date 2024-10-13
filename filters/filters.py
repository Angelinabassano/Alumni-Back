import django_filters
from .models import Coder, Skill

class CoderFilter(django_filters.FilterSet):
    front_end_skills = django_filters.ModelMultipleChoiceFilter(
        queryset=Skill.objects.all(),
        field_name='front_end_skills',
        to_field_name='name',
        conjoined=False
    )
    back_end_skills = django_filters.ModelMultipleChoiceFilter(
        queryset=Skill.objects.all(),
        field_name='back_end_skills',
        to_field_name='name',
        conjoined=False
    )
    experience = django_filters.CharFilter(field_name='experience', lookup_expr='icontains')
    availability = django_filters.CharFilter(field_name='availability', lookup_expr='icontains')
    language = django_filters.CharFilter(field_name='language', lookup_expr='icontains')

    class Meta:
        model = Coder
        fields = ['front_end_skills', 'back_end_skills', 'experience', 'availability', 'language']
