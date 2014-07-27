sudo sh clean.sh
python build_mobile.py
sudo phonegap build ios
platforms/perm.sh
sh finishiOSBuild.sh
open platforms/ios/Hextris.xcodeproj/