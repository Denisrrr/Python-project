from django.db import models


class Profession(models.Model):
    name = models.CharField('Название профессии', max_length=80)
    desc = models.TextField('Краткое описание')
    header_bg = models.ImageField('Изображение-фон для шапки', upload_to='images/main', null=True, blank=True)
    where_used = models.TextField('Где востребована')
    when_appeared = models.TextField('Когда появилась')
    about_img = models.ImageField('Изображение для раздела о профессии', upload_to='images/main/', null=True, blank=True)
    skills = models.TextField('Какие навыки необходимы для профессии')
    skills_img = models.ImageField('Изображение для раздела о навыках', upload_to='images/main/', null=True, blank=True)
    grades = models.TextField('Уровни по опыту работы')
    how_to_become = models.TextField('Как войти в профессию')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class SalaryStatistics(models.Model):
    profession = models.ForeignKey(Profession, verbose_name='Выбранная профессия', on_delete=models.DO_NOTHING)
    plot_img = models.ImageField('Изображение графика востребованности', upload_to='images/salary/')
    table = models.TextField('Таблица статистики востребованности')

    def __str__(self):
        return 'Статистика по востребованности'

    class Meta:
        verbose_name = 'Статистика по востребованности'
        verbose_name_plural = 'Статистики по востребованности'


class AreaStatistics(models.Model):
    plot_img = models.ImageField('Изображение графика статистики по городам', upload_to="images/area/")
    salary_table = models.TextField('Таблица ЗП по городам')
    fraction_table = models.TextField('Таблица доли вакансий по городам')

    def __str__(self):
        return 'Статистика по городам'

    class Meta:
        verbose_name = 'Статистика по городам'
        verbose_name_plural = 'Статистики по городам'


class SkillStatisticsPerYear(models.Model):
    profession = models.ForeignKey(Profession, verbose_name='Выбранная профессия', on_delete=models.DO_NOTHING)
    year = models.IntegerField('Год')
    plot_img = models.ImageField('Изображение графика топ-10 навыков', upload_to="images/skills/")
    table = models.TextField('Таблица')

    def __str__(self):
        return f'ТОП-10 навыков ({self.year}, {self.profession})'

    class Meta:
        verbose_name = 'Статистика по навыкам за год'
        verbose_name_plural = 'Статистики по навыкам'

