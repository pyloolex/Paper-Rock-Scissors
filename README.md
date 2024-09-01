# This is the "paper-rock-scissors" game.

It's implemented in Python without third-party libraries.
Only standard Python libraries were used:
* random: To get a random value for a computer's choice in the game.
* unittest: To test the application.


## To run in Docker

The application is dockerised. To build a docker image run:
```
    docker build -t game .
```

To play a game run:
```
    docker run -ti game main.py
```
after building the docker image.

To run the tests, build a docker image and then execute:
```
    docker run game test/game_test.py
```

## To run locally

The application can work without docker too, if it's more convenient for you.
Just add the game directory to the PYTHONPATH env variable and run:
```
    python ./main.py
```

Then you can also run the tests in the same way:
```
    python test/game_test.py
```

## Interaction example:
```
Welcome to a game "paper-rock-scissors"!

It's a game for two players. Now you are playing versus computer.
You pick one game symbol and a computer picks one game symbol.

Available options:
* paper
* rock
* scissors

The winner is determined by the following schema:
* paper beats rock
* rock beats scissors
* scissors beats paper

Please, specify how many rounds you would like to play and press "Enter".
(Available options: 1-5)
Number of rounds: 3
-----
Round 1/3:
Please, pick one of the game symbols, type your choice and press "Enter":
- paper
- rock
- scissors
Your choice: scissors
Computer's choice: scissors
Draw! Current score: You 1:1 Computer
Press "Enter" to continue.
-----
Round 2/3:
Please, pick one of the game symbols, type your choice and press "Enter":
- paper
- rock
- scissors
Your choice: paper
Computer's choice: scissors
You lost! Current score: You 1:2 Computer
Press "Enter" to continue.
-----
Round 3/3:
Please, pick one of the game symbols, type your choice and press "Enter":
- paper
- rock
- scissors
Your choice: rock
Computer's choice: paper
You lost! Current score: You 1:3 Computer
Press "Enter" to continue.
*****
Game over. The final score: You 1:3 Computer.
Press "Enter" to exit.
```
