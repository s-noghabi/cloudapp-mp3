pip install --upgrade pip
pip install --upgrade virtualenv

mkdir -p $HOME/bin

if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    PATH=$PATH:$HOME/bin
    export PATH
    echo "Added $HOME/bin to PATH"
fi

wget -O $HOME/bin/lein https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
chmod a+x $HOME/bin/lein
echo "#!/bin/bash
export LEIN_ROOT=true" > /etc/profile.d/leinroot.sh
export LEIN_ROOT=true
lein

mkdir -p /data/virtualenvs
touch /root/.ssh/config

echo "/opt/rh/python27/root/usr/lib64/" >> /etc/ld.so.conf.d/x86_64-linux-gnu.conf
ldconfig

mkdir -p /var/log/storm/streamparse
chown -R storm:hadoop /var/log/storm/streamparse

pip install git+https://github.com/srujun/streamparse.git
