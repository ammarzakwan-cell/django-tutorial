from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import User

def user_list(request):
    return render(request, 'list.html')

class DataTableAPIView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        # Retrieve request parameters
        search_value = request.GET.get('search[value]', '')
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))
        order_column_index = int(request.GET.get('order[0][column]', 0))
        order_dir = request.GET.get('order[0][dir]', 'asc')

        # Define columns mapping (DataTables column names)
        columns = ['first_name', 'last_name', 'email', 'id']  # Adjust to match your model fields

        # Base QuerySet
        queryset = User.objects.all()

        # Apply search filter
        if search_value:
            queryset = queryset.filter(
                Q(email__icontains=search_value) | 
                Q(first_name__icontains=search_value)
            )

        # Calculate the filtered count before slicing
        records_filtered = queryset.count()

        # Apply ordering
        if order_column_index < len(columns):
            column_name = columns[order_column_index]
            if order_dir == 'asc':
                queryset = queryset.order_by(column_name)
            else:
                queryset = queryset.order_by(f"-{column_name}")
        else:
            queryset = queryset.order_by('-id')

        # Apply pagination
        queryset = queryset[start:start + length]

        # Total record count
        records_total = User.objects.count()

        # Prepare response data
        data = [
            {
                'first_name': obj.first_name,
                'last_name': obj.last_name,
                'email': obj.email,
                'id': obj.id,
            }
            for obj in queryset
        ]

        # Return JSON response
        return Response({
            'draw': int(request.GET.get('draw', 1)),  # Pass-through value from DataTables
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data,
        })
