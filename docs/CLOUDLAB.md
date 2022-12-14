# Setting Up a CloudLab Account
This is a tutorial for Georgia Tech students enrolled in *Introduction to
Enterprise Computing* (CS4365/6365) or *Real-Time/Embedded Systems*
(CS4220/CS6235). It shows how to setup a CloudLab account for running system
performance experiments on the cloud using the BuzzBlog Benchmark.

## Generating a New SSH Key Pair
First, generate an SSH key pair to be used exclusively in CloudLab.
```
ssh-keygen -t rsa -b 4096
```

Then, upload the newly generated SSH public key to GitHub:
1. Access the [GitHub SSH keys page](https://github.com/settings/keys).
2. Click on *New SSH key*.
3. Copy and paste the newly generated SSH public key.

## Creating a CloudLab Account
Your experiments will run on private clouds instantiated in
[CloudLab](https://www.cloudlab.us), a public infrastructure for provisioning
scientific clouds with total control over computing resources.

To create your CloudLab account:
1. Access the [CloudLab sign-up page](https://cloudlab.us/signup.php).
2. Fill out your personal information.
3. In *Project Information*, select *Join Existing Project*. The project to be
joined is named *Infosphere*.
4. In *SSH Public Key file*, upload the newly generated SSH public key.

Your request to join project *Infosphere* is now waiting for approval.

Finally, send your username to the TA in charge of the project.

## Setting Bash as Your Default Linux Shell in CloudLab
Once you have access to CloudLab, set *Bash* as your default Linux shell:
1. Access the [Emulab settings page](https://www.emulab.net/moduserinfo.php3).
2. In *Shell*, select *Bash*.
