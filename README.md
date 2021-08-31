# DuoFlash

![Duo](https://vignette.wikia.nocookie.net/duolingo/images/b/be/Duo_2019.png/revision/latest?cb=20190307143704)

DuoFlash, a backend to obtain words that you've learned on the Duolingo web/android/ios platform, all from the convenience of your personal terminal.

1. :brain: Effortlessly Enjoy the learning vocabulary reinforcement process, without even opening a web browser.

2. :pencil2: Translate each word from your target language to English, or try your hand at translating from English to your target language. The choice is yours!

3. :recycle: Continue to translate missed words until you complete the translation cycle.

## Motivation

![App](https://github.com/normandy14/duoTerminal/blob/master/doc/screenshot.png?raw=true)

Duoterminal is a project created for the user that wants to supplement their language learning on the Duolingo platform with additional learning tools. Duolingo is a great learning tool, but its web/android/ios iterface is bulky. The main app also forces user to learn and reinforce learned words in sentences.

DuoTerminal allows for reinforcement of learned words in isolation. It also requires the user to type in by hand the translation of the individual words, unlike the Duolingo app which encourages the user to click the correct translation of a sentence.

Pip3 should be installed before Pipenv because Pip3 is needed to install Pipenv.

### Installing

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

You will be presented with a menu such as the following, when you run the program successfully:

```
welcome to duo terminal: review duolingo words on your terminal
select: (l)ogin or (q)uit
```

## Running the tests

Explain how to run the automated tests for this system:

1. :snake: Enter the shell enviroment

```
pipenv shell
```

2. :snake: Install the dependencies

```
pipenv install --dev
```

3. :snake: Run the tests

```
pipenv run nosetests testApp.py
```

### Break down into end to end tests

Explain what these tests test and why.

The methods tests the data processing and manipulation of the data stored in hashes:

```
pipenv run nosetests testApp.py
----------------------------------------------------------------------
Ran 14 tests in 0.005s

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
