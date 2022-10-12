from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer, MeasurementAddSerializer


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response({'sensors': serializer.data})

    def post(self, request):
        sensor = request.data
        serializer = SensorSerializer(data=sensor)
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()

        return Response({"success": "Sensor '{}' created successfully".format(sensor_saved.name)})


class SensorEdit(APIView):
    def put(self, request, pk):
        saved_sensor = get_object_or_404(Sensor.objects.all(), pk=pk)
        data = request.data
        serializer = SensorSerializer(instance=saved_sensor, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
        return Response({
            "success": "Sensor '{}' updated successfully".format(sensor_saved.name)
        })

class MeasurementAdd(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer

class SensorMeasurement(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
