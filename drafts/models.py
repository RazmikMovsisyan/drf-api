from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Post

class Draft(models.Model):
    DRAFT_STATUS = [
        ('draft', 'Draft'),
        ('scheduled', 'Scheduled'),
        ('published', 'Published'),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drafts')
    content = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(
        upload_to='drafts/%Y/%m/%d/', 
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=DRAFT_STATUS, default='draft')
    scheduled_time = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    
    published_post = models.OneToOneField(
        Post, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='original_draft'
    )
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Draft by {self.author.username} - {self.status}"
    
    def publish(self):
        """Publish the draft as a new post"""
        from posts.models import Post
        
        # Create a new post with the draft data
        post = Post.objects.create(
            author=self.author,
            content=self.content,
            image=self.image,
            created_at=timezone.now()
        )
        
        # Update draft status
        self.status = 'published'
        self.published_post = post
        self.published_at = timezone.now()
        self.save()
        
        return post
    
    def schedule(self, schedule_time):
        """Schedule the draft for later publication"""
        self.status = 'scheduled'
        self.scheduled_time = schedule_time
        self.save()