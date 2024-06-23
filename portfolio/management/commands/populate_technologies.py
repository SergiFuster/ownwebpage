# populate_technologies.py
from django.core.management.base import BaseCommand
from portfolio.models import Technology

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        technologies = [
            'Python', 'Django', 'JavaScript', 'React', 'HTML', 'CSS',
            'Bootstrap', 'Materialize', 'PostgreSQL', 'SQLite', 'Heroku',
            'Git', 'GitHub', 'VSCode', 'PyCharm', 'Sublime', 'Atom',
            'Linux', 'Windows', 'MacOS', 'AWS', 'Azure', 'GCP', 'Docker',
            'Kubernetes', 'Jenkins', 'TravisCI', 'CircleCI', 'Jira',
            'Confluence', 'Slack', 'Trello', 'Asana', 'Notion', 'Postman',
            'Insomnia', 'Swagger', 'TDD', 'BDD', 'Agile', 'Scrum',
            'Kanban', 'XP', 'Pair Programming', 'Mob Programming',
            'CI/CD', 'DevOps',
        ]
        for tech in technologies:
            Technology.objects.get_or_create(name=tech)

        self.stdout.write(self.style.SUCCESS('Tecnologías creadas correctamente'))
