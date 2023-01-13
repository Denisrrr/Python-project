import json
from datetime import datetime

import requests
from django.shortcuts import render
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from app.models import Profession, SalaryStatistics, AreaStatistics


def index(request):
    profession = Profession.objects.get(id=1)
    return render(request, 'index.html', context={'profession': profession})


def salary(request):
    profession = Profession.objects.get(id=1)
    statistics = SalaryStatistics.objects.get(profession=profession)
    return render(request, 'salary.html', context={'statistics': statistics})


def area(request):
    statistics = AreaStatistics.objects.get(id=1)
    return render(request, 'area.html', context={'statistics': statistics})


def skills(request):
    profession = Profession.objects.get(id=1)
    statistics = profession.skillstatisticsperyear_set.all().order_by('year')
    return render(request, 'skills.html', context={'profession': profession, 'statistics': statistics})

def last_vacancies(request):
    def get_salary_average(salary_from, salary_to):
        if salary_from and salary_to:
            return int((int(salary_from) + int(salary_to)) / 2)
        else:
            if salary_from:
                return int(salary_from)
            else:
                return int(salary_to)

    def fetch_vacancies_per_date(date: datetime, profession: str):
        vacancies = []
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.1, status_forcelist=[500])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        session.mount('http://', HTTPAdapter(max_retries=retries))
        params = {"page": 0, "per_page": 10, "text": profession, "date_from": date.strftime('%Y-%m-%d'),
                  "date_to": date.strftime('%Y-%m-%d'),
                  "specialization": 1, "only_with_salary": "true"}
        r = session.get('https://api.hh.ru/vacancies', params=params)
        data = json.loads(r.content.decode())
        for item in data['items']:
            r = session.get(item['url'], params=params)
            vacancy = json.loads(r.content.decode())
            parsed_vacancy = {'name': vacancy['name'], 'description': vacancy['description'],
                              'key_skills': list(map(lambda skill: skill['name'], vacancy['key_skills'])),
                              'employer': vacancy['employer']['name']}
            salary_from = vacancy['salary']['from']
            salary_to = vacancy['salary']['to']
            currency = vacancy['salary']['currency']
            parsed_vacancy['salary'] = f'{get_salary_average(salary_from, salary_to)} {currency}'
            parsed_vacancy['area'] = vacancy['area']['name']
            parsed_vacancy['published_at'] = datetime.strptime(vacancy['published_at'], '%Y-%m-%dT%H:%M:%S%z')
            vacancies.append(parsed_vacancy)
        r.close()
        result = sorted(vacancies, key=lambda v: v['published_at'], reverse=True)
        return result

    profession = Profession.objects.get(id=1)
    date_to_fetch = datetime(2022, 12, 21)
    vacancies = fetch_vacancies_per_date(date_to_fetch, profession)
    return render(request, 'last-vacancies.html', context={'profession': profession, 'vacancies': vacancies})
