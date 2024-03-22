from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_members = models.ManyToManyField('auth.User', related_name='projects')

    def __str__(self):
        return self.name
    
    def get_project_duration(self):
        duration = self.end_date-self.start_date
        return duration.days
    
    def get_team_members_count(self):
        return self.team_members.count()