---
title: "DeepInfer: el motor de inferencia de producción de DeepSeek, con Ascend como objetivo de primera clase"
source: "https://github.com/deepseek-ai/DeepInfer | https://inf.latent.space/ | https://github.com/deepseek-ai/DeepInfer/blob/main/README.md"
author: "DeepSeek"
date: 2026-10-20
captured: 2026-10-25
---

# DeepInfer

> DeepInfer is the high-performance inference framework that powers DeepSeek's large-scale production services. This open-source release provides offline inference with the core features needed for serving at scale.

Licencia **Apache 2.0**. No es un juguete de referencia: es el stack que sirve su propia API.

## Modelo soportado

`deepseek-ai/DeepSeek-V4.1-Flash-1017` (checkpoint por defecto, descargado a la caché de Hugging Face en el primer arranque; `DEEPINFER_HF_MODEL_DIR` para copia local).

## Capacidades enviadas

- **Kernels optimizados**: FlashMLA, DeepGEMM, DeepEP, TileKernels, DeepSelect y kernels propios en TileLang.
- **Paralelismo**: Attention DP / CP balanceado, MoE EP + EPLB.
- **DSpark y verificación con planificación por confianza**: aceleración de decodificación con tokens borrador; `DEEPINFER_ENABLE_MTP_VARLEN=1` y `DEEPINFER_USE_NEXTN_DECODE` controla la longitud máxima de borrador (por defecto 5).
- **SWA bounded replay**: reduce el trabajo de prefill del decodificador replicando solo un sufijo acotado. `DEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compact` y `DEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140` para V4.1; el sufijo retenido debe cubrir la ventana SWA más la longitud máxima de backtracking.
- **Planificación asíncrona**: solapa el batch scheduling de CPU con la ejecución en dispositivo; activada por defecto (zero-overhead batch scheduler).
- **Inferencia invariante al batch**: resultados idénticos entre composiciones de batch distintas (`DEEPINFER_BATCH_INVARIANT=1`, solo NVIDIA).
- **Muestreo determinista**: mismas salidas para los mismos tokens de entrada y parámetros (`DEEPINFER_BATCH_INVARIANT=1`, `DEEPINFER_ENABLE_MTP_VARLEN=0`, `seq_seed` fijo; solo NVIDIA).
- **Salidas estructuradas**: restricción por regex, JSON Schema o gramática EBNF vía `so_args` en `SamplingParams`.

## Hardware

- GPU NVIDIA SM100.
- **NPU Huawei Ascend 950** — soporte de primera clase, no un fork de la comunidad. En `deepinfer/platform.py`, `PlatformNPU` usa TileLang con backend `asc`, `hccl` como backend distribuido, mapea `torch.cuda.*` sobre `torch.npu.*` vía `torch_npu.contrib.transfer_to_npu`, fija `TILELANG_DEFAULT_TARGET=ascend` y ajusta HCCL (`HCCL_BUFFSIZE=16`, timeouts de 240/200 s). Requiere CANN 9.2; NVIDIA requiere CUDA 13.

## Frontera del release

Lo que **no** incluye, y hace falta para un servicio completo: sistema de KV cache, disaggregación VE/Prefill/Decode (la mayor parte del motor ya está implementada) y balanceo entre réplicas data-parallel para prefill y decode. Esas piezas siguen acopladas a la infraestructura interna.

## Cifras citadas por DeepSeek

- Throughput de un solo clúster: **155 billones de tokens/día**.
- Ingreso: **38 USD por tarjeta-hora** (precios de valle).
- Componente adicional abierto: `deepseek-recipe`, codificador/decodificador de tokens alineado con la lógica de la API oficial, para que despliegues de terceros obtengan la misma experiencia de API.

## Por qué importa

El cuello de botella de los agentes no es solo el razonamiento: es cuántas completaciones por segundo y por dólar puedes permitirte cuando un harness fan-out lanza 1.024 workers, o cuando un bucle único reenvía 16.581 tokens de system prompt en cada paso. Un motor que corre en silicio no-NVIDIA y que se publica bajo Apache 2.0 cambia el denominador de esa ecuación para quien no tiene acceso a H100.
