"""
╔══════════════════════════════════════════════════════════════════════════════╗
║         QA/QC PRO PORTAFOLIO — Ingeniero Yesid Cruz                        ║
║         QA/QC Eléctrico & Instrumentación                                   ║
║         Dashboard Interactivo — Python / Dash  v10                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

INSTRUCCIONES (Visual Studio Code):
    1. pip install dash dash-bootstrap-components pandas openpyxl plotly
    2. Coloca el Excel en la misma carpeta que este script
    3. python QA_QC_PRO_DASHBOARD.py
    4. Abre http://127.0.0.1:8050
"""

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 1 — IMPORTACIONES
# ─────────────────────────────────────────────────────────────────────────────
import os, sys, warnings
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from datetime import datetime

warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 2 — CONFIGURACIÓN GLOBAL (Paleta Corporativa)
# ─────────────────────────────────────────────────────────────────────────────
CONFIG = {
    "nombre":     "Ingeniero Yesid Cruz",
    "especialidad": "QA/QC Eléctrico & Instrumentación",
    "excel_file": "QA_QC_PRO_DASHBOARD_v10_YesidCruz.xlsx",
    "titulo":     "QA/QC PRO PORTAFOLIO",
}

C = {
    "bg":          "#0d1117",
    "panel":       "#161b22",
    "card":        "#1c2128",
    "azul_p":      "#1a5276",
    "azul":        "#2e86c1",
    "acento":      "#3498db",
    "gris":        "#8b949e",
    "blanco":      "#e6edf3",
    "verde":       "#2ecc71",
    "amarillo":    "#f39c12",
    "rojo":        "#e74c3c",
    "borde":       "#30363d",
}

# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 3 — CARGA DE DATOS
# ─────────────────────────────────────────────────────────────────────────────

def _leer_hoja(ruta: str, hoja: str, header_row: int = 1) -> pd.DataFrame:
    """Lee una hoja del Excel dado el índice de fila de encabezados."""
    try:
        df = pd.read_excel(ruta, sheet_name=hoja, header=header_row)
        df.columns = [str(c).strip() for c in df.columns]
        df = df.dropna(how="all")
        # Eliminar filas que son títulos embebidos (comienzan con emoji)
        mask = df.iloc[:, 0].astype(str).str.match(r'^[📅📊⚙️📜⚠️🔍]')
        df = df[~mask]
        df = df.reset_index(drop=True)
        return df
    except Exception as e:
        print(f"  ⚠️  Error en hoja {hoja}: {e}")
        return pd.DataFrame()


def cargar_datos(ruta_excel: str) -> dict:
    """Carga y retorna todas las hojas relevantes del Excel."""
    # Todas las hojas tienen título en fila 0, encabezados en fila 1
    datos = {
        "master":       _leer_hoja(ruta_excel, "MASTER_ACTIVIDADES", 1),
        "certificados": _leer_hoja(ruta_excel, "CERTIFICADOS",       1),
        "plan_semanal": _leer_hoja(ruta_excel, "PLAN_SEMANAL",       1),
        "ncs":          _leer_hoja(ruta_excel, "REGISTRO_NC",        1),
        "avance":       _leer_hoja(ruta_excel, "AVANCE",             1),
    }
    return datos


def calcular_kpis(datos: dict) -> dict:
    """Calcula KPIs ejecutivos desde los DataFrames."""
    kpis = {
        "total_actividades":      0,
        "avance_ponderado":       0.0,
        "ncs_abiertas":           0,
        "certificados_entregados":0,
        "proyectos_activos":      0,
        "semaforo": "rojo",
        "semaforo_color": C["rojo"],
        "semaforo_emoji": "🔴",
    }

    # Total actividades
    if not datos["master"].empty:
        df = datos["master"]
        id_col = next((c for c in df.columns if c.upper() == "ID"), None)
        if id_col:
            df_valid = df[df[id_col].astype(str).str.startswith(("QA","QC"))]
            kpis["total_actividades"] = len(df_valid)

    # Avance ponderado (suma de col AVANCE PONDERADO o % AVANCE)
    if not datos["avance"].empty:
        df = datos["avance"]
        # Preferir columna AVANCE PONDERADO
        pond_col = next((c for c in df.columns if "PONDER" in c.upper()), None)
        if not pond_col:
            pond_col = next((c for c in df.columns if "% AVANCE" in c.upper() or "AVANCE" in c.upper()), None)
        if pond_col:
            vals = pd.to_numeric(df[pond_col], errors="coerce").dropna()
            total = float(vals.sum())
            # Si los valores parecen porcentuales (0–100), normalizar
            if total > 1:
                kpis["avance_ponderado"] = min(total / 100.0, 1.0)
            else:
                kpis["avance_ponderado"] = min(total, 1.0)

    # NCs abiertas
    if not datos["ncs"].empty:
        df = datos["ncs"]
        estado_col = next((c for c in df.columns if "ESTADO" in c.upper()), None)
        if estado_col:
            kpis["ncs_abiertas"] = int(
                df[estado_col].astype(str).str.contains("Abierta", case=False, na=False).sum()
            )

    # Certificados entregados
    if not datos["certificados"].empty:
        df = datos["certificados"]
        # Columna ENTREGADO numérica
        ent_col = next((c for c in df.columns if c.upper() == "ENTREGADO"), None)
        if ent_col:
            kpis["certificados_entregados"] = int(
                pd.to_numeric(df[ent_col], errors="coerce").fillna(0).sum()
            )
        else:
            estado_col = next((c for c in df.columns if "ESTADO" in c.upper()), None)
            if estado_col:
                kpis["certificados_entregados"] = int(
                    df[estado_col].astype(str).str.contains("Entreg|Complet", case=False, na=False).sum()
                )

    # Proyectos activos
    if not datos["master"].empty:
        proy_col = next((c for c in datos["master"].columns if "PROYECTO" in c.upper()), None)
        if proy_col:
            kpis["proyectos_activos"] = datos["master"][proy_col].nunique()

    # Semáforo
    pct = kpis["avance_ponderado"] * 100
    if pct >= 90:
        kpis.update({"semaforo":"verde",   "semaforo_color":C["verde"],    "semaforo_emoji":"✅"})
    elif pct >= 70:
        kpis.update({"semaforo":"amarillo","semaforo_color":C["amarillo"], "semaforo_emoji":"⚠️"})
    else:
        kpis.update({"semaforo":"rojo",    "semaforo_color":C["rojo"],     "semaforo_emoji":"🔴"})

    return kpis


# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 4 — GRÁFICOS
# ─────────────────────────────────────────────────────────────────────────────

_LAYOUT = dict(
    plot_bgcolor  = C["card"],
    paper_bgcolor = C["card"],
    font=dict(color=C["blanco"], family="Segoe UI, sans-serif", size=12),
    margin=dict(l=40, r=20, t=50, b=40),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=C["blanco"])),
)


def fig_qa_vs_qc(datos):
    fig = go.Figure()
    df = datos.get("master", pd.DataFrame())
    if df.empty:
        return fig.update_layout(**_LAYOUT, title="Sin datos")

    tipo_col = next((c for c in df.columns if c.upper() == "TIPO"), None)
    proy_col = next((c for c in df.columns if "PROYECTO" in c.upper()), None)
    if not tipo_col or not proy_col:
        return fig.update_layout(**_LAYOUT, title="Columnas no encontradas")

    agrup = df.groupby([proy_col, tipo_col]).size().reset_index(name="n")
    agrup["proy_s"] = agrup[proy_col].apply(lambda x: str(x).split("_")[-1][:18])

    for tipo, color in [("QA", C["azul"]), ("QC", C["verde"])]:
        sub = agrup[agrup[tipo_col] == tipo]
        fig.add_trace(go.Bar(
            name=tipo, x=sub["proy_s"], y=sub["n"],
            marker_color=color,
            marker_line=dict(color=C["bg"], width=1),
            text=sub["n"], textposition="inside",
            textfont=dict(color="white", size=11),
        ))

    fig.update_layout(
        **_LAYOUT,
        title=dict(text="⚙️ Actividades QA vs QC por Proyecto",
                   font=dict(color=C["blanco"], size=13), x=0.02),
        barmode="stack",
        xaxis=dict(gridcolor=C["borde"], title="Proyecto"),
        yaxis=dict(gridcolor=C["borde"], title="# Actividades"),
    )
    return fig


def fig_semanal(datos):
    fig = go.Figure()
    df = datos.get("plan_semanal", pd.DataFrame())
    if df.empty:
        return fig.update_layout(**_LAYOUT, title="Sin datos semanales")

    sem_col  = next((c for c in df.columns if "SEMANA" in c.upper()), None)
    prog_col = next((c for c in df.columns if "PROGRAM" in c.upper()), None)
    ejec_col = next((c for c in df.columns if "EJECUT" in c.upper()), None)
    if not all([sem_col, prog_col, ejec_col]):
        return fig.update_layout(**_LAYOUT, title="Columnas no encontradas")

    df = df.copy()
    df[prog_col] = pd.to_numeric(df[prog_col], errors="coerce").fillna(0)
    df[ejec_col] = pd.to_numeric(df[ejec_col], errors="coerce").fillna(0)
    agrup = df.groupby(sem_col)[[prog_col, ejec_col]].sum().reset_index()
    agrup = agrup[agrup[sem_col].astype(str).str.startswith("S")].sort_values(sem_col)

    fig.add_trace(go.Scatter(
        x=agrup[sem_col], y=agrup[prog_col], name="Programado",
        mode="lines+markers",
        line=dict(color=C["azul"], width=2.5, dash="dash"),
        marker=dict(size=7, color=C["azul"]),
    ))
    fig.add_trace(go.Scatter(
        x=agrup[sem_col], y=agrup[ejec_col], name="Ejecutado",
        mode="lines+markers",
        line=dict(color=C["verde"], width=2.5),
        marker=dict(size=7, color=C["verde"]),
        fill="tonexty", fillcolor="rgba(46,204,113,0.08)",
    ))
    fig.update_layout(
        **_LAYOUT,
        title=dict(text="📅 Cumplimiento Semanal — Programado vs Ejecutado",
                   font=dict(color=C["blanco"], size=13), x=0.02),
        xaxis=dict(gridcolor=C["borde"], title="Semana"),
        yaxis=dict(gridcolor=C["borde"], title="Actividades"),
    )
    return fig


def fig_certificados(datos):
    fig = go.Figure()
    df = datos.get("certificados", pd.DataFrame())
    if df.empty:
        return fig.update_layout(**_LAYOUT, title="Sin datos de certificados")

    estado_col = next((c for c in df.columns if "ESTADO" in c.upper()), None)
    if not estado_col:
        return fig.update_layout(**_LAYOUT, title="Columna ESTADO no encontrada")

    conteo = df[estado_col].astype(str).value_counts()
    conteo = conteo[~conteo.index.str.contains("nan|None|ESTADO", case=False, na=False)]
    colores = [C["verde"] if ("Entreg" in l or "Complet" in l) else
               C["amarillo"] if "Parcial" in l else C["rojo"]
               for l in conteo.index]

    fig.add_trace(go.Pie(
        labels=conteo.index, values=conteo.values, hole=0.55,
        marker=dict(colors=colores, line=dict(color=C["bg"], width=2)),
        textinfo="label+percent", textfont=dict(color="white", size=11),
    ))
    fig.update_layout(
        **_LAYOUT,
        title=dict(text="📜 Estado de Certificados",
                   font=dict(color=C["blanco"], size=13), x=0.02),
    )
    return fig


def fig_avance_tipo(datos):
    fig = go.Figure()
    df = datos.get("avance", pd.DataFrame())
    if df.empty:
        return fig.update_layout(**_LAYOUT, title="Sin datos de avance")

    tipo_col  = next((c for c in df.columns if c.upper() == "TIPO"), None)
    avance_col = next((c for c in df.columns if "PONDER" in c.upper()), None)
    if not avance_col:
        avance_col = next((c for c in df.columns if "% AVANCE" in c.upper()), None)
    if not tipo_col or not avance_col:
        return fig.update_layout(**_LAYOUT, title="Columnas no encontradas")

    df = df.copy()
    df[avance_col] = pd.to_numeric(df[avance_col], errors="coerce").fillna(0)
    agrup = df.groupby(tipo_col)[avance_col].sum().reset_index()
    colores = [C["azul"] if t == "QA" else C["verde"] for t in agrup[tipo_col]]

    fig.add_trace(go.Bar(
        x=agrup[avance_col], y=agrup[tipo_col], orientation="h",
        marker=dict(color=colores, line=dict(color=C["bg"], width=1)),
        text=[f"{v:.1f}" for v in agrup[avance_col]],
        textposition="outside", textfont=dict(color=C["blanco"]),
    ))
    fig.update_layout(
        **_LAYOUT,
        title=dict(text="📊 Avance Ponderado por Tipo QA/QC",
                   font=dict(color=C["blanco"], size=13), x=0.02),
        xaxis=dict(gridcolor=C["borde"], title="Avance Ponderado"),
        yaxis=dict(gridcolor=C["borde"]),
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 5 — EXPORTACIÓN HTML ESTÁTICO
# ─────────────────────────────────────────────────────────────────────────────

def exportar_html(datos, kpis, ruta="QA_QC_PRO_PORTAFOLIO.html"):
    """Genera el HTML portafolio standalone con Plotly embebido."""

    avance_pct = kpis["avance_ponderado"] * 100

    figs = {
        "qa_qc":   fig_qa_vs_qc(datos),
        "semanal": fig_semanal(datos),
        "cert":    fig_certificados(datos),
        "avance":  fig_avance_tipo(datos),
    }

    # Tabla NC
    def tabla_nc():
        df = datos.get("ncs", pd.DataFrame())
        if df.empty:
            return '<p style="color:#8b949e;padding:10px">Sin registros de NC</p>'
        estado_col = next((c for c in df.columns if "ESTADO" in c.upper()), None)
        df_open = df[df[estado_col].astype(str).str.contains("Abierta", case=False, na=False)] if estado_col else df
        if df_open.empty:
            return f'<p style="color:{C["verde"]};padding:10px;font-size:14px">✅ No hay NCs abiertas actualmente</p>'
        cols = [c for c in df.columns if any(k.upper() in c.upper() for k in ["N° NC","FECHA","PROYECTO","DESCRIPCIÓN","ESTADO","FECHA LÍMITE"])]
        if not cols: cols = df.columns[:6].tolist()
        df_s = df_open[cols]
        h = '<table style="width:100%;border-collapse:collapse"><thead><tr>'
        for col in df_s.columns:
            h += f'<th style="background:{C["azul_p"]};color:{C["blanco"]};padding:8px 12px;font-size:11px;border:1px solid {C["borde"]};white-space:nowrap">{col}</th>'
        h += "</tr></thead><tbody>"
        for i,(_, row) in enumerate(df_s.iterrows()):
            bg = C["card"] if i%2==0 else C["panel"]
            h += "<tr>"
            for val in row:
                txt = str(val)[:70] if pd.notna(val) else "—"
                color = C["rojo"] if "Abierta" in txt else C["blanco"]
                h += f'<td style="background:{bg};color:{color};padding:7px 12px;font-size:11px;border:1px solid {C["borde"]}">{txt}</td>'
            h += "</tr>"
        h += "</tbody></table>"
        return h

    # Inyección de figuras Plotly
    scripts = ""
    for fid, fkey in [("fig-qa-qc","qa_qc"),("fig-semanal","semanal"),("fig-cert","cert"),("fig-avance","avance")]:
        fk2 = fkey.replace("-","_")
        scripts += f"""
var _d{fk2}={figs[fkey].to_json()};
Plotly.newPlot('{fid}',_d{fk2}.data,_d{fk2}.layout,{{responsive:true,displayModeBar:false}});
"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>QA/QC PRO PORTAFOLIO — {CONFIG['nombre']}</title>
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',-apple-system,sans-serif;background:{C['bg']};color:{C['blanco']};min-height:100vh}}
.hdr{{background:{C['panel']};border-bottom:1px solid {C['borde']};padding:18px 32px;display:flex;justify-content:space-between;align-items:center}}
.hdr h1{{font-size:22px;font-weight:700}}
.hdr .sub{{font-size:12px;color:{C['acento']};margin-top:4px;font-weight:600}}
.hdr .meta{{font-size:11px;color:{C['gris']};text-align:right}}
.body{{padding:28px 32px}}
.s-title{{font-size:16px;font-weight:600;color:{C['blanco']};margin-bottom:4px}}
.s-desc{{font-size:12px;color:{C['gris']};margin-bottom:12px}}
hr{{border:none;border-top:1px solid {C['borde']};margin-bottom:20px}}
.kpi-row{{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:24px}}
.kpi-card{{background:{C['card']};border:1px solid {C['borde']};border-radius:10px;padding:20px 24px;flex:1;min-width:140px}}
.kpi-icon{{font-size:20px;margin-right:8px}}
.kpi-lbl{{font-size:11px;color:{C['gris']};font-weight:600;letter-spacing:1px;text-transform:uppercase}}
.kpi-val{{font-size:38px;font-weight:700;line-height:1;margin:8px 0 4px}}
.kpi-sub{{font-size:11px;color:{C['gris']}}}
.kpi-bar{{height:3px;width:40px;border-radius:2px;margin-top:12px}}
.prog-box{{background:{C['card']};border:1px solid {C['borde']};border-radius:10px;padding:16px 20px;margin-bottom:28px}}
.prog-bg{{background:{C['panel']};border-radius:6px;overflow:hidden;height:12px;border:1px solid {C['borde']}}}
.prog-fill{{height:12px;border-radius:6px}}
.charts-row{{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:16px}}
.chart-card{{background:{C['card']};border:1px solid {C['borde']};border-radius:10px;padding:8px;flex:1;min-width:280px}}
.nc-box{{background:{C['card']};border:1px solid {C['borde']};border-radius:10px;padding:16px;overflow-x:auto;margin-bottom:28px}}
.footer{{padding:20px 32px;border-top:1px solid {C['borde']};font-size:11px;color:{C['gris']}}}
.btn-pdf{{background:{C['azul_p']};color:{C['blanco']};border:none;padding:10px 22px;border-radius:6px;font-size:13px;cursor:pointer;font-family:inherit;font-weight:600;letter-spacing:.5px}}
.btn-pdf:hover{{background:{C['azul']}}}
@media print{{.btn-pdf{{display:none}}.chart-card{{page-break-inside:avoid}}}}
</style>
</head>
<body>

<div class="hdr">
  <div>
    <h1>⚡ QA/QC PRO PORTAFOLIO</h1>
    <div class="sub">{CONFIG['nombre']} — {CONFIG['especialidad']}</div>
  </div>
  <div class="meta">
    <div>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    <div style="margin-top:4px">Estado: <span style="color:{kpis['semaforo_color']};font-weight:700">{kpis['semaforo_emoji']} {kpis['semaforo'].upper()}</span></div>
    <div style="margin-top:8px"><button class="btn-pdf" onclick="window.print()">🖨️ Exportar PDF</button></div>
  </div>
</div>

<div class="body">

  <!-- KPIs -->
  <p class="s-title">📊 Indicadores Clave de Desempeño (KPIs)</p>
  <p class="s-desc">Resumen ejecutivo del estado del proyecto</p>
  <hr>
  <div class="kpi-row">
    <div class="kpi-card">
      <div><span class="kpi-icon">📋</span><span class="kpi-lbl">Total Actividades</span></div>
      <div class="kpi-val" style="color:{C['acento']}">{kpis['total_actividades']}</div>
      <div class="kpi-sub">Actividades registradas</div>
      <div class="kpi-bar" style="background:{C['acento']}"></div>
    </div>
    <div class="kpi-card">
      <div><span class="kpi-icon">📊</span><span class="kpi-lbl">Avance Ponderado</span></div>
      <div class="kpi-val" style="color:{kpis['semaforo_color']}">{avance_pct:.1f}%</div>
      <div class="kpi-sub">Progreso general del proyecto</div>
      <div class="kpi-bar" style="background:{kpis['semaforo_color']}"></div>
    </div>
    <div class="kpi-card">
      <div><span class="kpi-icon">⚠️</span><span class="kpi-lbl">NCs Abiertas</span></div>
      <div class="kpi-val" style="color:{C['rojo'] if kpis['ncs_abiertas']>0 else C['verde']}">{kpis['ncs_abiertas']}</div>
      <div class="kpi-sub">No conformidades pendientes</div>
      <div class="kpi-bar" style="background:{C['rojo'] if kpis['ncs_abiertas']>0 else C['verde']}"></div>
    </div>
    <div class="kpi-card">
      <div><span class="kpi-icon">📜</span><span class="kpi-lbl">Certificados</span></div>
      <div class="kpi-val" style="color:{C['verde']}">{kpis['certificados_entregados']}</div>
      <div class="kpi-sub">Certificados entregados</div>
      <div class="kpi-bar" style="background:{C['verde']}"></div>
    </div>
    <div class="kpi-card">
      <div><span class="kpi-icon">🏗️</span><span class="kpi-lbl">Proyectos Activos</span></div>
      <div class="kpi-val" style="color:{C['azul']}">{kpis['proyectos_activos']}</div>
      <div class="kpi-sub">Proyectos en gestión</div>
      <div class="kpi-bar" style="background:{C['azul']}"></div>
    </div>
  </div>

  <!-- Semáforo -->
  <div class="prog-box">
    <div style="font-size:13px;margin-bottom:8px">
      <strong style="color:{kpis['semaforo_color']}">{kpis['semaforo_emoji']} Semáforo de Avance: {kpis['semaforo'].upper()} — {avance_pct:.1f}%</strong>
    </div>
    <div class="prog-bg">
      <div class="prog-fill" style="width:{min(avance_pct,100):.1f}%;background:{kpis['semaforo_color']};box-shadow:0 0 8px {kpis['semaforo_color']}60"></div>
    </div>
    <div style="font-size:10px;margin-top:6px">
      <span style="color:{C['rojo']};margin-right:14px">🔴 Rojo &lt;70%</span>
      <span style="color:{C['amarillo']};margin-right:14px">⚠️ Amarillo 70–89%</span>
      <span style="color:{C['verde']}">✅ Verde ≥90%</span>
    </div>
  </div>

  <!-- Gráficos -->
  <p class="s-title" style="margin-top:8px">📈 Gráficos Gerenciales</p>
  <p class="s-desc">Análisis visual del desempeño QA/QC por proyecto y semana</p>
  <hr>
  <div class="charts-row">
    <div class="chart-card"><div id="fig-qa-qc" style="min-height:320px"></div></div>
    <div class="chart-card"><div id="fig-semanal" style="min-height:320px"></div></div>
  </div>
  <div class="charts-row">
    <div class="chart-card"><div id="fig-cert" style="min-height:300px"></div></div>
    <div class="chart-card"><div id="fig-avance" style="min-height:300px"></div></div>
  </div>

  <!-- Certificados -->
  <p class="s-title" style="margin-top:12px">📜 Resumen de Certificados</p>
  <p class="s-desc">Estado de certificados de calibración y conformidad de materiales</p>
  <hr>
  <div class="kpi-row" style="margin-bottom:28px">
    <div class="kpi-card" style="flex:0 0 180px;text-align:center">
      <div class="kpi-val" style="color:{C['verde']};font-size:52px">{kpis['certificados_entregados']}</div>
      <div class="kpi-sub" style="font-size:13px">Certificados Entregados</div>
    </div>
    <div class="chart-card" style="flex:1">
      <div id="fig-cert2" style="height:200px"></div>
    </div>
  </div>

  <!-- NCs -->
  <p class="s-title">⚠️ Registro de No Conformidades Abiertas</p>
  <p class="s-desc">NCs activas que requieren gestión y cierre inmediato</p>
  <hr>
  <div class="nc-box">{tabla_nc()}</div>

</div>

<div class="footer">
  ⚡ {CONFIG['nombre']} — {CONFIG['especialidad']} &nbsp;|&nbsp;
  QA/QC PRO PORTAFOLIO v10 &nbsp;|&nbsp; {datetime.now().year}
</div>

<script>
{scripts}
// Duplicar gráfico certificados en segunda sección
var _dcert2={figs['cert'].to_json()};
Plotly.newPlot('fig-cert2',_dcert2.data,_dcert2.layout,{{responsive:true,displayModeBar:false}});
</script>
</body>
</html>"""

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ HTML exportado: {ruta}")
    return ruta


# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 6 — LAYOUT DASH (Servidor Interactivo)
# ─────────────────────────────────────────────────────────────────────────────

def kpi_card(icono, titulo, valor, sub, color):
    return html.Div([
        html.Div([html.Span(icono,style={"fontSize":"20px","marginRight":"8px"}),
                  html.Span(titulo,style={"fontSize":"11px","color":C["gris"],"fontWeight":"600","letterSpacing":"1px","textTransform":"uppercase"})],
                 style={"display":"flex","alignItems":"center","marginBottom":"10px"}),
        html.Div(str(valor),style={"fontSize":"38px","fontWeight":"700","color":color,"lineHeight":"1","marginBottom":"6px"}),
        html.Div(sub,style={"fontSize":"11px","color":C["gris"]}),
        html.Div(style={"height":"3px","width":"40px","backgroundColor":color,"marginTop":"12px","borderRadius":"2px"}),
    ],style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px","padding":"20px 24px","flex":"1","minWidth":"140px"})


def crear_layout(datos, kpis):
    avance_pct = kpis["avance_ponderado"] * 100
    F = {"fontFamily":"Segoe UI,-apple-system,sans-serif","background":C["bg"],"minHeight":"100vh","color":C["blanco"]}

    return html.Div([

        # Header
        html.Div([
            html.Div([
                html.H1("⚡ QA/QC PRO PORTAFOLIO",
                        style={"fontSize":"22px","fontWeight":"700","color":C["blanco"],"margin":"0"}),
                html.Div([html.Span("⚡ ",style={"color":C["acento"]}),
                          html.Span(CONFIG["nombre"],style={"color":C["acento"],"fontWeight":"600"}),
                          html.Span("  —  "+CONFIG["especialidad"],style={"color":C["gris"],"fontSize":"12px"})],
                         style={"marginTop":"4px"}),
            ]),
            html.Div([
                html.Div(f"Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
                         style={"fontSize":"11px","color":C["gris"]}),
                html.Div([html.Span("Estado: ",style={"color":C["gris"],"fontSize":"12px"}),
                          html.Span(f"{kpis['semaforo_emoji']} {kpis['semaforo'].upper()}",
                                    style={"color":kpis["semaforo_color"],"fontWeight":"700","fontSize":"12px"})],
                         style={"marginTop":"4px"}),
            ],style={"textAlign":"right"}),
        ],style={"display":"flex","justifyContent":"space-between","alignItems":"flex-start",
                 "background":C["panel"],"borderBottom":f"1px solid {C['borde']}","padding":"16px 28px"}),

        # Body
        html.Div([
            # KPIs
            html.H3("📊 Indicadores Clave de Desempeño",
                    style={"fontSize":"16px","fontWeight":"600","margin":"0 0 4px","color":C["blanco"]}),
            html.P("Resumen ejecutivo del estado del proyecto",
                   style={"fontSize":"12px","color":C["gris"],"margin":"0 0 12px"}),
            html.Hr(style={"borderColor":C["borde"],"margin":"0 0 20px"}),

            html.Div([
                kpi_card("📋","Total Actividades",kpis["total_actividades"],"Actividades registradas",C["acento"]),
                kpi_card("📊","Avance Ponderado",f"{avance_pct:.1f}%","Progreso general",kpis["semaforo_color"]),
                kpi_card("⚠️","NCs Abiertas",kpis["ncs_abiertas"],"No conformidades",C["rojo"] if kpis["ncs_abiertas"]>0 else C["verde"]),
                kpi_card("📜","Certificados",kpis["certificados_entregados"],"Certificados entregados",C["verde"]),
                kpi_card("🏗️","Proyectos Activos",kpis["proyectos_activos"],"Proyectos en gestión",C["azul"]),
            ],style={"display":"flex","gap":"16px","flexWrap":"wrap","marginBottom":"24px"}),

            # Semáforo
            html.Div([
                html.Div([html.Span("Semáforo de Avance: ",style={"color":C["gris"],"fontSize":"12px","marginRight":"8px"}),
                          html.Span(f"{kpis['semaforo_emoji']} {kpis['semaforo'].upper()} — {avance_pct:.1f}%",
                                    style={"color":kpis["semaforo_color"],"fontWeight":"700","fontSize":"14px"})],
                         style={"marginBottom":"8px"}),
                html.Div(html.Div(style={"height":"12px","width":f"{min(avance_pct,100):.1f}%",
                                         "background":kpis["semaforo_color"],"borderRadius":"6px"}),
                         style={"background":C["panel"],"borderRadius":"6px","border":f"1px solid {C['borde']}","overflow":"hidden"}),
                html.Div([html.Span("🔴 Rojo <70%",style={"color":C["rojo"],"fontSize":"10px","marginRight":"14px"}),
                          html.Span("⚠️ Amarillo 70–89%",style={"color":C["amarillo"],"fontSize":"10px","marginRight":"14px"}),
                          html.Span("✅ Verde ≥90%",style={"color":C["verde"],"fontSize":"10px"})],
                         style={"marginTop":"6px"}),
            ],style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px",
                     "padding":"16px 20px","marginBottom":"28px"}),

            # Gráficos
            html.H3("📈 Gráficos Gerenciales",
                    style={"fontSize":"16px","fontWeight":"600","margin":"8px 0 4px","color":C["blanco"]}),
            html.P("Análisis visual del desempeño QA/QC",
                   style={"fontSize":"12px","color":C["gris"],"margin":"0 0 12px"}),
            html.Hr(style={"borderColor":C["borde"],"margin":"0 0 20px"}),

            html.Div([
                html.Div(dcc.Graph(figure=fig_qa_vs_qc(datos),config={"displayModeBar":False}),
                         style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px","padding":"8px","flex":"1","minWidth":"280px"}),
                html.Div(dcc.Graph(figure=fig_semanal(datos),config={"displayModeBar":False}),
                         style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px","padding":"8px","flex":"1","minWidth":"280px"}),
            ],style={"display":"flex","gap":"16px","flexWrap":"wrap","marginBottom":"16px"}),

            html.Div([
                html.Div(dcc.Graph(figure=fig_certificados(datos),config={"displayModeBar":False}),
                         style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px","padding":"8px","flex":"1","minWidth":"260px"}),
                html.Div(dcc.Graph(figure=fig_avance_tipo(datos),config={"displayModeBar":False}),
                         style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px","padding":"8px","flex":"1","minWidth":"260px"}),
            ],style={"display":"flex","gap":"16px","flexWrap":"wrap","marginBottom":"28px"}),

            # NCs
            html.H3("⚠️ No Conformidades Abiertas",
                    style={"fontSize":"16px","fontWeight":"600","margin":"8px 0 4px","color":C["blanco"]}),
            html.P("NCs activas que requieren gestión y cierre",
                   style={"fontSize":"12px","color":C["gris"],"margin":"0 0 12px"}),
            html.Hr(style={"borderColor":C["borde"],"margin":"0 0 20px"}),

            html.Div(_tabla_nc_dash(datos),
                     style={"background":C["card"],"border":f"1px solid {C['borde']}","borderRadius":"10px",
                            "padding":"16px","overflowX":"auto","marginBottom":"28px"}),

            # Footer
            html.Hr(style={"borderColor":C["borde"]}),
            html.P(f"⚡ {CONFIG['nombre']} — {CONFIG['especialidad']} | QA/QC PRO v10 | {datetime.now().year}",
                   style={"fontSize":"11px","color":C["gris"],"paddingBottom":"20px"}),

        ],style={"padding":"24px 28px"}),

    ],style=F)


def _tabla_nc_dash(datos):
    """Tabla Dash de NCs abiertas."""
    df = datos.get("ncs", pd.DataFrame())
    if df.empty:
        return html.Div("Sin registros de NC", style={"color":C["gris"],"padding":"20px"})
    estado_col = next((c for c in df.columns if "ESTADO" in c.upper()), None)
    df_open = df[df[estado_col].astype(str).str.contains("Abierta", case=False, na=False)] if estado_col else df
    if df_open.empty:
        return html.Div("✅ No hay NCs abiertas actualmente",
                        style={"color":C["verde"],"padding":"20px","fontSize":"14px"})
    cols = [c for c in df.columns if any(k in c.upper() for k in ["N° NC","FECHA","PROYECTO","DESCRIPCIÓN","ESTADO","FECHA LÍMITE"])]
    if not cols: cols = df.columns[:5].tolist()
    df_s = df_open[cols]

    header = html.Tr([html.Th(c,style={"background":C["azul_p"],"color":C["blanco"],"padding":"8px 12px",
                                         "fontSize":"11px","fontWeight":"600","border":f"1px solid {C['borde']}",
                                         "whiteSpace":"nowrap"}) for c in df_s.columns])
    rows = []
    for i,(_,row) in enumerate(df_s.iterrows()):
        bg = C["card"] if i%2==0 else C["panel"]
        rows.append(html.Tr([
            html.Td(str(v)[:60] if pd.notna(v) else "—",
                    style={"background":bg,"color":C["rojo"] if "Abierta" in str(v) else C["blanco"],
                           "padding":"7px 12px","fontSize":"11px","border":f"1px solid {C['borde']}"})
            for v in row
        ]))
    return html.Table([html.Thead(header),html.Tbody(rows)],
                      style={"width":"100%","borderCollapse":"collapse"})


# ─────────────────────────────────────────────────────────────────────────────
# MÓDULO 7 — PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "═"*60)
    print("  ⚡ QA/QC PRO PORTAFOLIO — Ingeniero Yesid Cruz")
    print("  QA/QC Eléctrico & Instrumentación")
    print("═"*60)

    # Buscar el Excel
    ruta = CONFIG["excel_file"]
    for alt in [ruta, "QA_QC_PRO_DASHBOARD_v10_YesidCruz__4_.xlsx"]:
        if os.path.exists(alt):
            ruta = alt
            break

    if not os.path.exists(ruta):
        print(f"\n⚠️  Excel no encontrado: {ruta}")
        print("   Coloca el Excel en la misma carpeta que este script.\n")
        datos = {k:pd.DataFrame() for k in ["master","certificados","plan_semanal","ncs","avance"]}
    else:
        print(f"\n📂 Excel: {ruta}")
        datos = cargar_datos(ruta)
        for k,v in datos.items():
            print(f"   ✅ {k}: {len(v)} registros")

    kpis = calcular_kpis(datos)
    pct  = kpis["avance_ponderado"]*100
    print(f"\n📊 KPIs:")
    print(f"   Actividades:   {kpis['total_actividades']}")
    print(f"   Avance:        {pct:.1f}%  {kpis['semaforo_emoji']} {kpis['semaforo'].upper()}")
    print(f"   NCs abiertas:  {kpis['ncs_abiertas']}")
    print(f"   Certificados:  {kpis['certificados_entregados']}")
    print(f"   Proyectos:     {kpis['proyectos_activos']}")

    # Exportar HTML estático
    html_out = "QA_QC_PRO_PORTAFOLIO.html"
    print(f"\n💾 Exportando → {html_out}")
    exportar_html(datos, kpis, html_out)

    # Servidor Dash
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
               title="QA/QC PRO — Yesid Cruz", suppress_callback_exceptions=True)
    app.layout = crear_layout(datos, kpis)

    print(f"\n🌐 Servidor en: http://127.0.0.1:8050")
    print(f"   HTML estático: {html_out}")
    print("═"*60 + "\n")
    app.run(debug=False, host="0.0.0.0", port=8050)


if __name__ == "__main__":
    main()
