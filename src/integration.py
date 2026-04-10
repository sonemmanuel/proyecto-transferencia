from pathlib import Path
from datetime import datetime
from pandas import DataFrame
from colorama import Fore, Style
from file import load_data

# Ruta del directorio data/ relativa a este archivo
DATA_DIR = (Path(__file__).resolve().parent / "../data").resolve()

def generate_report(users_data, *args, **kwargs):
    if not users_data:
        print(f"{Fore.RED}✗ No hay datos para generar reporte.{Style.RESET_ALL}")
        return None
    
    try:
        df = DataFrame(users_data)
        group_by = kwargs.get('group_by', None)
        show_stats = kwargs.get('show_stats', True)
        
        # Mostrar encabezado
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"Reporte de Usuarios - {timestamp}")
        print(f"{'='*60}{Style.RESET_ALL}")
        
        # Agrupar si se especifica
        if group_by and group_by in df.columns:
            grouped = df.groupby(group_by)
            print(f"\n{Fore.YELLOW}Datos agrupados por: {group_by}{Style.RESET_ALL}")
            for name, group in grouped:
                print(f"\n{Fore.GREEN}{group_by.capitalize()}: {name}{Style.RESET_ALL}")
                print(group.to_string(index=False))
                print(f"Cantidad: {len(group)}")
        else:
            print(f"\n{Fore.YELLOW}Total de registros: {len(df)}{Style.RESET_ALL}")
            print(df.to_string(index=False))
        
        # Mostrar estadísticas
        if show_stats:
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"Estadísticas{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
            print(f"Total de usuarios: {len(df)}")
            print(f"Edad promedio: {df['age'].mean():.1f} años")
            print(f"Edad máxima: {df['age'].max()} años")
            print(f"Edad mínima: {df['age'].min()} años")
            
            # Contar por estado
            if 'status' in df.columns:
                status_counts = df['status'].value_counts()
                print(f"\n{Fore.YELLOW}Estado de usuarios:{Style.RESET_ALL}")
                for status, count in status_counts.items():
                    print(f"  {status.capitalize()}: {count}")
        
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        return df
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error al generar reporte: {e}{Style.RESET_ALL}")
        return None

def export_to_csv(users_data=None, *args, **kwargs):
    """Exporta registros a un archivo CSV con filtrado y ordenamiento opcional.
    
    Primero carga los usuarios de data/registros.json si no se proporcionan datos.
    
    Args:
        users_data: Lista de diccionarios con datos de usuarios (opcional)
        *args: Argumentos posicionales (no usado actualmente)
        **kwargs: Argumentos con nombre:
            - 'filename': Nombre del archivo (default: 'reporte.csv')
            - 'filter_status': Filtrar por estado ('activo', 'inactivo')
            - 'sort_by': Columna para ordenar (default: 'id')
            - 'min_age': Edad mínima para filtrar
    
    Returns:
        bool: True si se exportó correctamente, False en caso contrario
    """
    # Cargar datos de registros.json si no se proporcionan
    if not users_data:
        print(f"{Fore.CYAN}Cargando datos de data/registros.json...{Style.RESET_ALL}")
        users_data = load_data()
    
    if not users_data:
        print(f"{Fore.RED}✗ No hay datos para exportar.{Style.RESET_ALL}")
        return False
    
    try:
        # Parámetros con valores por defecto
        filename = kwargs.get('filename', 'reporte.csv')
        filter_status = kwargs.get('filter_status', None)
        sort_by = kwargs.get('sort_by', 'id')
        min_age = kwargs.get('min_age', None)
        
        # Crear DataFrame
        df = DataFrame(users_data)
        
        # Aplicar filtros si se especifican
        if filter_status:
            df = df[df['status'].str.lower() == filter_status.lower()]
        
        if min_age is not None:
            df = df[df['age'] >= min_age]
        
        # Ordenar datos
        if sort_by in df.columns:
            df = df.sort_values(by=sort_by)
        
        # Guardar a CSV
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        output_path = DATA_DIR / filename
        df.to_csv(output_path, index=False, encoding='utf-8')
        
        print(f"{Fore.GREEN}✓ Archivo exportado correctamente: {output_path}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}  Registros exportados: {len(df)}{Style.RESET_ALL}")
        return True
        
    except Exception as e:
        print(f"{Fore.RED}✗ Error al exportar: {e}{Style.RESET_ALL}")
        return False