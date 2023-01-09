import os


class FilesGenerator():
    """
    test
    """
    def __init__(self):
        if 'files' not in os.listdir():
            os.mkdir('./files')

    def create_file(self, number_of_files=10000):
        """
        Criar files
        """
        for number in range(number_of_files):
            file_content = f"""
        file_{number}
        """
            with open(f"files//file_{number}.txt", "w") as file:

                for conteudo in file_content:
                    file.write(str(conteudo))


if __name__ == "__main__":
    FilesGenerator().create_file()
