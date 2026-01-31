

```bash

$ curl https://repo.anaconda.com/pkgs/misc/gpgkeys/anaconda.asc | gpg --dearmor > conda.gpg

$ install -o root -g root -m 644 conda.gpg /usr/share/keyrings/conda-archive-keyring.gpg

$ gpg --keyring /usr/share/keyrings/conda-archive-keyring.gpg --no-default-keyring --fingerprint 34161F5BF5EB1D4BFBBB8F0A8AEB4F8B29D82806

$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/conda-archive-keyring.gpg] https://repo.anaconda.com/pkgs/misc/debrepo/conda stable main" > /etc/apt/sources.list.d/conda.list

$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/conda-archive-keyring.gpg] https://repo.anaconda.com/pkgs/misc/debrepo/conda stable main" | sudo tee -a /etc/apt/sources.list.d/conda.list

$ apt update

$ apt-get install conda

$ source /opt/conda/etc/profile.d/conda.sh
$ conda -V
conda 24.5.0
$



$ bash Anaconda3-2025.12-1-Linux-x86_64.sh

Welcome to Anaconda3 2025.12-1

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>>
By continuing installation, you hereby consent to the Anaconda Terms of Service available at https://anaconda.com/legal.


Do you accept the license terms? [yes|no]
>>> yes

Anaconda3 will now be installed into this location:
/root/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/root/anaconda3] >>>
Downloading and Extracting Packages:

Preparing transaction: done
Executing transaction: done
installation finished.
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

Note: You can undo this later by running `conda init --reverse $SHELL`

Proceed with initialization? [yes|no]
[no] >>> yes
no change     /root/anaconda3/condabin/conda
no change     /root/anaconda3/bin/conda
no change     /root/anaconda3/bin/conda-env
no change     /root/anaconda3/bin/activate
no change     /root/anaconda3/bin/deactivate
no change     /root/anaconda3/etc/profile.d/conda.sh
no change     /root/anaconda3/etc/fish/conf.d/conda.fish
no change     /root/anaconda3/shell/condabin/Conda.psm1
no change     /root/anaconda3/shell/condabin/conda-hook.ps1
no change     /root/anaconda3/lib/python3.13/site-packages/xontrib/conda.xsh
no change     /root/anaconda3/etc/profile.d/conda.csh
modified      /root/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

Thank you for installing Anaconda3!


```
