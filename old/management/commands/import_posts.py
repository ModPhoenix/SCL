from django.core.management.base import BaseCommand, CommandError
from old.models import WpPosts
from blog.models import Post
from profiles.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        for p in WpPosts.objects.using('old').filter(post_type='post'):
            post = Post.objects.filter(title=p.post_title).first()
            if not post:
                post = Post()
            
            post.author = User.objects.get(id=1)
            post.title = p.post_title
            post.content = p.post_content
            post.created_at = p.post_date
            post.updated_at = p.post_modified
            post.save()


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            print(p.post_title)