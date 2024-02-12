from django.shortcuts import render
from rest_framework.views import APIView
import os
from elastic.settings import  BASE_DIR
from .models import Student
from rest_framework.response import Response 
from rest_framework import status
# Create your views here.
csv_path = os.path.join(BASE_DIR,'search/data_of_student.csv')

class GenerateData(APIView):
    def post(self,request):
        import csv

        list_of_data = []

        with open(csv_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                list_of_data.append(row)

        # Print the first few rows to verify
        for row in list_of_data:
            Student.objects.create(studentname=row[0],place=row[1],designation=row[2],email=row[3])
           

from elasticsearch_dsl import Search

def get_suggestions(querys):
    s = Search(index='student').query('match', place='Bangalore') \
                                     .suggest('suggestion', querys, term={'field': 'studentname'}) \
                                     .suggest('email_suggestion', querys, term={'field': 'email'}) \
                                     .suggest('designation_suggestion', querys, term={'field': 'designation'}) \
                                     
    
    response = s.execute()
    suggestions = [option['text'] for option in response.suggest.suggestion[0]['options']]
    return suggestions

class SearchView(APIView):
    def post(self,request):
        a = get_suggestions('p')
        print(a)
        return Response({},status=status.HTTP_202_ACCEPTED)
