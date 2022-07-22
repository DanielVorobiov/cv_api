from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from common.cv_data import cv_data


class CurriculumVitaeViewSet(ViewSet):
    """
    API endpoints that allow viewing the info from the Curriculum Vitae
    """
    @action(detail=False, methods=['GET'], url_path='about', url_name='about')
    def about(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['about']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='experience')
    def experience(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['experience']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='education')
    def education(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['education']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='volunteering')
    def volunteering(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['volunteering']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='contacts')
    def contacts(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['contacts']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='soft-skills')
    def soft_skills(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['soft-skills']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='technical-skills')
    def technical_skills(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['technical-skills']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='languages')
    def languages(self, request, *args, **kwargs):
        return Response(
            {'value': cv_data['languages']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='awards')
    def awards(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['awards']},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['GET'], url_path='hobbies')
    def hobbies(self, request, *args, **kwargs):
        return Response(
            {"value": cv_data['hobbies']},
            status=status.HTTP_200_OK
        )
