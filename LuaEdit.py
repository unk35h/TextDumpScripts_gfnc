import os
from pathlib import Path


def BytesFileEdit(inputDir, outputDir):
    KEYWORD = b'\x19\x93\x0D\x0A\x1A\x0A'
    INSERT_INT_SIZE_BYTE = b'\x04'
    REPLACE_FORMAT_BYTE = b'\x00'

    inputDir = Path(inputDir)
    outputDir = Path(outputDir)


    for inputRoot, _, files in os.walk(inputDir):
        inputRoot = Path(inputRoot)
        '''
        relativeDir = inputRoot.relative_to(inputDir)
        outputRoot = outputDir / relativeDir 
        outputRoot.mkdir(parents=True, exist_ok=True)
        '''

        for inputFileFullName in files:
            inputPath = inputRoot / inputFileFullName

            with open(inputPath, 'rb') as f:
                rawfileByte = f.read()
                position = rawfileByte.find(KEYWORD)
                leftPart = rawfileByte[:position+6]
                rightPart = rawfileByte[position+6:]
                tempList = [leftPart, rightPart]
                fileByte = INSERT_INT_SIZE_BYTE.join(tempList)
                fileByte = fileByte.replace(b'\x01', REPLACE_FORMAT_BYTE, 1)

            outputFileFullName = Path(inputFileFullName).stem
            outputPath = outputDir / outputFileFullName
            outputDir.mkdir(parents=True, exist_ok=True)

            with open(outputPath, 'wb') as f:
                f.write(fileByte)


if __name__=="__main__":
    BytesFileEdit('./Lua01Raw', './Lua02Edit')