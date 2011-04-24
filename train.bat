@echo off

rem This batch file serves as a wrapper for several
rem  MALLET command line tools.

echo Usage: train.bat [Training File] [Thread Number] [Output Model File]

if "%3" == "" goto eof

if not "%MALLET_HOME%" == "" goto gotMalletHome

echo MALLET requires an environment variable MALLET_HOME.
goto :eof

:gotMalletHome

set MALLET_CLASSPATH=%MALLET_HOME%\class;%MALLET_HOME%\lib\mallet-deps.jar
set MALLET_MEMORY=1G
set MALLET_ENCODING=UTF-8

set CLASS=cc.mallet.fst.SimpleTagger

set MALLET_ARGS=--train true --model-file "%3" --threads %2 "%1"

java -Xmx%MALLET_MEMORY% -ea -Dfile.encoding=%MALLET_ENCODING% -classpath %MALLET_CLASSPATH% %CLASS% %MALLET_ARGS%

:eof
