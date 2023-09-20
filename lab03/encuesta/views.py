from django.shortcuts import render
from .models import Proveedor, Cliente, Categoria, Producto, Venta, DetalleVenta

def index(request):
    # Obtener las ventas más recientes ordenadas por fecha descendente
    ventas_recientes = Venta.objects.order_by('-fecha')[:5]
    
    # Obtener todos los productos y personas de la base de datos
    productos = Producto.objects.all()
    personas = Cliente.objects.all()

    context = {
        'ventas_recientes': ventas_recientes,
        'productos': productos,
        'personas': personas,
    }
    return render(request, 'encuesta/index.html', context)

def detalle_venta(request, venta_id):
    venta = Venta.objects.get(pk=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)

    context = {
        'venta': venta,
        'detalles': detalles,
    }
    return render(request, 'encuesta/detalle.html', context)

def resultados_venta(request, venta_id):
    venta = Venta.objects.get(pk=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)

    context = {
        'venta': venta,
        'detalles': detalles,
    }
    return render(request, 'encuesta/resultados.html', context)

