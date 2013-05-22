exec {'apt-get update': 
  command => "/usr/bin/apt-get update"
}

apt-package {["octave3.2","git"]: }
apt-package {["python-dev", "python-setuptools", "ipython-notebook"]: }
apt-package {"python-pip": require => Package["python-dev"]}
apt-package {["python-numpy", "python-scipy", "python-matplotlib"]: }
apt-package {"libjpeg62": }
apt-package {["r-base", "wget"]: }
class { "rstudio": }

python-package {["nose", "nltk", "pycluster", "hcluster", "virtualenv", "python-hashes", "beautifulsoup4","pymorph", "mahotas"]: }

define apt-package($package = $title) {
  package {$package:
    ensure   => present,
    provider => apt,
    require  => Exec['apt-get update']
  }
}
define python-package($package = $title) {
  package {$package:
    ensure   => present,
    provider => pip,
    require  => Package["python-pip"]
  }
}

class rstudio {
  $version = "0.97.551"
  $home_dir = "/home/vagrant"
  $package_loc = "${home_dir}/rstudio"
  $package_name = "rstudio-${version}-amd64.deb"

  file {$package_loc: 
    ensure => directory,
    owner  => vagrant,
    group  => vagrant,
    mode   => 0644
  }

  class {"rstudio-package": 
    package_name => $package_name,
    package_loc  => $package_loc
  }

  package {"rstudio":
    provider => dpkg,
    ensure   => installed,
    source   => "${package_loc}/${package_name}",
    require  => Class["rstudio-package"]
  } 
}

class rstudio-package($package_name, $package_loc) {
  exec {"wget http://download1.rstudio.org/${package_name}  -P ${package_loc} -o ${package_loc}/wget.log": 
    user    => vagrant,
    path    => ["/usr/local/sbin", "/bin", "/sbin", "/usr/bin", "/usr/sbin"],
    creates => "${package_loc}/${package_name}",
    require => [Package["wget"], File[$package_loc]]
  }
}
