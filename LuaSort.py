import os
import shutil

from pathlib import Path


def StringFileSort(inputDir, outputDir):
    inputDir = Path(inputDir)
    outputDir = Path(outputDir)

    for inputRoot, _, files in os.walk(inputDir):
        inputRoot = Path(inputRoot)
        outputRoot = outputDir
        outputRoot.mkdir(parents=True, exist_ok=True)

        for inputFileFullName in files:
            inputPath = inputRoot / inputFileFullName

            #with open(inputPath, 'r', encoding="utf-8") as f:
                #rawfileString = f.read()

            stringList = inputFileFullName.split('.')
            stringListCount = len(stringList)
            fileExtension = stringList[stringListCount-1]
            fileName = stringList[stringListCount-2]
            outputFileFullName = '.'.join([fileName, fileExtension])
            outputFileFullName = Path(outputFileFullName)

            stringList.remove(fileExtension)
            stringList.remove(fileName)
            subOutputDir = '/'.join(stringList)
            subOutputDir = Path(subOutputDir)
            targetOutputDir = outputRoot / subOutputDir
            targetOutputDir.mkdir(parents=True, exist_ok=True)
            outputPath = targetOutputDir / outputFileFullName

            shutil.copy2(inputPath, outputPath)
            #with open(outputPath, 'w+', encoding="utf-8") as f:
                #f.write(rawfileString)


if __name__=="__main__":
    StringFileSort('./Lua03Decode/', './Lua04Sort/')