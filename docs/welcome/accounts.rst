########################
Accounts
########################

This page will describe all the accounts/logins you will require to be able to function as a robot operations engineer. Ensure that you have access to all of them before you start. Use your rapyuta-robotics.com email address for all of them.

================
Github
================

* Create an account for `github <https://github.com>`_.

* Once the account is created make sure you get access to the `rapyuta-robotics <https://github.com/rapyuta-robotics>`_ github organization. You can ask in it_admin slack channel to get access.
If you already have one, make sure to add your rapyuta-robotics.com email address to your account and enable it as the primary email address so that you can be notified about updates on your contributions or review requests among other functionalities.

* The following :ref:`repositories <Repositories>` are frequently used and so it is recommended to clone them into your PC.

.. note:: 
    Create the directory ``~/catkin_ws/src/``. Many of the scripts we use in ROPS assume that the repositories exist inside of this directory. It will help with building the ros packages. 

==========================
Rapyuta.io
==========================

* Create an account for `rapyuta.io <https://console.rapyuta.io/>`_.

* Once the account is created, make sure you have access to the correct organization as well as projects.

* If you do not, you can ask any of the Robot Operations members to give you access.

* On your PC install `Rapyuta.io CLI <https://cli.rapyuta.io/>`_.

* Once that is installed, login to the Rapyuta.io CLI with the following command

``rio auth login``

==========================
Docker
==========================

* Create an account for `quay.io <https://quay.io/>`_.

* Once the account is created make sure you have access to the `rapyuta organization <https://quay.io/organization/rapyuta>`_.

* Login to docker via quay on your PC with the command ``docker login quay.io``.

========================
Azure
========================

* Create an account for `Azure <https://azure.microsoft.com/>`_.

* This will give you access to the key vault for SOPS decrypting.

* On your PC install `Azure CLI <https://learn.microsoft.com/en-us/cli/azure/install-azure-cli>`_.

* Once that is installed, login to the Azure CLI with the command ``az login``.

=========================
Bitwarden
=========================

* Create an account for `Bitwarden <https://bitwarden.com/>`_.

* This gives access to the Rapyuta Robotics vault.