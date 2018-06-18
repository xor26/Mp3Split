import os
import math
class Spliter():

    @staticmethod
    def splitFile(filePath,  outputDir, chunkCount):
        # filePath = "test.mp3"
        # outputDir = "output/"
        fileName = filePath.rsplit('.', 1)[0]
        fileName = fileName.rsplit('/', 1)[1]
        fileExtension = filePath.rsplit('.', 1)[1]

        fileSize = os.stat(filePath).st_size  # in bytes
        chunkSize = math.ceil(fileSize / chunkCount)
        chunkBeggining = 0
        chunkNum = 0
        with open(filePath, "rb") as file:
            chunk = file.read(chunkSize)
            while chunk != b'':
                chunkNum += 1
                with open(outputDir+"/"+fileName+"_"+str(chunkNum)+"."+fileExtension, "wb") as outputChunk:
                    outputChunk.write(chunk)
                chunk = file.read(chunkSize)
