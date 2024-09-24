from django.db import (models)

from django.contrib.auth.models import User


# Модель Video
class Video(models.Model):
    title = models.CharField(max_length=255) # Название видео
    description = models.TextField(blank=True) # Описание видео
    file = models.FileField(upload_to='videos/') # Файл видео(сыллка на файл)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')  # Автор видео
    created_at = models.DateTimeField(auto_now_add=True) # Дата загрузки
    views_count = models.IntegerField(default=0) # Количество просмотров

    def __str__(self):
        return self.title


# Модель Comment
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments') # Связь с видео
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments') # Автор коментариев
    text = models.TextField() # Текст коментариев
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания

    def __str__(self):
        return f'Comment by {self.author} on {self.video}'


# Модель Likes/Dislikes
class LikesDislaykes(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTE_CHOICE = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE) # Пользователь который лайкнул/дизлайкнул видео
    video = models.ForeignKey(Video, on_delete=models.CASCADE) # Связь с видео
    vote = models.SmallIntegerField(choices=VOTE_CHOICE) # Лайк или дизлайк

    def __str__(self):
        return f"{self.user} voted {'Like' if self.vote == 1 else 'Dislike'} on {self.video}"


# Модель Views
class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Пользователь который посмотрел видео
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='views') # Связь с видео
    viewed_at = models.DateTimeField(auto_now_add=True) # Дата просмотра

    def __str__(self):
        return f'View  by {self.user} on {self.video}'

