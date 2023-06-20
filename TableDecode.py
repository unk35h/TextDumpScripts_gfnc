import os
import json
import sys
import importlib

from pathlib import Path
from google.protobuf import json_format


def BytesFileDecode(inputDir, outputDir):
    PB2_MODULE_DIR = 'TablePb2.'
    KEY_BYTES = b"\x1a\x04\x08\x00\x12\x00"

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

            inputFile = open(inputPath, "rb")

            pb2Dir = ''.join([PB2_MODULE_DIR, Path(inputFileFullName).stem, '_pb2'])
            table_pb2 = importlib.import_module(pb2Dir)
            protobufMessage = table_pb2.CfgTable()

            rawFileBytes = inputFile.read()
            position = rawFileBytes.find(KEY_BYTES)
            targetFileBytes = rawFileBytes[position+6:]
            protobufMessage.ParseFromString(targetFileBytes)

            inputFile.close()

            outputFileFullName = ''.join([Path(inputFileFullName).stem,".json"])
            outputPath = outputDir / outputFileFullName
            outputDir.mkdir(parents=True, exist_ok=True)

            outputFile = open(outputPath, "w+", encoding="utf-8") 
            jsonRawDict = json_format.MessageToDict(message=protobufMessage)  

            jsonString = json.dumps(jsonRawDict, indent=2, ensure_ascii=False)
            outputFile.write(jsonString)

            outputFile.close()


if __name__=="__main__":
    BytesFileDecode('./Table01Raw/', './Table02Decode/')