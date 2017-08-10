# de.speedmann
Pelican source files for speedmann.de
## Usage
First run `ansible-playbook base.yml -u root -k`
This will configure users to be able to access the system and adds their public keys
Afterwards run `ànsible-playbook harden.yml` to configure ssh ~~and harden some basic OS Parameters~~
