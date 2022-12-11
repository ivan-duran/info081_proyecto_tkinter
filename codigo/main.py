import tkinter as tk
from tkinter import ttk
from files_related import *
from funciones_generos import *
from funciones_peliculas import *
import os
import sys


def root_generator():
    """
    Crea una ventana y la retorna
    """
    root = tk.Toplevel()
    root.geometry("1080x720")  # Tamaño de la ventana
    root.config(bg="pink")
    root.config(cursor="heart")
    root.columnconfigure(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30, weight=10)
    root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=5, weight=10)
    return root


def close(event=None):
    """
    Cierra la aplicación
    """
    sys.exit()


def movies_menu(root_main):
    """
    Muestra las casillas para ingresar los datos de la películas
    """
    def temp_title(event):
        """
        Muestra un texto temporal en el entry 
        """
        if (event.type == tk.EventType.FocusIn
        and title_entry.get() == temp_title_text):
            title_entry.delete(0, "end")
            title_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if title_entry.get() == "":
                title_entry.config(fg="gray")
                title_entry.insert(0, temp_title_text)

    def temp_director(event):
        """
        Muestra un texto temporal en el entry 
        """
        if (event.type == tk.EventType.FocusIn
        and director_entry.get() == temp_director_text):
            director_entry.delete(0, "end")
            director_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if director_entry.get() == "":
                director_entry.config(fg="gray")
                director_entry.insert(0, temp_director_text)

    def temp_genre(event):
        """
        Muestra un texto temporal en el entry 
        """
        if (event.type == tk.EventType.FocusIn
        and genre_entry.get() == temp_genre_text):
            genre_entry.delete(0, "end")
            genre_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if genre_entry.get() == "":
                genre_entry.config(fg="gray")
                genre_entry.insert(0, temp_genre_text)

    def temp_year(event):
        """
        Muestra un texto temporal en el entry 
        """
        if (event.type == tk.EventType.FocusIn
        and year_entry.get() == temp_year_text):
            year_entry.delete(0, "end")
            year_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if year_entry.get() == "":
                year_entry.config(fg="gray")
                year_entry.insert(0, temp_year_text)

    def temp_score(event):
        """
        Muestra un texto temporal en el entry 
        """
        if (event.type == tk.EventType.FocusIn
        and score_entry.get() == temp_score_text):
            score_entry.delete(0, "end")
            score_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if score_entry.get() == "":
                score_entry.config(fg="gray")
                score_entry.insert(0, temp_score_text)

    def back_main(event):
        """
        Vuelve al menu principal
        """
        root_main.deiconify()
        root.destroy()

    def confirmar(event):
        """
        Valida si se ingreso texto en todas las casillas, si es así, 
        llama a la función main_peliculas() e ingresa la pelicula 
        si es que pasa todos los filtros de la función   
        """
        if (title_entry.get() != ""
            and not title_entry.get().isspace()
            and title_entry.get() != temp_title_text
            and director_entry.get() != "" 
            and director_entry.get() != temp_director_text
            and not director_entry.get().isspace() 
            and genre_entry.get() != ""
            and not genre_entry.get().isspace()
            and genre_entry.get() != temp_genre_text
            and year_entry.get() != ""
            and not year_entry.get().isspace()
            and year_entry.get() != temp_year_text 
            and score_entry.get() != ""
            and not score_entry.get().isspace()
            and score_entry.get() != temp_score_text):
            main_peliculas(title_entry.get(), director_entry.get(),
                           genre_entry.get(), year_entry.get(),
                           score_entry.get(), root)

        else:
            entry_error = tk.Toplevel(root)
            entry_error.geometry("500x100")
            entry_error.title("Error!")
            tk.Label(entry_error, text="Porfavor, ingrese todos los datos",
                     font=(None, 15)).pack(padx=10, pady=20)

    def in_button1(event):
        """
        Oscurecer el boton al pasar el mouse encima 
        """
        if event.type == tk.EventType.Enter:
            button1.config(bg="grey")
        else:
            button1.config(bg="grey90")

    def in_button2(event):
        """
        Oscurecer el boton al pasar el mouse encima 
        """
        if event.type == tk.EventType.Enter:
            button2.config(bg="grey")
        else:
            button2.config(bg="grey90")

    root = root_generator()
    root.title("Ingresar películas")
    root_main.withdraw()

    # Titulo de la ventana
    tk.Label(root, text="Ingresar Películas", font=(None, 30), bg="pink",
             ).grid(row=0, column=3, columnspan=5, sticky="new")

    # Imagen de la ventana
    file_path = os.path.dirname(os.path.abspath(__file__))
    img_movie_path = os.path.join(file_path, "imagenes", "oruga.png")
    img_movie = tk.PhotoImage(file=img_movie_path)
    tk.Label(root, image=img_movie, bg="pink").grid(
        row=0, column=8, rowspan=8, columnspan=3)

    # Título
    title_entry = tk.Entry(root, width=40, font=(None, 20), fg="gray")
    title_entry.grid(row=1, column=1, columnspan=7, sticky="w")
    temp_title_text = "Ingrese el Título de la película"
    title_entry.insert(0, temp_title_text)

    # Director
    director_entry = tk.Entry(root, width=40, font=(None, 20), fg="gray")
    director_entry.grid(row=3, column=1, columnspan=7, sticky="w")
    temp_director_text = "Ingrese el Director de la película"
    director_entry.insert(0, temp_director_text)

    # Genero
    tk.Label(
        root, text="*El género debe estar en la base de datos",
        font=(None, 11), fg="Black", bg="pink"
    ).grid(row=5, column=1, columnspan=4, sticky="sw",)
    genre_entry = tk.Entry(root, width=40, font=(None, 20), fg="gray")
    genre_entry.grid(row=5, column=1, columnspan=7, rowspan=1, sticky="w")
    temp_genre_text = "Ingrese el Género de la película"
    genre_entry.insert(0, temp_genre_text)

    # Año
    tk.Label(
        root, text="*El año debe ser mayor o igual a 1895 ", font=(None, 11),
        fg="Black", bg="pink"
    ).grid(row=7, column=1, columnspan=4, sticky="sw",)

    year_entry = tk.Entry(root, width=30, font=(None, 20), fg="gray", )
    year_entry.grid(row=7, column=1, columnspan=4, sticky="w")
    temp_year_text = "Ingrese el año de la película"
    year_entry.insert(0, temp_year_text)

    # Valoracion
    tk.Label(
        root, text="*La valoración debe ser entre 1 y 5", font=(None, 11),
        fg="Black", bg="pink"
    ).grid(row=7, column=6, columnspan=4, sticky="sw",)
    score_entry = tk.Entry(root, width=30, font=(None, 20), fg="gray")
    score_entry.grid(row=7, column=6, columnspan=4, rowspan=1, sticky="e")
    temp_score_text = "Ingrese la valoración de la película"
    score_entry.insert(0, temp_score_text)

    #  Botones
    button1 = tk.Button(root, text="Volver atrás", cursor="hand1", height=2)
    button1.grid(row=9, column=1, columnspan=2, sticky="sew")
    button2 = tk.Button(root, text="Confirmar", cursor="hand1", height=2)
    button2.grid(row=9, column=8, columnspan=2, sticky="sew")

    # Eventos
    title_entry.bind("<FocusIn>", temp_title)
    title_entry.bind("<FocusOut>", temp_title)

    director_entry.bind("<FocusIn>", temp_director)
    director_entry.bind("<FocusOut>", temp_director)

    genre_entry.bind("<FocusIn>", temp_genre)
    genre_entry.bind("<FocusOut>", temp_genre)

    year_entry.bind("<FocusIn>", temp_year)
    year_entry.bind("<FocusOut>", temp_year)

    score_entry.bind("<FocusIn>", temp_score)
    score_entry.bind("<FocusOut>", temp_score)

    button1.bind("<Button-1>", back_main)
    button2.bind("<Button-1>", confirmar)
    button1.bind("<Enter>", in_button1)
    button1.bind("<Leave>", in_button1)
    button2.bind("<Enter>", in_button2)
    button2.bind("<Leave>", in_button2)

    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)

    root.mainloop()


def genres_menu(root_main):
    """
    Muestra las casillas para ingresar los generos y ademas imprime la 
    lista de estos 
    """

    def temp_genre(event):
        """
        Muestra un texto temporal en la casilla
        """
        if (event.type == tk.EventType.FocusIn and
                genre_entry.get() == temp_genre_text):
            genre_entry.delete(0, "end")
            genre_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if genre_entry.get() == "":
                genre_entry.config(fg="gray")
                genre_entry.insert(0, temp_genre_text)

    def temp_genre_father(event):
        """
        Muestra un texto temporal en la casilla
        """
        if (event.type == tk.EventType.FocusIn and
                genre_father_entry.get() == temp_genre_father_text):
            genre_father_entry.delete(0, "end")
            genre_father_entry.config(fg="black")
        if event.type == tk.EventType.FocusOut:
            if genre_father_entry.get() == "":
                genre_father_entry.config(fg="gray")
                genre_father_entry.insert(0, temp_genre_father_text)

    def back_main(event):
        """
        Volver al menu principal
        """
        root_main.deiconify()
        root.destroy()

    def in_button1(event):
        """
        Oscurece el boton al pasar el mouse por encima
        """
        if event.type == tk.EventType.Enter:
            button1.config(bg="grey")
        else:
            button1.config(bg="grey90")

    def in_button2(event):
        """
        Oscurece el boton al pasar el mouse por encima
        """
        if event.type == tk.EventType.Enter:
            button2.config(bg="grey")
        else:
            button2.config(bg="grey90")

    def recursive_print(matrix: list, genre_to_print: str,
                        tab_depth=1) -> None:
        for genre in matrix:
            if (genre[1] == genre_to_print):
                text_area.config(state="normal")
                aux = genre[0].strip('\"')
                aux_tab = "\t" * tab_depth
                text_area.insert(tk.END, f"{aux_tab + aux}\n")
                recursive_print(matrix, genre[0], tab_depth + 1)
        text_area.config(state="disable")

    def reload_genre_list():
        text_area.config(state="normal")
        text_area.delete(1.0, tk.END)
        matrix = obtain_matrix(genres_path)
        text_area.insert(tk.END, "General\n")
        recursive_print(matrix, "\"General\"")

    def confirmar(event):
        """
        Valida si se ingreso texto en todas las casillas, si es así, 
        llama a la función main_generos() e ingresa el género  
        si es que pasa todos los filtros de la función
        """
        if (genre_entry.get() != "" and not genre_entry.get().isspace() and
                genre_entry.get() != temp_genre_text):
            if (genre_father_entry.get().isspace() or
                genre_father_entry.get() == "" or
                    genre_father_entry.get() == temp_genre_father_text):
                main_generos(genre_entry.get(), "", root)
            else:
                main_generos(genre_entry.get(), genre_father_entry.get(), root)
        else:
            entry_error = tk.Toplevel(root)
            entry_error.geometry("500x100")
            entry_error.title("Error!")
            tk.Label(entry_error, text="Ingrese un género válido",
                     font=(None, 15)).pack(padx=10, pady=20)
        reload_genre_list()

    # Archivos
    file_path = os.path.dirname(os.path.abspath(__file__))
    genres_path = os.path.join(file_path, "archivos", "generos.csv")

    # Título pestaña
    root = root_generator()
    root.title("Ingresar géneros")
    root_main.withdraw()

    # Titulo de la ventana
    tk.Label(root, text="Ingresar Géneros", font=(None, 30), bg="pink",
             ).grid(row=0, column=3, columnspan=5, sticky="new")

    # Lista de generos
    frame_genre = tk.Frame(root, bd="3", relief="groove")
    frame_genre.grid(row=2, column=2, columnspan=7, rowspan=1, sticky="nsew")
    scroll_v = tk.Scrollbar(frame_genre)
    scroll_v.pack(side="right", fill="y")
    text_area = tk.Text(
        frame_genre, wrape=None, yscrollcommand=scroll_v.set,
        font=(None, 18), height=15
    )
    text_area.pack(expand="true", fill="both")
    scroll_v.config(command=text_area.yview)
    matrix = obtain_matrix(genres_path)
    text_area.insert(tk.END, "General\n")
    recursive_print(matrix, "\"General\"")

    # Genero
    genre_entry = tk.Entry(root, width=50, font=(None, 25), fg="gray")
    genre_entry.grid(row=6, column=2, columnspan=7, rowspan=1, sticky="w")
    temp_genre_text = "Ingrese el Género aquí"
    genre_entry.insert(0, temp_genre_text)

    # Genero Padre
    tk.Label(root, text="*Si no especifica género padre, se asignará "
             "automaticamente en general", font=(None, 10), fg="Black",
             bg="pink").grid(row=8, column=2, columnspan=4, sticky="nw",)
    genre_father_entry = tk.Entry(root, width=50, font=(None, 25), fg="gray")
    genre_father_entry.grid(
        row=7, column=2, columnspan=7, rowspan=1, sticky="w")
    temp_genre_father_text = "(opcional) Ingrese el Género Padre"
    genre_father_entry.insert(0, temp_genre_father_text)

    #  Botones
    button1 = tk.Button(root, text="Volver atrás", cursor="hand1", height=2)
    button1.grid(row=9, column=1, columnspan=2, sticky="sew")
    button2 = tk.Button(root, text="Confirmar", cursor="hand1", height=2)
    button2.grid(row=9, column=8, columnspan=2, sticky="sew")

    # Eventos
    genre_entry.bind("<FocusIn>", temp_genre)
    genre_entry.bind("<FocusOut>", temp_genre)

    genre_father_entry.bind("<FocusIn>", temp_genre_father)
    genre_father_entry.bind("<FocusOut>", temp_genre_father)

    button1.bind("<Button-1>", back_main)
    button1.bind("<Enter>", in_button1)
    button1.bind("<Leave>", in_button1)
    button2.bind("<Enter>", in_button2)
    button2.bind("<Leave>", in_button2)
    button2.bind("<Button-1>", confirmar)

    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)

    root.mainloop()


def list_menu(root_main):
    """
    Muestra la lista de peliculas  
    """
    def back_main(event):
        """
        Vuelve al menu  principal 
        """
        root_main.deiconify()
        root.destroy()

    def buscador_peliculas(event):
        """
        Busca pelicula según el filtro seleccionado  
        """
        texto_buscado = buscador.get().lower()
        if (
            texto_buscado != "" and not texto_buscado.isspace()
            and buscador_combo.get() != combo_normal
        ):
            text_area.config(state="normal")
            text_area.delete(1.0, tk.END)
            if buscador_combo.get() == combo_title:
                for i in movies_list:
                    if (
                        i[0].lower().find(texto_buscado) != -1
                        or i[1].lower().find(texto_buscado) != -1
                    ):
                        text_area.insert(tk.END, f"{', '.join(i)}\n")
            elif buscador_combo.get() == combo_genre:
                for i in movies_list:
                    if (
                        i[2].lower().find(texto_buscado) != -1
                        and texto_buscado != ""
                        and not texto_buscado.isspace()
                    ):
                        text_area.insert(tk.END, f"{', '.join(i)}\n")
            elif buscador_combo.get() == combo_score:
                for i in movies_list:
                    if (
                        i[4].find(texto_buscado) != -1 
                        and texto_buscado != ""
                        and not texto_buscado.isspace()
                    ):
                        text_area.insert(tk.END, f"{', '.join(i)}\n")
            text_area.config(state="disable")
        else:
            text_area.config(state="normal")
            text_area.delete(1.0, tk.END)
            for i in movies_list:
                text_area.insert(tk.END, f"{', '.join(i)}\n")

    file_path = os.path.dirname(os.path.abspath(__file__))
    movies_path = os.path.join(file_path, "archivos", "peliculas.csv")
    movies_list = crea_lista_archivo(movies_path, ",")

    root = root_generator()
    root.title("Ingresar películas")
    root_main.withdraw()
    movies_list = crea_lista_archivo(movies_path, ",")

    #  Botones
    button1 = tk.Button(root, text="Volver atrás", cursor="hand1", height=2)
    button1.grid(row=9, column=1, columnspan=2, sticky="sew")

    #  Buscador
    frame_search = tk.Frame(
        root, bd=3, height="40", relief="groove")
    frame_search.grid(row=3, column=2, columnspan=7, sticky="we")

    buscador = tk.Entry(frame_search, font=("Courrier", 20), width=45)
    buscador.grid(row=0, column=1, sticky="ns")
    combo_title = "Título o director"
    combo_genre = "Género"
    combo_score = "Valoración"
    combo_normal = "Buscar película por:"
    buscador_combo = ttk.Combobox(frame_search, state="readonly",
                                  values=[combo_normal, combo_title,
                                          combo_genre, combo_score]
                                  )
    buscador_combo.current(0)
    buscador_combo.grid(row=0, column=0, sticky="w")
    button_search = tk.Button(frame_search, text="buscar", cursor="hand1")
    button_search.grid(row=0, column=2, sticky="e")

    #  Peliculas
    frame_movie = tk.Frame(root, bd="3", relief="groove")
    frame_movie.grid(row=6, column=2, columnspan=7, rowspan=1, sticky="nsew")
    scroll_v = tk.Scrollbar(frame_movie)
    scroll_v.pack(side="right", fill="y")
    text_area = tk.Text(
        frame_movie, wrape=None, yscrollcommand=scroll_v.set,
        font=(None, 18), height=15
    )
    for i in movies_list:
        text_area.insert(tk.END, f"{', '.join(i)}\n")

    text_area.pack(expand="true", fill="both")
    scroll_v.config(command=text_area.yview)
    text_area.config(state="disabled")

    # Eventos
    button1.bind("<Button-1>", back_main)
    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)
    button_search.bind("<Button-1>", buscador_peliculas)
    buscador.bind("<Return>", buscador_peliculas)

    root.mainloop()


def main():
    """
    Crea la ventana principal de la aplicación y muesta los botones 
    correspondientes junto a la imagen y el título
    """
    def genres_window(event):
        genres_menu(root)

    def movies_window(event):
        movies_menu(root)

    def list_window(event):
        list_menu(root)

    def in_button1(event):
        """
        Oscurece el boton al pasar el mouse por encima
        """
        if event.type == tk.EventType.Enter:
            button1.config(bg="grey")
        else:
            button1.config(bg="grey90")

    def in_button2(event):
        """
        Oscurece el boton al pasar el mouse por encima
        """
        if event.type == tk.EventType.Enter:
            button2.config(bg="grey")
        else:
            button2.config(bg="grey90")

    def in_button3(event):
        """
        Oscurece el boton al pasar el mouse por encima
        """
        if event.type == tk.EventType.Enter:
            button3.config(bg="grey")
        else:
            button3.config(bg="grey90")

    # Ventana Principal
    root = tk.Tk()
    root.geometry("1080x720")  # Tamaño de la ventana
    file_path = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(file_path, "imagenes", "icon.png")
    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon)
    root.title("Fvck this is cine")
    root.config(bg="pink")
    root.config(cursor="heart")
    root.columnconfigure(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30, weight=10)
    root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      minsize=10, weight=10)

    # Titulo
    tk.Label(
        root,
        text="Bienvenido a Fvck this is cine\nLa aplicacion para buscar, "
        "clasificar y puntuar\n tus películas favoritas\na continuacion haz "
        "click en tu opción deseada",
        bg="white",
        font=("Arial", 20, "bold", "roman"), relief="groove", bd=3
    ).grid(row=1, column=2, rowspan=1, columnspan=7, sticky="nsew")

    # Imagen de la ventana
    img_main_path = os.path.join(file_path, "imagenes", "esto_es_cine.png")
    img_main = tk.PhotoImage(file=img_main_path)
    tk.Label(root, image=img_main).grid(row=5, column=3, columnspan=5)

    # Botones
    button1 = tk.Button(root, text="Ingresar Género", cursor="hand1", height=1)
    button1.grid(row=8, column=1, rowspan=2,  columnspan=2, sticky="nsew")
    button2 = tk.Button(root, text="Ingresar Películas", cursor="hand1")
    button2.grid(row=8, column=8, rowspan=2, columnspan=2, sticky="nsew")
    button3 = tk.Button(root, text="Lista de películas", cursor="hand1")
    button3.grid(row=8, column=5, rowspan=2, columnspan=1, sticky="nsew")

    # Eventos
    button1.bind("<Button-1>", genres_window)
    button2.bind("<Button-1>", movies_window)
    button3.bind("<Button-1>", list_window)
    button1.bind("<Enter>", in_button1)
    button1.bind("<Leave>", in_button1)
    button2.bind("<Enter>", in_button2)
    button2.bind("<Leave>", in_button2)
    button3.bind("<Enter>", in_button3)
    button3.bind("<Leave>", in_button3)

    root.bind("<Escape>", close)
    root.protocol("WM_DELETE_WINDOW", close)

    root.mainloop()


if __name__ == "__main__":
    main()
