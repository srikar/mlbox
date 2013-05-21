exec {'apt-get update': 
  command => "/usr/bin/apt-get update"
}

apt-package {["octave3.2","git"]: }
apt-package {["python-dev", "python-setuptools", "ipython-notebook"]: }
apt-package {"python-pip": require => Package["python-dev"]}
apt-package {["python-numpy", "python-scipy", "python-matplotlib"]: }
apt-package {"libjpeg62": }
apt-package {["r-base", "rstudio"]: }

python-package {["nose", "nltk", "pycluster", "hcluster", "virtualenv", "python-hashes", "beautifulsoup4"]: }

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
