# Leaves

[![Leaves Logo](/misc/logo.png)](https://github.com/igncp/leaves)

This project is for educational purposes. It uses some useful and powerful tools to get, manage, visualize and analyze data.

## Usage

You need to have Vagrant installed on your computer. Then, from a terminal, run (this may take several minutes):

`vagrant up`

This command will setup a virtual machine with the configuration set in the Vagrant file, and then install some software and do some configuration in the machine, configured in the `salt-provisioner` dir. Both operations may take a long time. Once they finish, you can enter the virtual machine by:

`vagrant ssh`

As you would see, the directory of the project will be shared with the guest machine in the `/leaves` directory. Once there, you can run the scripts located in the `bin` directory. Note that mostly of them, they will only work if they called from that directory, e.g.:

`./bin/linux-shell/csv-output-table`

To be able to run the scripts, you must set them as executables. Just call `make set-executables` in the `/leaves` directory and it will automatically set them for you.


## Sources
You can check the Sources.md file to see where the data is taken from.


## Sections
The main sections of the project are: APIs (e.g. LinkedIn), big-data (e.g. Hadoop), databases (e.g. MySQL), languages (e.g. python) and linux-shell (e.g. curl, jq).


## Structure
The main directories used in the project:
- `./bin` : Holds the scripts. Note that some of them (e.g. in the APIs subdirectory) may need to set up credentials in the `config` dir.
- `./config` : Holds the necessary credentials files for some services (e.g. the LinkedIn API).
- `./src` : Contains the code that many of the scripts run.
- `./reports` : Contains output from some programs, e.g. plots.
- `/data` : Generated in the guest virtual machine, contains the data files used by some software, and the HDFS used by Hadoop.

## License and Author
This project is purely educational and it is licensed under the MIT License.
2015 - Ignacio Carbajo