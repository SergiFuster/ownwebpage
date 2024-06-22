from django_filters import FilterSet, ChoiceFilter
from .models import Post

DATE_CHOICES = [
    ('today', 'Today'),
    ('this_week', 'This Week'),
    ('this_month', 'This Month'),
]
class PostFilter(FilterSet):
    date = ChoiceFilter(choices=DATE_CHOICES, method='filter_by_date', empty_label='Any Date')
    class Meta:
        model = Post
        fields = {
            'date_posted': ['gte'],
        }

    def filter_by_date(self, queryset, name, value):
        from django.utils import timezone
        from datetime import timedelta

        if value == 'today':
            return queryset.filter(date_posted__date=timezone.now().date())
        elif value == 'this_week':
            start_week = timezone.now().date() - timedelta(days=timezone.now().weekday())
            return queryset.filter(date_posted__date__gte=start_week)
        elif value == 'this_month':
            return queryset.filter(date_posted__date__month=timezone.now().month)
        return queryset
    