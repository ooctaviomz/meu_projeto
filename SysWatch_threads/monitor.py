import psutil
import time

def coletar_dados():
    # Porcentagens de uso do sistema
    cpu = psutil.cpu_percent(interval=0.5)
    memoria = psutil.virtual_memory()
    disco = psutil.disk_usage("/")

    # Lista de processos com uso de memória
    processos = []
    for proc in psutil.process_iter(["pid", "name", "memory_info", "memory_percent"]):
        try:
            info = proc.info
            memoria_mb = info["memory_info"].rss / (1024 * 1024)
            processos.append({
                "pid": info["pid"],
                "nome": info["name"],
                "memoria_mb": round(memoria_mb, 1),
                "memoria_pct": round(info["memory_percent"], 1),
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    # Ordena do maior para o menor consumo de memória
    processos.sort(key=lambda p: p["memoria_mb"], reverse=True)

    return {
        "cpu_pct": cpu,
        "memoria_pct": memoria.percent,
        "memoria_total_gb": round(memoria.total / (1024**3), 1),
        "disco_pct": disco.percent,
        "disco_total_gb": round(disco.total / (1024**3), 1),
        "processos": processos[:20],  # top 20
    }
