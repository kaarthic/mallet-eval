@echo off

rem This batch file serves as a wrapper for several
rem  MALLET command line tools.

echo Usage: tag.sh [MODEL FILE] [TEST FILE]

if not "%MALLET_HOME%" == "" goto gotMalletHome

echo MALLET requires an environment variable MALLET_HOME.
goto :eof

:gotMalletHome

set MALLET_CLASSPATH=%MALLET_HOME%\class;%MALLET_HOME%\lib\mallet-deps.jar
set MALLET_MEMORY=1G
set MALLET_ENCODING=UTF-8

set CLASS=cc.mallet.fst.SimpleTagger

set MALLET_ARGS=--model-file "%1" "%2"

java -Xmx%MALLET_MEMORY% -ea -Dfile.encoding=%MALLET_ENCODING% -classpath %MALLET_CLASSPATH% %CLASS% %MALLET_ARGS%

:eof
