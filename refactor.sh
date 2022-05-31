#!/bin/bash

# pushd ../
# popd
# echo # --------Install NodeJS SDKs--------
# rm -rf ~/.config/yarn/link/@willguibr
# make tfgen && make build_sdks
# make install_nodejs_sdk
# cp bin/pulumi-resource-zpa $GOPATH/bin/
# mkdir -p examples/zpa_segment_group
# cd examples/zpa_segment_group

# echo # --------Install Python SDKs--------
# rm -rf ~/.config/yarn/link/@willguibr
# make tfgen && make build_sdks
# make install_python_sdk
# cp bin/pulumi-resource-zpa $GOPATH/bin/
# mkdir -p examples/test-demo
# cd examples/test-demo/

echo # --------Install GO SDKs--------
rm -rf ~/.config/yarn/link/@willguibr
make tfgen && make build_go
make install_go_sdk
cp bin/pulumi-resource-zpa $GOPATH/bin/
# mkdir -p examples/test-demo
# cd examples/test-demo/

# echo # --------Install GO SDKs--------
# rm -rf ~/.config/yarn/link/@willguibr
# make tfgen && make build_sdks
# make install_dotnet_sdk
# cp bin/pulumi-resource-zpa $GOPATH/bin/
# mkdir -p examples/test-demo
# cd examples/test-demo/

# echo # --------Install Plugins--------
# rm -rf ~/.config/yarn/link/@willguibr
# make tfgen && make build_sdks
# make install_plugins
# cp bin/pulumi-resource-zpa $GOPATH/bin/
# mkdir -p examples/test-demo
# cd examples/test-demo/

# echo # --------Install All SDKs--------
# rm -rf ~/.config/yarn/link/@willguibr
# make tfgen && make build_sdks
# make install_sdks
# cp bin/pulumi-resource-zpa $GOPATH/bin/
# mkdir -p examples/test-demo
# cd examples/test-demo/

# --------Install SDKs--------
# make install_dotnet_sdk
# make install_go_sdk
# make install_nodejs_sdk
# make install_plugins
# make install_python_sdk
# make install_sdks


# yarn link @willguibr/zpa