echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update

sudo apt-get install libedgetpu1-std


#sudo apt-get install libedgetpu1-max

sudo apt-get install python3-pycoral

python3 -m pip install --extra-index-url https://google-coral.github.io/py-repo/ pycoral~=2.0


# ALSO: See https://github.com/google-coral/examples-camera