# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
 
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "~> 20200304.0.0"
 
 # Thêm mới từ link https://stackoverflow.com/questions/22922891/vagrant-ssh-authentication-failure
 
  config.ssh.username = "vagrant"
  config.ssh.password = "vagrant"
  config.ssh.private_key_path = "~/.ssh/id_rsa"
  config.ssh.forward_agent = true
 
  config.vm.network "forwarded_port", guest: 8000, host: 8000
 
  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
 
    sudo apt-get update
    sudo apt-get install -y python3-venv zip
 
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
 end
 
 # Sau khi config xong thì làm theo video này: https://www.youtube.com/watch?v=QT8eRGGxn68&t=100s
 # => mở virtual box và đăng nhập với username và password là vagrant hết, sau đó nhập sudo nano /etc/ssh/sshd_config
 # Sửa: PasswordAuthentication từ no thàng yes
 
 # Sau đó mới type: vagrant up -> sau đó mới type: vagrant ssh (mở git bash mới được)
 
 # => Running and connecting to our dev server successfully