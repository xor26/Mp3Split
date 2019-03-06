import os
import math


class Spliter():

    @staticmethod
    def split_file(file_path, output_dir, chunk_count):
        file_name = file_path.rsplit('.', 1)[0]
        file_name = file_name.rsplit('/', 1)[1]
        file_extension = file_path.rsplit('.', 1)[1]

        file_size = os.stat(file_path).st_size  # in bytes
        chunk_size = math.ceil(file_size / chunk_count)
        chunk_num = 0
        with open(file_path, "rb") as file:
            chunk = file.read(chunk_size)
            while chunk != b'':
                chunk_num += 1
                with open(output_dir + "/" + file_name + "_" + str(chunk_num) + "." + file_extension,
                          "wb") as outputChunk:
                    outputChunk.write(chunk)
                chunk = file.read(chunk_size)
