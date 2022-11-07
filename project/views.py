from calendar import c
from django.shortcuts import render
from appArbitro.models import arbitro
from appContrato.models import contrato, persona, tipo_persona
from appEquipo.models import equipo, alineacion_equipo
from user.models import User

def contadoresAdmin(request):
    arbitros = arbitro.objects.count()
    entrenadores = persona.objects.filter(tipo_persona_id=2).count()
    jugadores = persona.objects.filter(tipo_persona_id=1).count()
    equipos = equipo.objects.count()
    usuarios = User.objects.all()
    data = {
        'arbitros' : arbitros,
        'entrenadores' : entrenadores,
        'jugadores' : jugadores,
        'equipos' : equipos,
        'usuarios': usuarios
    }
    return render(request, 'admin/index.html', data)

def contextoJugador(request):

    data = {
        
    }

    return render(request, 'jugador.html', data)

def contextoEquipo(request, nombre_equipo):
    equipos = equipo.objects.get(nombre=nombre_equipo.upper())
    tipo_persona_entrenador = tipo_persona.objects.get(descripcion='ENTRENADOR')
    persona_entrenador = persona.objects.filter(tipo_persona_id=tipo_persona_entrenador.tipo_persona_id)

    entrenadoractual = []
    for p_e in persona_entrenador:
        contratosentrenadores = contrato.objects.filter(persona_id= p_e.persona_id,nuevo_club=equipos.equipo_id, estado=True)
        for ce in contratosentrenadores:
            if(ce.estado == True):
                entrenadoractual = ce

    tipo_persona_jugador = tipo_persona.objects.get(descripcion='JUGADOR')
    persona_jugador = persona.objects.filter(tipo_persona_id=tipo_persona_jugador.tipo_persona_id)
    jugadores = []
    for p_j in persona_jugador:
        contratosjugadores = contrato.objects.filter(persona_id= p_j.persona_id, nuevo_club=equipos.equipo_id, estado=True)
        for cj in contratosjugadores:
            if(cj.estado == True):
                jugadores.append(cj)

    alineacion_equipo_final = []

    for j in jugadores:
        alineacionequipo = alineacion_equipo.objects.filter(contrato_id=j.contrato_id)
        for ae in alineacionequipo:
            if(ae.estado == True or ae.estado == False):
                alineacion_equipo_final.append(ae)

    data = {
        'equipo' : equipos,
        'entrenador': entrenadoractual,
        'alineacion': alineacion_equipo_final
    }

    return render(request, 'equipo.html', data)

def index(request):
    data={
        
    }
    return render(request, 'index.html', data)
