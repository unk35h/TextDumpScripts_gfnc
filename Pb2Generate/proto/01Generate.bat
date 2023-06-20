@echo off
setlocal EnableDelayedExpansion

FOR /r E:\11GfncDump\GameDataDump\Pb2Generate\proto %%f IN (*.proto) DO (
	set "FILE_NAME=%%~nf"
	set "OUTPUT_PATH=E:\11GfncDump\GameDataDump\Pb2Generate\pb2"
	protoc.exe --proto_path=./ !FILE_NAME!.proto --python_out=!OUTPUT_PATH!
)
pause