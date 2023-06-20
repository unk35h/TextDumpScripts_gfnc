@ echo off
setlocal EnableDelayedExpansion

cd E:\11GameTool\UnityTool\CNStudioNet6

echo "[Progress] Fetching Lua raw files"
.\AssetStudioCLI.exe E:\11GfncDump\GameDataDump\Lua00Asset E:\11GfncDump\GameDataDump\Lua01Raw --types TextAsset --key_index 4 --group_assets_type ByContainer

echo "[Progress] Fetching Config Table raw files"
.\AssetStudioCLI.exe E:\11GfncDump\GameDataDump\Table00Asset E:\11GfncDump\GameDataDump\Table01Raw --types TextAsset --key_index 4 --group_assets_type ByContainer

cd E:\11GfncDump\GameDataDump

echo "[Progress] Decoding Lua files"
python LuaEdit.py

FOR /r E:\11GfncDump\GameDataDump\Lua02Edit %%f IN (*.lua) DO (
	set "FILE_NAME=%%~nf"
	set "OUTPUT_PATH=E:\11GfncDump\GameDataDump\Lua03Decode"
	E:\11GfncDump\GameDataDump\luadec.exe -se UTF8 %%f > "!OUTPUT_PATH!\!FILE_NAME!.lua"
)

python LuaSort.py

echo "[Progress] Decoding Table files"
python TableDecode.py

PAUSE