from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model for extended user fields if needed
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

# Mentor Model
class Mentor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    role = models.CharField(max_length=100)  # E.g. "Character Animator"
    experience = models.CharField(max_length=100)
    attendance = models.CharField(max_length=10)
    top_rated = models.BooleanField(default=False)
    available_asap = models.BooleanField(default=False)
    coaching = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='mentor_pictures/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - Mentor"

# Mentee Model
class Mentee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    interests = models.TextField()  # Interests or areas they want to learn
    goals = models.TextField()      # Career or personal development goals
    assigned_mentor = models.ForeignKey(Mentor, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"{self.user.username} - Mentee"

# Session Model
class Session(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    session_notes = models.TextField(blank=True, null=True)  # Notes from the session
    session_type = models.CharField(max_length=50, choices=[('1on1', '1-on-1'), ('group', 'Group')])
    
    def __str__(self):
        return f"Session between {self.mentor.user.username} and {self.mentee.user.username} on {self.session_date}"

# Review Model
class Review(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    mentee = models.ForeignKey(Mentee, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review from {self.mentee.user.username} to {self.mentor.user.username}"

# PlatformStats Model (for platform-wide metrics)
class PlatformStats(models.Model):
    career_enhanced = models.IntegerField(default=0)
    empowered_mentors = models.IntegerField(default=0)
    global_community = models.IntegerField(default=0)
    connections_built = models.IntegerField(default=0)
    
    def __str__(self):
        return "Platform Stats"
