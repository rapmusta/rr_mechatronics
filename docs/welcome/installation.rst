########################
Installations
########################

This page will describe all the installations you will require to be able to function as a robot operations engineer. 

======
PyEnv
======

.. note::
    Downloading PyEnv is not necessary and you can feel free to use your own python virtual environment. It is highly recommended you update your python to 3.10. If you dont feel comfortable with Virtual Environments you can follow the following steps

1. Download PyEnv

    .. code-block:: bash

        sudo apt update -y
        sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
        curl https://pyenv.run | bash
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
        echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
        exec "$SHELL"


2. Install Python 3.10.8

    ``pyenv install 3.10.8``

3. Check if It was installed correctly

    ``pyenv versions``

4. Select Python 3.10.8 to be your Default

    ``pyenv global 3.10.8``

5. Confirm that python is now 3.10.8

    ``pyenv versions`` or  ``python3 --version``

======================
SOPS
======================

Install SOPS to be able to decrypt secrets/keys for customers.The SOPS repository can be found `here <https://github.com/getsops/sops>`_.

To confirm if you can decrypt with sops by decrypting any of the secrets.yaml in sootballs_sites repository with the following command;

``sops ~/catkin_ws/src/sootballs_sites/sites/${site}/rio/secrets.yaml``

.. note:: 
    You will not be able to decrypt the secrets.yaml with sops if you do not have access to azure.

======================
RDT
======================

Install RDT to be able to setup devices as well as deploy sootballs and udpate configurations. 

You can find the installation guide :ref:`here<Rapyuta Deployment Tool (RDT)>`

======================
Visualizer
======================

Clone the `rr_sootballs <https://github.com/rapyuta-robotics/rr_sootballs>`_ repository in ``~/catkin_ws/src/``

Install the requirements.txt

``pip3 install -r ~/catkin_ws/src/rr_sootballs/tools/requirements.txt``

.. tip:: 
    It is recommended you create a bash alias for easy access.

    ``echo "alias visual='python3 ~/catkin_ws/src/rr_sootballs/tools/scripts/visualizer.py -d'" >> ~/.bashrc``

    This will allow you to run the following command to easily generate sootball files

    ``visual --work_dir WORK_DIR [options]``

========================
Sootballs Site Tools
========================

Clone the `sootballs_sites <https://github.com/rapyuta-robotics/sootballs_sites>`_ repository into ``~/catkin_ws/src/``.

Install the requirements.txt.

``pip3 install -r ~/catkin_ws/src/sootballs_sites/tools/requirements.txt``


========================
Poetry
========================

Run the following code to install poetry.

.. code:: 

    curl -sSL https://install.python-poetry.org | python -
    # Maybe need install python 3.10 here
    poetry init
    poetry env use python3.10
    cd ${SOOTBALLS_SITES_REPO}
    poetry update package



This will allow you to bootstrap WMS

========================
Terraform
========================

Install Terraform following the instructions from this `Website <https://computingforgeeks.com/how-to-install-terraform-on-ubuntu/>`_

=========
Hydra
=========

Install Hydra following the instructions from this `Website <https://www.ory.sh/docs/hydra/self-hosted/install>`_
