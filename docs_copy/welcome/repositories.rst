##############
Repositories
##############

.. tip:: 
    It is recommended you clone it into the directory ``~/catkin_ws/src/``. Many of the scripts provided in this document assume you have it in this directory and it will help with building the ros packages. 

`sootballs_sites <https://github.com/rapyuta-robotics/sootballs_sites>`_ - main branch

    - Repository that stores all the customer specific information required for deployments, configurations, and map/site updates. 
    - New sites get created in this repo.

`rr_io_amr <https://github.com/rapyuta-robotics/rr_io_amr>`_ - devel branch
    
    - Repository where io_amr is developed
    - Required in order to bootstrap site data with `sitectl <https://github.com/rapyuta-robotics/rr_io_amr/blob/devel/bringup/sites/sitectl.py>`_ to the customers gwm

`rr_sootballs <https://github.com/rapyuta-robotics/rr_sootballs>`_ - devel branch

    - Repository where sootballs is developed
    - Required in order to check release `versions/docker images <https://github.com/rapyuta-robotics/rr_sootballs/blob/devel/docker/.env>`_

`rr_manifests <https://github.com/rapyuta-robotics/rr_manifests>`_ - devel branch

    - Repository where all deployment manifests are stored
    - A manifest is what holds all of the required version information for the various tools that the ROPS team uses. 
    - Each release has a different manifest, because different releases may use different versions of certain extensions. 

`rr_rops_runbooks <https://github.com/rapyuta-robotics/rr_rops_runbooks>`_ - devel branch

    - Repository where this documentation is hosted/stored
