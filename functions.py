def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    return float(sum(calificaciones) / len(calificaciones))
