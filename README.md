# Sistema-de-Detecci-n-de-Amenazas---Jhonny-Cueva
Configuración, integración y declaración de reglas usando Wazuh, GLPI, Suricata,  y agentes en LibroNet
# Proyecto: Sistema de Detección de Amenazas en Tiempo Real - LibroNet Digital S.A.
Este repositorio contiene la documentación técnica y las configuraciones del sistema implementado para la empresa **LibroNet Digital S.A.**, desarrollado como parte de la Macroactividad de la **Maestría Tecnológica en Herramientas de Ciberseguridad** (PAO I: 2026).

## 🏢 Descripción del Proyecto
El sistema implementa una plataforma de monitoreo y respuesta ante incidentes de seguridad en un entorno de laboratorio virtualizado. La arquitectura permite la visibilidad centralizada, trazabilidad de eventos y respuesta automatizada ante amenazas comunes en entornos de comercio electrónico.
#Nota en el scrip de la integración he borrado la ip y el token por medidas de seguridad alli debe poner el suyo si desean implementar este mismo modelo.

## 🏗️ Arquitectura Técnica
La solución integra las siguientes herramientas de código abierto:
- **Wazuh Manager (v4.x):** Correlación y clasificación de eventos de seguridad (detección basada en host).
- **Suricata IDS:** Inspección de tráfico de red para detección de escaneos y reconocimiento.
- **GLPI (v10.0.22):** Gestión de activos y mesa de servicio para la automatización de tickets.
- **MariaDB:** Persistencia de datos para GLPI.

## 📂 Estructura del Repositorio
```text
.
├── Servidor_107/           # Configuraciones de Wazuh Manager, GLPI, Suricata y DB
├── Cliente_108/            # Configuración de agentes (GLPI Agent + Wazuh Agent)
├── Portal_109_Final/       # Configuración de Apache y agente Wazuh
├── Scripts/                # Código fuente: custom-glpi.py (Integración API REST)
├── README.md               # Este archivo
└── Macroactividad.pdf      # Informe técnico detallado


🛡️ Incidentes Documentados
El sistema está configurado para detectar y generar tickets automáticos ante los siguientes escenarios:

Fuerza Bruta SSH: Detección de intentos fallidos de autenticación (Regla 5712).

Escaneo de Red (Nmap): Identificación de reconocimiento sobre el portal transaccional (Regla 100050 - Suricata).

Escalamiento de Privilegios: Detección de intentos no autorizados de ejecución de sudo (Reglas 5404/5503).

⚙️ Integración Automática
El script custom-glpi.py actúa como Active Response en Wazuh, permitiendo que cada alerta de seguridad relevante se convierta en un Ticket de GLPI con prioridad alta, notificando de inmediato al administrador vía SMTP.

Desarrollado por: Jhonny Cueva 
