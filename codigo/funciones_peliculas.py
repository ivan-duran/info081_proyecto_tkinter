from files_related import *
import tkinter as tk


def equal_movie_and_director_exists(list_to_validate: list) -> bool:
    """
    Recibe lista dispuesta de esta forma ["Pelicula", "Director"], retorna 
    valor booleano que corresponderá a sí ya existe o no este par en 
    "peliculas.csv".
    """
    movies_matrix = obtain_matrix(movies_path)
    lowered_list_to_validate = [x.lower() for x in list_to_validate]
    for i in range(len(movies_matrix)):
        values_of_interest = movies_matrix[i][:2]
        values_of_interest = [x.lower() for x in values_of_interest]
        if (values_of_interest
            == lowered_list_to_validate):
            return True
    return False


def input_movie(title: str, director: str, genre: str, year: str, score: str,
    root: str) -> str:
    """
    Esta función recibe el título, género, año, valoración y la ventana  
    del tkinter. Luego hace las validaciones de cada uno, si estas son 
    correctas retorna un string de estas separados por una coma.
    """
    entry_error = tk.Toplevel(root)
    entry_error.geometry("500x100")
    entry_error.title("Error!")
    title = title.capitalize()
    director = director.title()
    list_to_validate = []
    genres_list = obtain_list(genres_path, True)
    for i in range(len(genres_list)):
        genres_list[i] = genres_list[i].lower()  
    list_to_validate = [f'"{title}"', f'"{director}"']
    genre_aux = f'"{genre.lower()}"'
    if genre_aux not in genres_list:
        tk.Label(entry_error, text=("El género no se encuentra en nuestra"
            " base de datos,\ndebe agregarlos previamente"),
        font=(None, 15)).pack(padx=10, pady=20)
        return ""

    genre = genre.capitalize()
    try:
        if int(year) < 1895:
            tk.Label(entry_error,
            text=("El año debe ser mayor o igual a 1895"), font=(None, 15)
            ).pack(padx=10, pady=20)
            return ""
    except:
        tk.Label(entry_error, text=("El año debe ser un valor entero"),
            font=(None, 15)).pack(padx=10, pady=20)
        return "" 
    try:

        if int(score) < 1 or int(score) > 5:
            tk.Label(entry_error, text=("La valoración debe ser entre 1 y 5"),
            font=(None, 15)).pack(padx=10, pady=20)
            return ""
    except:
        tk.Label(entry_error, text=("La valoración debe ser un número entero"),
            font=(None, 15)).pack(padx=10, pady=20)
        return "" 
    if (equal_movie_and_director_exists(list_to_validate)):
        tk.Label(entry_error, text="La película con el director ingresado\n ya"
             " están en la base de datos",
        font=(None, 15)).pack(padx=10, pady=20)
        return ""
    entry_error.title("Omedeto")
    tk.Label(entry_error, text=("Su película se a ingresado\n correctamente"),
        font=(None, 15)).pack(padx=10, pady=20)

    all_user_input = f'"{title}", "{director}", "{genre}", {year}, {score}'

    return all_user_input


def main_peliculas(title: str, director: str, genre: str, year: str,
    score: str, root):
    """
    Recibe el título, director, género, año, valoración y la ventana del 
    tkinter. Abre el archivo peliculas.csv si existe, si no, lo crea, 
    luego ingresa la película que recibe de input_movie() en 
    peliculas.csv
    """
    already_exists = False
    files_in_directory = directories()
    for file in files_in_directory:
        if (file == "peliculas.csv"):
            already_exists = True
            break
    if (already_exists):
        with open(movies_path, 'r', encoding="utf-8") as csv_file:
            original_csv_file = csv_file.read()
            csv_file.seek(0) 
        with open(movies_path, 'a', encoding="utf-8") as csv_file:
            if (original_csv_file[-1:] == "\n"):
                input_as_string = input_movie(
                    title, director, genre, year, score, root)
                csv_file.write(input_as_string)
            else:
                input_as_string = input_movie(
                    title, director, genre, year, score, root)
                csv_file.write(f"\n{input_as_string}")
    else:
        with open(movies_path, 'w', encoding="utf-8") as csv_file:    
            input_as_string = input_movie(
                title, director, genre, year, score, root)
            csv_file.write(input_as_string)


file_path = os.path.dirname(os.path.abspath(__file__))
movies_path = os.path.join(file_path, "archivos", "peliculas.csv")
genres_path = os.path.join(file_path, "archivos", "generos.csv")