# DuoFlashBack

![Duo](https://vignette.wikia.nocookie.net/duolingo/images/b/be/Duo_2019.png/revision/latest?cb=20190307143704)

This is the back end of the improved [DuoTerminal App](https://github.com/normandy14/duoTerminal).

## Motivation

The previous [duoTerminal app](https://github.com/normandy14/duoTerminal) lacked a proper modern gui for use and navigation. Instead, it relies on the terminal for input and output. The interaction is like the following:

![App](https://github.com/normandy14/duoTerminal/blob/master/doc/screenshot.png?raw=true)

DuoFlash is created for the user that wants to supplement their language learning on the Duolingo platform with additional learning tools. Duolingo is a great learning tool, but its web/android/ios iterface is bulky. The user learns already encountered words on the Duolingo platform with flash cards

In addition, the duoTerminal project is archived because it was difficult to maintain because it was poorly written in some aspects. I document this in the previous project, [duoTerminal app](https://github.com/normandy14/duoTerminal)

### Installing

[Pip3](https://pip.pypa.io/en/stable/) should be installed before [Pipenv](https://pipenv.pypa.io/en/latest/) because Pip3 is needed to install Pipenv.

### Getting Started

A step by step series of examples that tell you how to get a development env running.

1. :card_index: Clone project

```
git clone [(HTTPS/SSH) URL]
```

2. :snake: Enter the Pipenv enviroment

```
pipenv shell
```

3. :snake: Install the program dependencies

```
pipenv install
```

4. :snake: Run the program

```
pipenv run python3 app.py
```

### After Run

The backend API is now running. Go to http://localhost:6500/auth/<lang> to see output in web browser.
  
Substitue lang for the language you use such as es - for Spanish, ar -f or  Arabic or fr - for French.
See Bash config for intructions to get your personal Duolingo user account or dummy user account set.

For example, to get the Spanish words associated with the Duolingo account:

  http://localhost:6500/auth/es
  
### Bash Setup

To reduce the time it takes to repeately type in the username and password correctly, for each seperate API requests.
Its recommended to create your own .env to store your duolingo account/ dummy account.

The username and password will be visible in plain text, so also configure .gitignore to ignore this file. For this project, the file is ignored by default.

### Add the Pytest File
1. Create pytest.ini file with `touch pytest.ini`
Create the following for the Pytest file:
```
[pytest]
env =
  USERNAME=
  PASSWORD=
```
2. USERNAME=[Your Username] where Username of the username of the Duolingo account
3. PASSWORD=[Your Password] where Password is the password of the Duolingo account
(Insert account credentials in [Your Username] and [Your Password])

## Running App
Duplicate paragraph, if now ready to go to endpoint:
  
The backend API is now running. Go to http://localhost:6500/auth/<lang> to see output in web browser.
Substitue lang for the language you use such as es - for Spanish, ar -f or  Arabic or fr - for French.
See Bash config for intructions to get your personal Duolingo user account or dummy user account set up.
  
## Running the tests

Explain how to run the automated tests for this system:
  
### Setting Up Test

1. :snake: Enter the shell enviroment

```
pipenv shell
```

2. :snake: Install the dependencies

```
pipenv install pytest
```
3. Follow instructions for Install .Env, but name file pytest.ini, with same security precautions
  
  ### Add pytest.ini File
  
  (credential management for pytest)

1. `cd` to directory
2. `touch pytest.ini`
3. open the pytest.ini file
4. Type: `EXPORT USERNAME[Your Username]` where 'Your Username' is the username of the account
5. Type `EXPORT PASSWORD[Your Password]` where 'Your Password' is the password of the account
6. Save the file
  
4. :snake: Run the tests

```
pipenv run pytest
```

### Output of Tests

```
pipenv run pytest
----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
```
<!--

## Python Libraries

1. :bird: [Duolingo](https://github.com/KartikTalwar/Duolingo/) -- Unofficial Duolingo API Wrapper

## Contributing

:newspaper: Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

:card_index: We use [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) for versioning.

## Authors

* :ocean: **Normandy14** - *Initial work* - [Github Account](https://github.com/Normandy14)

## License

:newspaper: This project is licensed under the GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details.

<!--

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

-->
