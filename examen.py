# examen
# Importar la libreria pip install nicegui
from nicegui import ui

# Link de referencia https://docs.python.org/es/3/tutorial/datastructures.html#

# Definir Lista
item = [20, 50, 9, 45, 9, 78, 56, 3]

# Definir los metodos para la lista
def render_list():
    # Dibujar los cuadros de memoria de mi lista
    list_container.clear()
    with list_container:
        if not item:
            ui.label('Lista vacía').classes('text-gray-400 italic')
            return

        with ui.row().classes('items-center gap-2 flex-wrap'):
            for idx, val in enumerate(item):
                with ui.column().classes('items-center gap-1'):
                    
                    ui.label(str(val)).classes('w-16 h-16 flex items-center justify-center '
                        'bg-blue-800 text-white font-bold text-lg rounded-lg shadow-md')
                    
                    ui.label(f'[{idx}]*').classes('text-xs font-semibold text-slate-700')

# Metodo append agregar un numero a la lista
def do_append():
    if val_input.value is not None:
        item.append(int(val_input.value))
        render_list() 
    else:
        ui.notify('Error: Debes introducir un valor para usar append().', color='blue')   

# Metodo Insert insertar un numero en la lista en una posicion especifica
def do_insert():
    if val_input.value is not None and idx_input.value is not None:
        idx = max(0, min(int(idx_input.value), len(item)))
        item.insert(idx, int(val_input.value))
        render_list()
    else:
        ui.notify('Error: Faltan datos (Valor o Índice) para realizar insert().', color='blue')

# Metodo Pop eliminar un numero de acuerdo a su indice, si no se especifica llega un mensaje de error
def do_pop():
    if not item:
        ui.notify('Error: La lista está vacía, no se puede hacer pop().', color='blue')
        return
    
    if idx_input.value is not None:
        idx = int(idx_input.value)
        if 0 <= idx < len(item):
            item.pop(idx)
            render_list()
        else:
            ui.notify(f'Error: Índice {idx} fuera de rango.', color='blue')

# Metodo Clear borra todos los elementos de la lista
def do_clear():
    item.clear()
    render_list()

# Metodo Count cuenta cuantas veces aparece un numero en la lista.
def do_count():
    if val_input.value is not None:
        val = int(val_input.value)
        cantidad = item.count(val)
        ui.notify(f'El valor {val} aparece {cantidad} vez(veces) en la lista.', color='info')
    else:
        ui.notify('Error: Ingresa un valor en el campo "Valor" para contar.', color='blue')

# Metodo Reverse voltea la lista, el primer elemento pasa a ser el ultimo y el ultimo pasa a ser el primero sin ordenar de mayor a menor solo invisrte la lista.
def do_reverse():
    item.reverse()
    render_list()

# Metodo Remove elimina el numero introducuido en el campo valor y borra el primer numero que este en la lista si es que hay dos iguales.
def do_remove():
    if val_input.value is not None:
        val = int(val_input.value)
        if val in item:
            item.remove(val)
            render_list()
        else:
            ui.notify(f'Error: El valor {val} no existe en la lista.', color='blue')
    else:
        ui.notify('Error: Ingresa el valor que deseas eliminar.', color='blue')

# Metodo Sort ordena de mayor a menor la lista
def do_sort():
    item.sort()
    render_list()

# titulo de la pagina en el navegador 
ui.page_title('Visualizador de Listas en Python con NiceGui')


with ui.column().classes('p-6 gap-6 w-full'):
    ui.label('Practica Grafica de una Lista').classes('text-2xl font-bold text-slate-800')

    with ui.card().classes('w-full p-4 min-h-[140px] bg-slate-50 border-slate-200'):
        list_container = ui.row().classes('w-full items-center')

    with ui.card().classes('w-full p-4 gap-4'):
        ui.label('OPERACIONES').classes('text-sm font-semibold text-slate-500')   

        with ui.row().classes('gap-4 items-center'):
            val_input = ui.number('Valor', placeholder="Introduce un número").classes('w-40')
            idx_input = ui.number('Indice', value=0, min=0).classes('w-40')

        
        with ui.row().classes('gap-2 flex-wrap'):
            ui.button('append(x)', icon='add', color='secondary', on_click=do_append)
            ui.button('insert(i, x)', icon='add_circle', color='info', on_click=do_insert)
            ui.button('pop(i)', icon='remove', color='warning', on_click=do_pop)
            ui.button('clear()', icon='delete', color='red', on_click=do_clear)
            ui.button('remove(x)', icon='remove_circle', color='orange', on_click=do_remove)
            ui.button('count(x)', icon='numbers', color='teal', on_click=do_count)
            ui.button('sort()', icon='sort_by_alpha', color='indigo', on_click=do_sort)
            ui.button('reverse()', icon='swap_horiz', color='purple', on_click=do_reverse)

render_list()
ui.run()
