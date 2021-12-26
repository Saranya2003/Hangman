% List of guessing vocab and letter

vocab(['hurt','pear','rain','crab','rose','wave','kite','bear','care','fast']).
letter(['a','b','c','e','h','i','k','n','o','p','r','s','t','u','w']).
%run a game
hangman:-
    getVocab(Ans),
    !,
    write('Welcome to hangman.'),
    nl,
    print(Ans),
    name(Ans,AnsList),
    makeBlanks(AnsList, BlankList),
    askGuess(AnsList,BlankList).

% Randomly return a vocab from the list
getVocab(Ans):-
    vocab(L),
    length(L, X),
    R is random(X),
    N is R+1,
    getNth(L, N, Ans).

% This part is let AI guess the letter

askGuess(AnsList, BlankList):-
    name(BlankName, BlankList),
    write(BlankName),
    nl,
    write('Enter your guess, followed by a period and return.'),
    nl,
    read(Guess),
    !,
    name(Guess, [GuessName]),
    processGuess(AnsList,BlankList,GuessName).

processGuess(AnsList,BlankList,GuessName):-
    member(GuessName,AnsList),
    !,
    write('Correct!'),
    nl,
    substitute(AnsList, BlankList, GuessName, NewBlanks),
    checkWin(AnsList,NewBlanks).

processGuess(AnsList, BlankList, _, CountFailed) :-
  (   CountFailed == 7
  ->  format('Sorry, game over. You didn\'t guess (~s)~n', [AnsList])
  ;   write('Nope!'),
      CountFailed1 is CountFailed + 1,
      askGuess(AnsList, BlankList, CountFailed1)
  ).

% Check to see the vocab is guessed. If so, write 'You win'

checkWin(AnsList, BlankList):-
    name(Ans, AnsList),
    name(BlankName, BlankList),
    BlankName = Ans,
    !,
    write('You win!').

checkWin(AnsList, BlankList):-
    !,
    askGuess(AnsList, BlankList).

% getNth([H|T],N,E) should be true when Ans is the Nth element of the list L. N will always be at least 1.
getNth([H|T],1,H).

getNth([H|T],N,E):-
    N1 is N-1,
    getNth(T,N1,E1),
    E=E1.

% makeBlanks(AnsCodes, BlankCodes) should take an answer phrase, which is a list
% of character codes that represent the answer phrase, and return a list
% where all codes but the '_' turn into the code for '*'.  The underscores
% need to remain to show where the words start and end.
makeBlanks(AnsCodes, BlankCodes) :-
  maplist(answer_blank, AnsCodes, BlankCodes).

answer_blank(Ans, Blank) :-
  Ans == 0'_ -> Blank = Ans ; Blank = 0'* .

% substitute(AnsList, BlankList, GuessName, NewBlanks) Takes character code lists AnsList and BlankList,
% and GuessName, which is the character code for the guessed letter.  The NewBlanks should again be a
% character code list, which puts all the guesses into the display word and keeps the *'s and _'s otherwise.
substitute(AnsCodes, BlankCodes, GuessName, NewBlanks) :-
     maplist(place_guess(GuessName), AnsCodes, BlankCodes, NewBlanks).

place_guess(Guess, Ans, Blank, Display) :-
    Guess == Ans -> Display = Ans ; Display = Blank.