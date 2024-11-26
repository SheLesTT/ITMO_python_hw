

def create_latex_table(table: list[list[str]], column_names: list[str]) -> str:
    for row in table:
        if len(row) != len(table[0]):
            raise ValueError("All rows must have the same number of columns")
    if len(column_names) != len(table[0]):
        raise ValueError("Column names must have the same number of columns as the table")

    table_str = "\\begin{tabular}{|" + "c|" * len(table[0]) + "}\n" \
    + "\t\hline\n"
    if column_names:
        table_str += "\t" + " & ".join(["\\textbf{" + col + "}" for col in column_names])
        table_str += " \\\\ \\hline\n"
    for row in table:
        table_str += "\t"+" & ".join(row) + " \\\\ \hline\n"
    table_str += "\\end{tabular}\n"
    return table_str

def create_latex_image(image_path: str) -> str:
    return f"\includegraphics[width=0.5\\textwidth]" +'{' f'{image_path}'+ '}\n'

