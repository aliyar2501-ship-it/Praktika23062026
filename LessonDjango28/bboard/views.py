from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestPostClassView(APIView):
    """
    Класс-контроллер для демонстрации работы APIView.
    Разделяет обработку GET и POST запросов по встроенным методам класса.
    """

    def get(self, request, *args, **kwargs):
        """Обработка GET-запроса (Чтение данных)"""
        return Response({
            "message": "Класс-контроллер (APIView) готов к работе.",
            "instruction": "Вы можете отправить GET или POST запрос."
        })

    def post(self, request, *args, **kwargs):
        """Обработка POST-запроса (Прием данных)"""
        incoming_data = request.data
        title = incoming_data.get('title')
        price = incoming_data.get('price')

        if not title:
            return Response(
                {"error": "Поле 'title' является обязательным для класса-контроллера!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        response_data = {
            "status": "success",
            "controller_type": "Class-Based View (APIView)",
            "received_payload": {
                "title": title,
                "price": price,
                "description": incoming_data.get('description', 'Описание отсутствует')
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)



from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def bug_view(request):
    # Намеренно вызываем ошибку Python
    result = 100 / 0
    return Response({"data": result})


from django.shortcuts import render

def custom_page_not_found(request, exception):
    # 'exception' обязателен для обработчика 404
    return render(request, 'errors/404.html', status=404)

def custom_server_error(request):
    # Для ошибки 500 аргумент 'exception' не требуется
    return render(request, 'errors/500.html', status=500)