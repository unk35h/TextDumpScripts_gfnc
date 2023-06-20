Some simple scripts to extract some text resources from Girls' Frontline: Neural Cloud, which is used for the repository gamedata_gfnc.

This project uses https://github.com/Razmoth/CNStudio to get raw files from the game.

Notes:
1.Put luascripts.ab to Lua00Asset. Put tables.ab to Table00Asset.
2.The running codes of whole progress is in WholeWork.txt. You have to edit it before using.
3.The structs of Protobuf Message for Table data are in Pb2Generate\proto. All struct are manually writen throught reading dump.cs from il2cppDumper.
4.This project use a custom luadec.exe. The luadec.exe uses the code from https://github.com/viruscamp/luadec/tree/master/vcproj-5.3. The int main(int argc, char* argv[]) in luadec/luadec/luadec.c is modified for preventing to add unneccessary header information to each lua file. The luadec.c has been put in this repository as a example.

