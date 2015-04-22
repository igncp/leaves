# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu12"
  config.vm.box_url = 'https://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box'
  config.vm.hostname = 'leaves-project'
  config.vm.network "forwarded_port", guest: 80, host: 9080
  config.vm.synced_folder "salt-provisioner/", "/srv/salt/"
  config.vm.synced_folder ".", "/leaves"
  config.vm.provision :salt do |salt|
    salt.log_level = 'warning'
    salt.colorize = true
    salt.run_highstate = true
    salt.minion_config = "salt-provisioner/minion.conf"
  end
end
