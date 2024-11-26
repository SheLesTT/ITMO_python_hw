from my_latex2.gen_latex import create_latex_table, create_latex_image





def create_latex_with_table() -> None:
    tex_string = "\documentclass{article}\n"

    tex_string += "\\usepackage{graphicx}\n"
    tex_string += "\\begin{document}\n"
    tex_string +=create_latex_table([["a", "b","e"], ["c", "d", 'f']], ["col1", "col2", "col3"])
    tex_string += "\\begin{figure}[h!]\n"
    tex_string += create_latex_image("volley.drawio.png")
    tex_string += "\\end{figure}\n"
    tex_string += "\\end{document}"

    with open("hw2_aritfacts/my_latex.tex", "w") as f:
        f.write(tex_string)


if __name__ == "__main__":
    create_latex_with_table()