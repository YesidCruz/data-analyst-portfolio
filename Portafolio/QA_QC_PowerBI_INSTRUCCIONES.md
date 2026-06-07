# ⚡ QA/QC PRO DASHBOARD — Power BI Desktop
## Ingeniero Yesid Cruz — QA/QC Eléctrico & Instrumentación

---

## PASO 1 — Conectar el Excel como fuente de datos

1. Abrir **Power BI Desktop**
2. `Inicio → Obtener datos → Excel`
3. Seleccionar: `QA_QC_PRO_DASHBOARD_v10_YesidCruz.xlsx`
4. En el Navegador, seleccionar las hojas:
   - ✅ `MASTER_ACTIVIDADES`
   - ✅ `CERTIFICADOS`
   - ✅ `PLAN_SEMANAL`
   - ✅ `REGISTRO_NC`
   - ✅ `AVANCE`
5. Clic en **Transformar datos** (no Cargar directamente)

---

## PASO 2 — Power Query: Limpiar cada tabla

Para cada tabla, en el Editor de Power Query:

### MASTER_ACTIVIDADES
```
- Quitar fila 0 (título con emoji)
- "Usar primera fila como encabezados"
- Filtrar columna ID: contiene "QA" o "QC"
- Cambiar tipo: PESO(%) → Decimal, CANTIDAD TOTAL → Entero
```

### PLAN_SEMANAL
```
- Quitar fila 0 (título)
- "Usar primera fila como encabezados"
- Cambiar tipo: CANT. PROGRAMADA → Entero, CANT. EJECUTADA → Entero
- Columna FECHA → tipo Fecha
```

### CERTIFICADOS
```
- Quitar fila 0
- "Usar primera fila como encabezados"
- Cambiar tipo: PROGRAMADO → Entero, ENTREGADO → Entero, % AVANCE → Decimal
```

### REGISTRO_NC
```
- Quitar fila 0
- "Usar primera fila como encabezados"
- Columnas FECHA DETECCIÓN, FECHA LÍMITE → tipo Fecha
```

### AVANCE
```
- Quitar fila 0
- "Usar primera fila como encabezados"
- Cambiar tipo: % AVANCE → Decimal, AVANCE PONDERADO → Decimal
```

---

## PASO 3 — Medidas DAX (KPIs)

Crear una tabla `_MEDIDAS` vacía y agregar estas medidas:

```dax
-- ── TOTAL ACTIVIDADES ──
Total Actividades = COUNTROWS(MASTER_ACTIVIDADES)

-- ── AVANCE PONDERADO ──
Avance Ponderado % =
DIVIDE(
    SUMX(AVANCE, AVANCE[AVANCE PONDERADO]),
    100
)

-- ── NCs ABIERTAS ──
NCs Abiertas =
CALCULATE(
    COUNTROWS(REGISTRO_NC),
    REGISTRO_NC[ESTADO] = "🔴 Abierta"
)

-- ── CERTIFICADOS ENTREGADOS ──
Certificados Entregados =
CALCULATE(
    SUM(CERTIFICADOS[ENTREGADO])
)

-- ── SEMÁFORO ──
Semáforo =
VAR pct = [Avance Ponderado %] * 100
RETURN
    IF(pct >= 90, "✅ VERDE",
    IF(pct >= 70, "⚠️ AMARILLO",
    "🔴 ROJO"))

-- ── COLOR SEMÁFORO ──
Color Semáforo =
VAR pct = [Avance Ponderado %] * 100
RETURN
    IF(pct >= 90, "#2ecc71",
    IF(pct >= 70, "#f39c12",
    "#e74c3c"))

-- ── AVANCE QA ──
Avance QA =
CALCULATE(
    AVERAGE(AVANCE[% AVANCE]),
    AVANCE[TIPO] = "QA"
)

-- ── AVANCE QC ──
Avance QC =
CALCULATE(
    AVERAGE(AVANCE[% AVANCE]),
    AVANCE[TIPO] = "QC"
)

-- ── % CUMPLIMIENTO SEMANAL ──
Cumplimiento Semanal % =
DIVIDE(
    SUM(PLAN_SEMANAL[CANT. EJECUTADA]),
    SUM(PLAN_SEMANAL[CANT. PROGRAMADA])
)
```

---

## PASO 4 — Visuals Requeridos

### 4.1 Tarjetas KPI (Cards)
Insertar 4 tarjetas de tipo `Card`:
| Tarjeta | Medida | Color |
|---------|--------|-------|
| Total Actividades | `[Total Actividades]` | Azul acento `#3498db` |
| Avance Ponderado | `[Avance Ponderado %]` (formato %) | Semáforo dinámico |
| NCs Abiertas | `[NCs Abiertas]` | Rojo `#e74c3c` |
| Certificados Entregados | `[Certificados Entregados]` | Verde `#2ecc71` |

**Formato de cada card:**
- Fondo: `#1c2128`
- Borde: `1px #30363d`
- Fuente valor: Segoe UI, 36px, Bold
- Etiqueta: Segoe UI, 11px, color `#8b949e`

---

### 4.2 Gráfico de Barras Apiladas QA vs QC

1. Insertar visual: **Gráfico de barras apiladas**
2. Configurar:
   - **Eje X:** `MASTER_ACTIVIDADES[PROYECTO]`
   - **Valores:** Recuento de `ID` por `TIPO`
   - **Leyenda:** `MASTER_ACTIVIDADES[TIPO]`
3. Colores:
   - QA: `#2e86c1`
   - QC: `#2ecc71`
4. Fondo: `#1c2128`, sin cuadrícula visible

---

### 4.3 Gráfico de Líneas — Cumplimiento Semanal

1. Insertar visual: **Gráfico de líneas**
2. Configurar:
   - **Eje X:** `PLAN_SEMANAL[SEMANA]`
   - **Valores Y1:** `SUM(PLAN_SEMANAL[CANT. PROGRAMADA])` — línea discontinua azul `#2e86c1`
   - **Valores Y2:** `SUM(PLAN_SEMANAL[CANT. EJECUTADA])` — línea sólida verde `#2ecc71`
3. Activar: **Líneas de referencia** para meta 100%

---

### 4.4 Semáforo de Avance (KPI visual)

**Opción A — Medidor (Gauge):**
1. Insertar visual: **Medidor**
2. Valor: `[Avance Ponderado %]`
3. Destino: `1` (100%)
4. Colores condicionales con la medida `[Color Semáforo]`

**Opción B — Tarjeta con formato condicional:**
1. Card con `[Semáforo]`
2. Formato condicional en color de fuente:
   - `✅ VERDE` → `#2ecc71`
   - `⚠️ AMARILLO` → `#f39c12`
   - `🔴 ROJO` → `#e74c3c`

---

## PASO 5 — Tema Corporativo (JSON)

Guardar como `tema_yesid_cruz.json` y cargar desde
`Vista → Temas → Examinar temas`:

```json
{
  "name": "QA/QC Yesid Cruz",
  "dataColors": ["#2e86c1","#2ecc71","#e74c3c","#f39c12","#3498db","#1a5276"],
  "background": "#0d1117",
  "foreground": "#e6edf3",
  "tableAccent": "#2e86c1",
  "visualStyles": {
    "*": {
      "*": {
        "background": [{"color": {"solid": {"color": "#1c2128"}}}],
        "border": [{"show": true, "color": {"solid": {"color": "#30363d"}}}]
      }
    },
    "card": {
      "*": {
        "labels": [{"color": {"solid": {"color": "#8b949e"}}, "fontSize": 11}],
        "calloutValue": [{"fontSize": 32, "fontFamily": "Segoe UI"}]
      }
    }
  }
}
```

---

## PASO 6 — Texto de Cabecera Personalizado

Insertar un **Cuadro de texto** en la parte superior del informe:

```
⚡  QA/QC PRO DASHBOARD
Ingeniero Yesid Cruz — QA/QC Eléctrico & Instrumentación
```

Configuración:
- Fuente: Segoe UI, 18px (título) / 13px (subtítulo)
- Color: `#e6edf3` y `#3498db`
- Fondo: `#1a5276`
- Sin borde

---

## PASO 7 — Publicar en Power BI Service

1. `Inicio → Publicar`
2. Seleccionar el workspace destino
3. URL del dashboard: `https://app.powerbi.com/groups/<workspace>/reports/<id>`
4. Para LinkedIn: captura la vista del informe publicado o exporta como PDF desde
   `Archivo → Exportar → PDF`

---

## PASO 8 — Actualización Automática

En Power BI Service:
1. `Conjunto de datos → Configuración → Actualización programada`
2. Habilitar: **Sí**
3. Frecuencia: Diaria / Cada hora
4. Requiere: **Power BI Gateway** (modo personal o empresa) con acceso al Excel en red/SharePoint

Para Excel en SharePoint/OneDrive:
- Usar conector `SharePoint Online List` o `OneDrive for Business`
- La actualización funciona sin Gateway

---

## RESUMEN DE KPIs CALCULADOS (datos actuales)

| KPI | Valor |
|-----|-------|
| Total Actividades | **56** |
| Avance Ponderado | **97.2%** ✅ VERDE |
| NCs Abiertas | **2** 🔴 |
| Certificados Entregados | **25** |
| Proyectos Activos | **3** |

---

*Documento generado automáticamente para: Ingeniero Yesid Cruz — QA/QC Eléctrico & Instrumentación*
*Fecha: {{ fecha actual }}*
