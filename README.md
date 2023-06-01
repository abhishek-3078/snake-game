INTRODUCTION
We made this snake game by using tkinter which is basically GUI ,here we see that the front page of the  our Snake game which is developed by me i.e Amit Kumar so,let’s see the what are the functionalities of different button , level , difficulty ,mode and last we see the rules for the user who has playing this game. the further next part of this game that is how is it actually work is explained by my teammates Aman kumar and Abhishek kumar in our next slides.

1.BUTTONS:-In this front page there are many buttons which is used i.e easy,medium and hard these buttons is for the users who choose the difficulty level as he wish and the button i.e high score by this button user can see its previous high score and also the option of reset high score by this button user can reset its previous high score.our next button is start game by this button user can start the game .

2.DIFFICULTY:-This difficulty option gives three option i.e easy,medium and hard.In these options we basically maintain the the speed of the snake as the difficulty options user can select.int the easy option the speed of the snake is lower and the increasing from easy to medium and the speed is fastest at the level hard.

3.MODE:-In our games there are options of mode of this game  i.e single player as well as multiplayers after completing the both user can see their score.

4.RULES:-There are following rules for playing this game
a→Snake do not touch the wall of the window if they touch then the           game ends.
b→Snake should not touch its own body.

In this snake game, we gave the features to play in three difficulty levels along with the modes as single and multiplayer mode.In which two players can play together and compare there score.
Difficulty is based on the speed of the snake motion.
		For implementing this we used classes concepts to create instances of the snake/snakes and food/foods and here is interesting food in between we called it bigfood ,by eating that player get the five points and by normal food player gets one(1)
Point. 
					SNAKE CLASS
In snake class using init we initialise a snake body coordinates two-dimensional list and a canvas list for its body structure using that coordinates.		
					 FOOD CLASS
In food class we use the module random to generate two values namely x and y for the food in between the window frame.and 
Its coordinates list to store that value of x and y for the future reference of snake eating the food condition.Also a list to store the canvas for the food.

					    BIG FOOD
Big food concept is similar to the food, just there is a difference in scoring part of the game to make it more interesting ,Bigfood is generated after every NINE eating of the normal food.

				  COLLISION CONDITION
Whenever the snake takes its next move we check the collision condition as; Does snake head (list first element of snake coordinates) collide with any body parts(list elements of snake coordinates other than first element)  or not ?  Does the snake head collide with the body of the window.In any of the two conditions is true the function returns true else false.

				    CHANGE DIRECTION

In this function the simple logic is that the snake can’t move exactly backwards. For example, a right moving snake can’t move left in its just next turn.Otherwise other key enter by the user is valid and for that valid key the snake new direction is set to the user entered key from the previous direction.


For installing clone this repo using 
git clone https://github.com/abhishek-3078/snake-game.git 
and enjoy.