# check_comments.py

import sys

def count_comments(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    # Contar los comentarios
    comment_count = 0
    for line in lines:
        if line.strip().startswith("#"):  # Verifica si la línea es un comentario
            comment_count += 1
    
    return comment_count

def main():
    file_path = "app.py"  # Archivo a revisar
    
    # Contar los comentarios
    comment_count = count_comments(file_path)
    
    # Si hay más de 5 comentarios, fallar el commit
    if comment_count > 5:
        print(f"¡Error! El archivo '{file_path}' tiene {comment_count} comentarios, lo cual excede el límite de 5.")
        sys.exit(1)  # Código de error para evitar el commit
    else:
        print(f"El archivo '{file_path}' tiene {comment_count} comentarios. Todo en orden.")
        sys.exit(0)  # Código de éxito

if __name__ == "__main__":
    main()
