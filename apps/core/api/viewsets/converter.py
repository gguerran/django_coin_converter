from drf_spectacular.utils import extend_schema, OpenApiParameter, inline_serializer

from rest_framework.response import Response
from rest_framework.serializers import CharField, DecimalField, DateTimeField
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from apps.core.api.services import convert_service

DEFAULT_ERROR_MESSAGE = "Não foi possível converter as moedas. Verifique os parâmetros informados."


class ConverterView(APIView):
    @extend_schema(
        description="Endpoint para converter moedas.",
        parameters=[
            OpenApiParameter(name="from", type=str, required=True, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="to", type=str, required=True, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="amount", type=float, required=True, location=OpenApiParameter.QUERY),
        ],
        responses={
            HTTP_200_OK: inline_serializer(
                name="ConverterResponse",
                fields={
                    "from": CharField(default="USD"),
                    "to": CharField(default="BRL"),
                    "amount": DecimalField(max_digits=8, decimal_places=2, default=150.35),
                    "converted": DecimalField(max_digits=8, decimal_places=2, default=774.83),
                    "datetime": DateTimeField(),
                },
            ),
            HTTP_400_BAD_REQUEST: inline_serializer(
                name="ConverterErrorResponse", fields={"error": CharField(default=DEFAULT_ERROR_MESSAGE)}
            ),
        },
    )
    def get(self, request):
        try:

            from_currency = request.query_params.get("from").upper()
            to_currency = request.query_params.get("to").upper()
            amount = request.query_params.get("amount")
            return Response(convert_service(from_currency, to_currency, amount), status=HTTP_200_OK)
        except Exception:
            return Response({"error": DEFAULT_ERROR_MESSAGE}, status=HTTP_400_BAD_REQUEST)
