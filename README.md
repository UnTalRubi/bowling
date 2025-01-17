# Bowling Score
Bowling Game Kata

### Naming Convention

"Pins": Valores de cada una de las tiradas.

"Roll": Lanzamiento de bola.

"Strike": Tirar todos los bolos en un solo roll (X). Puntúa sumando los Pins que has tirado en ese Frame mas los dos Rolls del frame siguiente.

"Spare": Tirar todos los bolos en dos rolls (/). Puntúa sumando los Pins que has tirado en ese Frame mas el primer Roll del frame siguiente.

"Miss": No tirar ningún bolo en un roll (-)

"Frame": Cada ronda de una partida de bolos, 10 frames por partida.

"First Roll": Primera tirada de un frame.

"Second Roll": Segunda tirada de un frame.

"Third Roll": Tercera tirada exclusiva del frame 10.

A standard game of ten-pin bowling consists of 10 frames, with a maximum of two rolls in each of the first nine frames and three in the tenth. 

A strike occurs when the bowler knocks down all 10 pins on the first roll; if this occurs in any of the first nine frames, the frame ends immediately without a second roll being taken. 

A spare occurs if the bowler leaves any pins standing after the first roll, then knocks them all down on the second. 

In any given frame, the bowler scores one point for every pin knocked down; a spare or strike awards one extra point for each pin knocked down on the next one or two rolls, respectively.

In the tenth frame, the bowler gets one extra roll for making a spare, or two for a strike. 

The highest possible score for a single game is 300, achieved by rolling 12 consecutive strikes (a "perfect game").