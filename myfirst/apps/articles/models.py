from django.db import models

# Create your models here.
class Article (models. Model):
    article_title = models.CharField('Название артикля', max_length = 200)
    article_text = models.TextField('TEKCT CTaтьи')
    pub_date= models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title    
    
    class Meta:
        verbose_name = 'Артикль'
        verbose_name_plural = 'Артикли'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 50)
    comment_text = models.CharField('TEKCT KOMMEHTaрия', max_length = 200)

    def __str__(self):
        return self.author_name 

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'        