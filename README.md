# Entorno04 - GeneXus & AI Skill Orchestration

Este entorno está configurado como un espacio de trabajo avanzado para el desarrollo con GeneXus, utilizando una capa de orquestación de agentes de IA basada en la metodología "Nexa" y el ecosistema XPZ/XML.

## 📁 Estructura del Entorno

- **`.agents/skills/`**: Biblioteca local de habilidades sincronizada con la base global.
- **`scripts/`**: Wrappers locales y herramientas de automatización.
- **`XpzExportadosPelaIDE/`**: Carpeta de entrada para archivos `.xpz`.
- **`ObjetosDaKbEmXml/`**: Snapshot oficial de la KB materializado en XML.
- **`KbIntelligence/`**: Índice derivado para triaje técnico y funcional.
- **`ObjetosGeradosParaImportacaoNaKbNoGenexus/`**: Área de trabajo para objetos generados.
- **`PacotesGeradosParaImportacaoNaKbNoGenexus/`**: Área de salida para paquetes de importación.

## 🤖 Orquestación de Agentes

El archivo [AGENTS.md](file:///d:/aaProyectos/Entorno04/AGENTS.md) define los roles y protocolos de interacción. Todos los agentes deben seguir el flujo **A-P-E (Analyze-Plan-Execute)**.

## 🚀 Estado del Proyecto
- **KB Integrada**: `77Lab` (D:\Models\77Lab\AngularV1)
- **Estado de Sincronización**: Materializado e Índice Validado (`GATE_OK`).
- **Orquestación**: MCP Genexus18 Activo.

## 🛠️ Comandos Útiles
- **Sincronizar**: `.\scripts\Update-77LabKbFromXpz.ps1`
- **Auditar**: `.\scripts\Test-77LabKbSetupAudit.ps1`
- **Consultar**: `.\scripts\Query-77LabKbIntelligence.ps1`

---
*Configurado por Antigravity*
