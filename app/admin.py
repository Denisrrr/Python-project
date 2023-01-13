from django.contrib import admin

from app.models import Profession, SalaryStatistics, AreaStatistics, SkillStatisticsPerYear

admin.site.register(Profession)
admin.site.register(SalaryStatistics)
admin.site.register(AreaStatistics)
admin.site.register(SkillStatisticsPerYear)
