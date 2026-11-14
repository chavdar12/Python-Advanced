"""Behaviour tests for the lesson scripts, using the examples from the course PDFs.

Every lesson script is either covered here or listed in COMPILE_ONLY with the reason
(test_by_folder.py still compile-checks those).
"""
import contextlib
import io
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# (script, stdin lines, expected stdout, compare lines unordered?)
STDIN_CASES = [('001-Lists-As-Stacks-And-Queues/001_reverse_strings.py', ['I Love Python'], 'nohtyP evoL I', False),
 ('001-Lists-As-Stacks-And-Queues/001_reverse_strings.py', ['Stacks and Queues'], 'seueuQ dna skcatS', False),
 ('001-Lists-As-Stacks-And-Queues/002_matching_brackets.py', ['1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'],
  '(2 + 3)\n(3 + 1)\n(2 - (2 + 3) * 4 / (3 + 1))', False),
 ('001-Lists-As-Stacks-And-Queues/002_matching_brackets.py', ['(2 + 3) - (2 + 3)'], '(2 + 3)\n(2 + 3)',
  False),
 ('001-Lists-As-Stacks-And-Queues/003_supermarket.py',
  ['George', 'Peter', 'William', 'Paid', 'Michael', 'Oscar', 'Olivia', 'Linda', 'End'],
  'George\nPeter\nWilliam\n4 people remaining.', False),
 ('001-Lists-As-Stacks-And-Queues/003_supermarket.py', ['Anna', 'Emma', 'Alexander', 'End'],
  '3 people remaining.', False),
 ('001-Lists-As-Stacks-And-Queues/004_water_dispenser.py',
  [2, 'Peter', 'Amy', 'Start', 2, 'refill 1', 1, 'End'], 'Peter got water\nAmy got water\n0 liters left',
  False),
 ('001-Lists-As-Stacks-And-Queues/004_water_dispenser.py',
  [10, 'Peter', 'George', 'Amy', 'Alice', 'Start', 2, 3, 3, 3, 'End'],
  'Peter got water\nGeorge got water\nAmy got water\nAlice must wait\n2 liters left', False),
 ('001-Lists-As-Stacks-And-Queues/005_hot_potato.py', ['Tracy Emily Daniel', 2],
  'Removed Emily\nRemoved Tracy\nLast is Daniel', False),
 ('001-Lists-As-Stacks-And-Queues/005_hot_potato.py', ['George Peter Michael William Thomas', 10],
  'Removed Thomas\nRemoved Peter\nRemoved Michael\nRemoved George\nLast is William', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/001_reverse_numbers.py', ['1 2 3 4 5'], '5 4 3 2 1', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/002_maximum_and_minimum_element.py',
  [9, '1 97', 2, '1 20', 2, '1 26', '1 20', 3, '1 91', 4], '26\n20\n91, 20, 26', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/002_maximum_and_minimum_element.py',
  [10, 2, '1 47', '1 66', '1 32', 4, 3, '1 25', '1 16', '1 8', 4], '32\n66\n8\n8, 16, 25, 32, 66, 47',
  False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/003_fast_food.py', [348, '20 54 30 16 7 9'], '54\nOrders complete',
  False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/003_fast_food.py', [499, '57 45 62 70 33 90 88 76'],
  '90\nOrders left: 76', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/004_fashion_boutique.py', ['5 4 8 6 3 8 7 7 9', 16], '5', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/004_fashion_boutique.py', ['1 7 8 2 5 4 7 8 9 6 3 2 5 4 6', 20],
  '5', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/005_truck_tour.py', [3, '1 5', '10 3', '3 4'], '1', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/006_balanced_parentheses.py', ['{[()]}'], 'YES', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/006_balanced_parentheses.py', ['{[(])}'], 'NO', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/006_balanced_parentheses.py', ['{{[[(())]]}}'], 'YES', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/007_robotics.py',
  ['ROB-15;SS2-10;NX8000-3', '8:00:00', 'detail', 'glass', 'wood', 'apple', 'End'],
  'ROB - detail [08:00:01]\nSS2 - glass [08:00:02]\nNX8000 - wood [08:00:03]\nNX8000 - apple [08:00:06]',
  False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/008_robotics_with_functions.py',
  ['ROB-15;SS2-10;NX8000-3', '8:00:00', 'detail', 'glass', 'wood', 'apple', 'End'],
  'ROB - detail [08:00:01]\nSS2 - glass [08:00:02]\nNX8000 - wood [08:00:03]\nNX8000 - apple [08:00:06]',
  False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/007_robotics.py',
  ['ROB-60', '7:59:59', 'detail', 'glass', 'wood', 'sock', 'End'],
  'ROB - detail [08:00:00]\nROB - sock [08:01:00]\nROB - wood [08:02:00]\nROB - glass [08:03:00]', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/008_robotics_with_functions.py',
  ['ROB-60', '7:59:59', 'detail', 'glass', 'wood', 'sock', 'End'],
  'ROB - detail [08:00:00]\nROB - sock [08:01:00]\nROB - wood [08:02:00]\nROB - glass [08:03:00]', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/009_crossroads.py',
  [10, 5, 'Mercedes', 'green', 'Mercedes', 'BMW', 'Skoda', 'green', 'END'],
  'Everyone is safe.\n3 total cars passed the crossroads.', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/009_crossroads.py',
  [9, 3, 'Mercedes', 'Hummer', 'green', 'Hummer', 'Mercedes', 'green', 'END'],
  'A crash happened!\nHummer was hit at e.', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/010_key_revolver.py',
  [50, 2, '11 10 5 11 10 20', '15 13 16', 1500],
  'Ping!\nBang!\nReloading!\nBang!\nBang!\nReloading!\n2 bullets left. Earned $1300', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/010_key_revolver.py',
  [20, 6, '14 13 12 11 10 5', '13 3 11 10', 800],
  "Bang!\nPing!\nPing!\nPing!\nPing!\nPing!\nCouldn't get through. Locks left: 3", False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/011_cups_and_bottles.py', ['4 2 10 5', '3 15 15 11 6'],
  'Bottles: 3\nWasted litters of water: 26', False),
 ('002-Exercise-Lists-As-Stacks-And-Queues/011_cups_and_bottles.py', ['1 5 28 1 4', '3 18 1 9 30 4 5'],
  'Cups: 4\nWasted litters of water: 35', False),
 ('003-Tuples-And-Sets/001_count_same_values.py', ['-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'],
  '-2.5 - 3 times\n4.0 - 2 times\n3.0 - 4 times\n-5.5 - 1 times', False),
 ('003-Tuples-And-Sets/002_average_student_grades.py',
  [7, 'Peter 5.20', 'Mark 5.50', 'Peter 3.20', 'Mark 2.50', 'Alex 2.00', 'Mark 3.46', 'Alex 3.00'],
  'Peter -> 5.20 3.20 (avg: 4.20)\nMark -> 5.50 2.50 3.46 (avg: 3.82)\nAlex -> 2.00 3.00 (avg: 2.50)', True),
 ('003-Tuples-And-Sets/003_record_unique_names.py',
  [8, 'Lee', 'Joey', 'Lee', 'Joe', 'Alan', 'Alan', 'Peter', 'Joey'], 'Lee\nJoey\nJoe\nAlan\nPeter', True),
 ('003-Tuples-And-Sets/004_parking_lot.py',
  [10, 'IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'IN, CA9999TT', 'IN, CA2866HI', 'OUT, CA1234TA',
   'IN, CA2844AA', 'OUT, CA2866HI', 'IN, CA9876HH', 'IN, CA2822UU'],
  'CA2844AA\nCA9999TT\nCA2822UU\nCA9876HH', True),
 ('003-Tuples-And-Sets/004_parking_lot.py',
  [4, 'IN, CA2844AA', 'IN, CA1234TA', 'OUT, CA2844AA', 'OUT, CA1234TA'], 'Parking Lot is Empty', False),
 ('003-Tuples-And-Sets/005_softuni_party.py',
  [5, '7IK9Yo0h', '9NoBUajQ', 'Ce8vwPmE', 'SVQXQCbc', 'tSzE5t0p', '9NoBUajQ', 'Ce8vwPmE', 'SVQXQCbc', 'END'],
  '2\n7IK9Yo0h\ntSzE5t0p', False),
 ('004-Exercise-Tuples-And-Sets/001_unique_usernames.py',
  [6, 'George', 'George', 'George', 'Peter', 'George', 'NiceGuy1234'], 'George\nPeter\nNiceGuy1234', True),
 ('004-Exercise-Tuples-And-Sets/002_sets_of_elements.py', ['4 3', 1, 3, 5, 7, 3, 4, 5], '3\n5', True),
 ('004-Exercise-Tuples-And-Sets/002_sets_of_elements.py', ['2 2', 1, 3, 1, 5], '1', False),
 ('004-Exercise-Tuples-And-Sets/003_periodic_table.py', [4, 'Ce O', 'Mo O Ce', 'Ee', 'Mo'], 'Ce\nEe\nMo\nO',
  True),
 ('004-Exercise-Tuples-And-Sets/004_count_symbols.py', ['SoftUni rocks'],
  ' : 1 time/s\n'
  'S: 1 time/s\n'
  'U: 1 time/s\n'
  'c: 1 time/s\n'
  'f: 1 time/s\n'
  'i: 1 time/s\n'
  'k: 1 time/s\n'
  'n: 1 time/s\n'
  'o: 2 time/s\n'
  'r: 1 time/s\n'
  's: 1 time/s\n'
  't: 1 time/s',
  False),
 ('004-Exercise-Tuples-And-Sets/005_phonebook.py', ['Adam-0888080808', 2, 'Mery', 'Adam'],
  'Contact Mery does not exist.\nAdam -> 0888080808', False),
 ('004-Exercise-Tuples-And-Sets/006_longest_intersection.py', [3, '0,3-1,2', '2,10-3,5', '6,15-3,10'],
  'Longest intersection is [6, 7, 8, 9, 10] with length 5', False),
 ('004-Exercise-Tuples-And-Sets/007_longest_intersection_with_ranges.py',
  [3, '0,3-1,2', '2,10-3,5', '6,15-3,10'], 'Longest intersection is [6, 7, 8, 9, 10] with length 5', False),
 ('004-Exercise-Tuples-And-Sets/008_battle_of_names.py', [4, 'Pesho', 'Stefan', 'Stamat', 'Gosho'],
  '304, 128, 206, 511', False),
 ('005-Multidimensional-Lists/001_sum_matrix_elements.py',
  ['3, 6', '7, 1, 3, 3, 2, 1', '1, 3, 9, 8, 5, 6', '4, 6, 7, 9, 1, 0'],
  '76\n[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]', False),
 ('005-Multidimensional-Lists/002_sum_matrix_columns.py',
  ['3, 6', '7 1 3 3 2 1', '1 3 9 8 5 6', '4 6 7 9 1 0'], '12\n10\n19\n20\n8\n7', False),
 ('005-Multidimensional-Lists/002_sum_matrix_columns.py', ['3, 3', '1 2 3', '4 5 6', '7 8 9'], '12\n15\n18',
  False),
 ('005-Multidimensional-Lists/003_primary_diagonal.py', [3, '11 2 4', '4 5 6', '10 8 -12'], '4', False),
 ('005-Multidimensional-Lists/003_primary_diagonal.py', [3, '1 2 3', '4 5 6', '7 8 9'], '15', False),
 ('005-Multidimensional-Lists/004_symbol_in_matrix.py', [3, 'ABC', 'DEF', 'X!@', '!'], '(2, 1)', False),
 ('005-Multidimensional-Lists/004_symbol_in_matrix.py', [4, 'asdd', 'xczc', 'qwee', 'qefw', 4],
  '4 does not occur in the matrix', False),
 ('005-Multidimensional-Lists/005_square_with_maximum_sum.py',
  ['3, 6', '7, 1, 3, 3, 2, 1', '1, 3, 9, 8, 5, 6', '4, 6, 7, 9, 1, 0'], '9 8\n7 9\n33', False),
 ('005-Multidimensional-Lists/005_square_with_maximum_sum.py', ['2, 4', '10, 11, 12, 13', '14, 15, 16, 17'],
  '12 13\n16 17\n58', False),
 ('006-Exercise-Multidimensional-Lists/001_diagonal_difference.py', [3, '11 2 4', '4 5 6', '10 8 -12'], '15',
  False),
 ('006-Exercise-Multidimensional-Lists/002_squares_in_matrix.py', ['3 4', 'A B B D', 'E B B B', 'I J B B'],
  '2', False),
 ('006-Exercise-Multidimensional-Lists/002_squares_in_matrix.py', ['2 2', 'a b', 'c d'], '0', False),
 ('006-Exercise-Multidimensional-Lists/003_maximal_sum.py',
  ['4 5', '1 5 5 2 4', '2 1 4 14 3', '3 7 11 2 8', '4 8 12 16 4'], 'Sum = 75\n1 4 14\n7 11 2\n8 12 16',
  False),
 ('006-Exercise-Multidimensional-Lists/004_matrix_shuffling.py',
  ['2 3', '1 2 3', '4 5 6', 'swap 0 0 1 1', 'swap 10 9 8 7', 'swap 0 1 1 0', 'END'],
  '5 2 3\n4 1 6\nInvalid input!\n5 4 3\n2 1 6', False),
 ('006-Exercise-Multidimensional-Lists/004_matrix_shuffling.py',
  ['1 2', 'Hello World', '0 0 0 1', 'swap 0 0 0 1', 'swap 0 1 0 0', 'END'],
  'Invalid input!\nWorld Hello\nHello World', False),
 ('006-Exercise-Multidimensional-Lists/005_snake_moves.py', ['5 6', 'SoftUni'],
  'SoftUn\nUtfoSi\nniSoft\nfoSinU\ntUniSo', False),
 ('006-Exercise-Multidimensional-Lists/006_knight_game.py', [5, '0K0K0', 'K000K', '00K00', 'K000K', '0K0K0'],
  '1', False),
 ('006-Exercise-Multidimensional-Lists/006_knight_game.py', [2, 'KK', 'KK'], '0', False),
 ('006-Exercise-Multidimensional-Lists/006_knight_game.py',
  [8, '0K0KKK00', '0K00KKKK', '00K0000K', 'KKKKKK0K', 'K0K0000K', 'KK00000K', '00K0K000', '000K00KK'], '12',
  False),
 ('006-Exercise-Multidimensional-Lists/008_miner.py',
  [5, 'up right right up right', '* * * c *', '* * * e *', '* * c * *', 's * * c *', '* * c * *'],
  'Game over! (1, 3)', False),
 ('006-Exercise-Multidimensional-Lists/009_miner_with_game_over_flag.py',
  [5, 'up right right up right', '* * * c *', '* * * e *', '* * c * *', 's * * c *', '* * c * *'],
  'Game over! (1, 3)', False),
 ('006-Exercise-Multidimensional-Lists/008_miner.py',
  [4, 'up right right right down', '* * * e', '* * c *', '* s * c', '* * * *'],
  'You collected all coals! (2, 3)', False),
 ('006-Exercise-Multidimensional-Lists/009_miner_with_game_over_flag.py',
  [4, 'up right right right down', '* * * e', '* * c *', '* s * c', '* * * *'],
  'You collected all coals! (2, 3)', False),
 ('006-Exercise-Multidimensional-Lists/008_miner.py',
  [6, 'left left down right up left left down down down', '* * * * * *', 'e * * * c *', '* * c s * *',
   '* * * * * *', 'c * * * c *', '* * c * * *'],
  '3 coals left. (5, 0)', False),
 ('006-Exercise-Multidimensional-Lists/009_miner_with_game_over_flag.py',
  [6, 'left left down right up left left down down down', '* * * * * *', 'e * * * c *', '* * c s * *',
   '* * * * * *', 'c * * * c *', '* * c * * *'],
  '3 coals left. (5, 0)', False),
 ('006-Exercise-Multidimensional-Lists/010_radioactive_mutant_vampire_bunnies.py',
  ['5 8', '.......B', '...B....', '....B..B', '........', '..P.....', 'ULLL'],
  'BBBBBBBB\nBBBBBBBB\nBBBBBBBB\n.BBBBBBB\n..BBBBBB\nwon: 3 0', False),
 ('006-Exercise-Multidimensional-Lists/010_radioactive_mutant_vampire_bunnies.py',
  ['4 5', '.....', '.....', '.B...', '...P.', 'LLLLLLLL'], '.B...\nBBB..\nBBBB.\nBBB..\ndead: 3 1', False),
 ('009-Functions-Advanced/001_absolute_values.py', ['1 2.5 -3 -4.5'], '[1.0, 2.5, 3.0, 4.5]', False),
 ('009-Functions-Advanced/002_rounding.py', ['1.0 2.5 3.0 4.5'], '[1, 2, 3, 4]', False),
 ('009-Functions-Advanced/006_character_combinations.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab', True),
 ('009-Functions-Advanced/007_character_combinations_with_perm.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab',
  True),
 ('009-Functions-Advanced/008_character_combinations_with_permutations.py', ['abc'],
  'abc\nacb\nbac\nbca\ncba\ncab', True),
 ('009-Functions-Advanced/009_character_combinations_printing.py', ['abc'], 'abc\nacb\nbac\nbca\ncba\ncab',
  True),
 ('009-Functions-Advanced/010_chairs.py', ['Peter, George, Amy', 2], 'Peter, George\nPeter, Amy\nGeorge, Amy',
  False),
 ('009-Functions-Advanced/011_expressions.py', ['1, 1, 1, 1'],
  '+1+1+1+1=4\n'
  '+1+1+1-1=2\n'
  '+1+1-1+1=2\n'
  '+1+1-1-1=0\n'
  '+1-1+1+1=2\n'
  '+1-1+1-1=0\n'
  '+1-1-1+1=0\n'
  '+1-1-1-1=-2\n'
  '-1+1+1+1=2\n'
  '-1+1+1-1=0\n'
  '-1+1-1+1=0\n'
  '-1+1-1-1=-2\n'
  '-1-1+1+1=0\n'
  '-1-1+1-1=-2\n'
  '-1-1-1+1=-2\n'
  '-1-1-1-1=-4',
  False),
 ('010-Exercise-Functions-Advanced/001_even_numbers.py', ['1 2 3 4'], '[2, 4]', False),
 ('010-Exercise-Functions-Advanced/002_sort.py', ['6 2 4'], '[2, 4, 6]', False),
 ('010-Exercise-Functions-Advanced/003_min_max_and_sum.py', ['2 4 6'],
  'The minimum number is 2\nThe maximum number is 6\nThe sum number is: 12', False),
 ('010-Exercise-Functions-Advanced/004_negative_vs_positive.py', ['1 2 -3 -4 65 -98 12 57 -84'],
  '-189\n137\nThe negatives are stronger than the positives', False),
 ('010-Exercise-Functions-Advanced/005_odd_or_even.py', ['Odd', '1 3 5 34 7 9 12 11 13 10'], '490', False),
 ('014-Error-Handling/001_so_many_exceptions.py', ['1, 4, 5'], '20', False),
 ('014-Error-Handling/001_so_many_exceptions.py', ['4, 5, 6, 1, 3'], '10', False),
 ('014-Error-Handling/001_so_many_exceptions.py', ['2, 5, 10'], '1', False),
 ('014-Error-Handling/003_repeat_text.py', ['Hello', 'Bye'], 'Variable times must be an integer', False),
 ('014-Error-Handling/003_repeat_text.py', ['Hello', 2], 'HelloHello', False),
 ('015-Exercise-Error-Handling/001_numbers_dictionary.py',
  ['one', 1, 'two', 2, 'Search', 'one', 'Remove', 'two', 'End'], "1\n{'one': 1}", False),
 ('015-Exercise-Error-Handling/001_numbers_dictionary.py', ['one', 'two', 'Search', 'Remove', 'End'],
  'The variable number must be an integer\n{}', False),
 ('015-Exercise-Error-Handling/001_numbers_dictionary.py',
  ['one', 1, 'Search', 'one', 'Remove', 'two', 'End'], "1\nNumber does not exist in dictionary\n{'one': 1}",
  False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/001_numbers.py',
  ['1 2 3 4 5', '1 2 3', 3, 'Add First 5 6', 'Remove Second 8 9 11', 'Check Subset'],
  'True\n1, 2, 3, 4, 5, 6\n1, 2, 3', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/001_numbers.py',
  ['5 4 2 9 9 5 4', '1 1 1 5 6 5', 4, 'Add First 5 6 9 3', 'Add Second 1 2 3 3 3', 'Check Subset',
   'Remove Second 1 2 3 4 5'],
  'False\n2, 3, 4, 5, 6, 9\n6', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/002_expression_evaluator.py', ['6 3 - 2 1 * 5 /'], '1', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/002_expression_evaluator.py', ['2 2 - 1 *'], '0', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/002_expression_evaluator.py',
  ['10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *'], '164', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/003_milkshakes.py',
  ['20, 24, -5, 17, 22, 60, 26', '26, 60, 22, 17, 24, 10, 55'],
  'Great! You made all the chocolate milkshakes needed!\nChocolate: 20\nMilk: 10, 55', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/003_milkshakes.py', ['-10, -2, -30, 10', '-5'],
  'Not enough milkshakes.\nChocolate: -10, -2, -30, 10\nMilk: empty', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/003_milkshakes.py', ['2, 3, 3, 7, 2', '2, 7, 3, 3, 2, 14, 6'],
  'Great! You made all the chocolate milkshakes needed!\nChocolate: empty\nMilk: 14, 6', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/004_honey.py',
  ['20 62 99 35 0 150', '120 60 10 1 70 10', '+ - + + / * - - /'],
  'Total honey made: 148\nBees left: 99, 35, 0, 150', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/004_honey.py', ['30', '15 9 5 150 8', '* + + * -'],
  'Total honey made: 4500\nNectar left: 15, 9, 5', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/005_santas_present_factory.py',
  ['10 -5 20 15 -30 10', '40 60 10 4 10 0'],
  'The presents are crafted! Merry Christmas!\nMaterials left: 20, -5, 10\nBicycle: 1\nTeddy bear: 2',
  False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/005_santas_present_factory.py',
  ['30 5 15 60 0 30', '-15 10 5 -15 25'],
  'No presents this Christmas!\nMaterials left: 20, 30\nDoll: 1\nTeddy bear: 1', False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/006_paint_colors.py', ['d yel blu e low redd'],
  "['yellow', 'blue', 'red']", False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/006_paint_colors.py', ['r ue nge ora bl ed'], "['red', 'blue']",
  False),
 ('016-Exercise-Stacks-Queues-Tuples-And-Sets/006_paint_colors.py', ['re ple blu pop e pur d'],
  "['red', 'purple', 'blue']", False),
 ('017-Exercise-Multidimensional-Lists-Second/001_flatten_lists.py', ['1 2 3 |4 5 6 |  7  88'],
  '7 88 4 5 6 1 2 3', False),
 ('017-Exercise-Multidimensional-Lists-Second/001_flatten_lists.py', ['7 | 4  5|1 0| 2 5 |3'],
  '3 2 5 1 0 4 5 7', False),
 ('017-Exercise-Multidimensional-Lists-Second/002_matrix_modification.py',
  [3, '1 2 3', '4 5 6', '7 8 9', 'Add 0 0 5', 'Subtract 1 1 2', 'END'], '6 2 3\n4 3 6\n7 8 9', False),
 ('017-Exercise-Multidimensional-Lists-Second/002_matrix_modification.py',
  [4, '1 2 3 4', '5 6 7 8', '8 7 6 5', '4 3 2 1', 'Add 4 4 100', 'Add 3 3 100', 'Subtract -1 -1 42',
   'Subtract 0 0 42', 'END'],
  'Invalid coordinates\nInvalid coordinates\n-41 2 3 4\n5 6 7 8\n8 7 6 5\n4 3 2 101', False),
 ('017-Exercise-Multidimensional-Lists-Second/003_knight_game.py', [2, 'KK', 'KK'], '0', False),
 ('017-Exercise-Multidimensional-Lists-Second/004_easter_bunny.py',
  [5, '1 3 7 9 11', 'X 5 4 X 63', '7 3 21 95 1', 'B 1 73 4 9', '9 2 33 2 0'],
  'right\n[3, 1]\n[3, 2]\n[3, 3]\n[3, 4]\n87', False),
 ('017-Exercise-Multidimensional-Lists-Second/004_easter_bunny.py',
  [8, '4 18 9 7 24 41 52 11', '54 21 19 X 6 34 75 57', '76 67 7 44 76 27 56 37', '92 35 25 37 52 34 56 72',
   '35 X 1 45 4 X 37 63', '105 X B 2 12 43 5 19', '48 19 35 20 32 27 42 4', '73 88 78 32 37 52 X 22'],
  'down\n[6, 2]\n[7, 2]\n113', False),
 ('017-Exercise-Multidimensional-Lists-Second/005_alice_in_wonderland.py',
  [5, '. A . . 1', 'R . 2 . .', '4 7 . 1 .', '. . . 2 .', '. 3 . . .', 'down', 'right', 'left', 'down', 'up',
   'left'],
  "Alice didn't make it to the tea party.\n. * . . 1\n* * * . .\n4 * . 1 .\n. . . 2 .\n. 3 . . .", False),
 ('017-Exercise-Multidimensional-Lists-Second/005_alice_in_wonderland.py',
  [7, '. A . 1 1 . .', '9 . . . 6 . 5', '. 6 . R . . .', '. 3 . . 1 . .', '. . . 2 . . 2', '. 3 . . 1 . .',
   '. 8 3 . . . 2', 'left', 'down', 'down', 'right'],
  'She did it! She went to the party.\n'
  '* * . 1 1 . .\n'
  '* . . . 6 . 5\n'
  '* * . R . . .\n'
  '. 3 . . 1 . .\n'
  '. . . 2 . . 2\n'
  '. 3 . . 1 . .\n'
  '. 8 3 . . . 2',
  False),
 ('017-Exercise-Multidimensional-Lists-Second/006_range_day.py',
  ['. . . . .', 'x . . . .', '. A . . .', '. . . x .', '. x . . x', 3, 'shoot down', 'move right 4',
   'move left 1'],
  'Training not completed! 3 targets left.\n[4, 1]', False),
 ('017-Exercise-Multidimensional-Lists-Second/006_range_day.py',
  ['. . . . .', '. . . . .', '. A x . .', '. . . . .', '. x . . .', 2, 'shoot down', 'shoot right'],
  'Training completed! All 2 targets hit.\n[4, 1]\n[2, 2]', False),
 ('017-Exercise-Multidimensional-Lists-Second/006_range_day.py',
  ['. . . . .', '. . . . .', '. . x . .', '. . . . .', '. x . . A', 3, 'shoot down', 'move right 2',
   'shoot left'],
  'Training not completed! 1 targets left.\n[4, 1]', False),
 ('017-Exercise-Multidimensional-Lists-Second/007_present_delivery.py',
  [5, 4, '- X V -', '- S - V', '- - - -', 'X - - -', 'up', 'right', 'down', 'right', 'Christmas morning'],
  '- - - -\n- - - S\n- - - -\nX - - -\nGood job, Santa! 2 happy nice kid/s.', False),
 ('017-Exercise-Multidimensional-Lists-Second/007_present_delivery.py',
  [3, 4, '- - - -', 'V - X -', '- V C V', '- - - S', 'left', 'up'],
  'Santa ran out of presents!\n- - - -\nV - - -\n- - S -\n- - - -\nNo presents for 1 nice kid/s.', False),
 ('021-Exam-Preparation/001_fireworks_show.py',
  ['5, 6, 4, 16, 11, 5, 30, 2, 3, 27', '1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22'],
  'Congrats! You made the perfect firework show!\n'
  'Palm Fireworks: 4\n'
  'Willow Fireworks: 3\n'
  'Crossette Fireworks: 3',
  False),
 ('021-Exam-Preparation/001_fireworks_show.py', ['-15, -8, 0, -16, 0, -22', '10, 5'],
  "Sorry. You can't make the perfect firework show.\n"
  'Explosive Power left: 10, 5\n'
  'Palm Fireworks: 0\n'
  'Willow Fireworks: 0\n'
  'Crossette Fireworks: 0',
  False),
 ('021-Exam-Preparation/002_darts.py',
  ['Ivan, Peter', '12 21 18 4 20 7 11', '9 D D D D D 10', '15 D T T T D 3', '2 D T B T D 19',
   '17 D T T T D 6', '22 D D D D D 14', '5 8 23 13 16 1 24', '(3, 3)'],
  'Ivan won the game with 1 throws!', False),
 ('021-Exam-Preparation/002_darts.py',
  ['George, Hristo', '17 8 21 6 13 3 24', '16 D D D D D 14', '7 D T T T D 15', '23 D T B T D 2',
   '9 D T T T D 22', '19 D D D D D 10', '12 18 4 20 5 11 1', '(1, 0)', '(2, 3)', '(0, 0)', '(4, 2)', '(5, 1)',
   '(3, 1)', '(0, 0)', '(2, 3)'],
  'Hristo won the game with 4 throws!', False)]

# (script, expression evaluated against the script's namespace, expected value)
FUNCTION_CASES = [('009-Functions-Advanced/003_multiplication_function.py', 'multiply(1, 4, 5)', 20),
 ('009-Functions-Advanced/003_multiplication_function.py', 'multiply(4, 5, 6, 1, 3)', 360),
 ('009-Functions-Advanced/003_multiplication_function.py', 'multiply(2, 0, 1000, 5000)', 0),
 ('009-Functions-Advanced/004_operate.py', 'operate("+", 1, 2, 3)', 6),
 ('009-Functions-Advanced/004_operate.py', 'operate("*", 3, 4)', 12),
 ('009-Functions-Advanced/005_person_info.py', 'get_info(**{"name": "George", "town": "Sofia", "age": 20})',
  'This is George from Sofia and he is 20 years old'),
 ('010-Exercise-Functions-Advanced/006_arguments_length.py', 'args_length(1, 32, 5)', 3),
 ('010-Exercise-Functions-Advanced/006_arguments_length.py', 'args_length([1, 2, 3])', 1),
 ('010-Exercise-Functions-Advanced/007_concatenate.py', 'concatenate("Soft", "Uni", "Is", "Great", "!")',
  'SoftUniIsGreat!'),
 ('010-Exercise-Functions-Advanced/008_even_or_odd.py', 'even_odd(1, 2, 3, 4, 5, 6, "even")', [2, 4, 6]),
 ('010-Exercise-Functions-Advanced/008_even_or_odd.py', 'even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd")',
  [1, 3, 5, 7, 9]),
 ('010-Exercise-Functions-Advanced/009_function_executor.py',
  'func_executor((lambda a, b: a + b, (1, 2)), (lambda a, b: a * b, (2, 4)))', [3, 8]),
 ('010-Exercise-Functions-Advanced/010_keyword_arguments_length.py',
  "kwargs_length(**{'name': 'Peter', 'age': 25})", 2),
 ('010-Exercise-Functions-Advanced/011_age_assignment.py', 'age_assignment("Peter", "George", G=26, P=19)',
  {'George': 26, 'Peter': 19}),
 ('010-Exercise-Functions-Advanced/012_recursion_palindrome.py', 'palindrome("abcba", 0)',
  'abcba is a palindrome'),
 ('010-Exercise-Functions-Advanced/012_recursion_palindrome.py', 'palindrome("peter", 0)',
  'peter is not a palindrome'),
 ('010-Exercise-Functions-Advanced/013_recursive_power.py', 'recursive_power(2, 10)', 1024),
 ('010-Exercise-Functions-Advanced/013_recursive_power.py', 'recursive_power(10, 100)',
  10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000),
 ('021-Exam-Preparation/003_cupcake_shop.py',
  'stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry")',
  ['choco', 'vanilla', 'banana', 'caramel', 'berry']),
 ('021-Exam-Preparation/003_cupcake_shop.py',
  'stock_availability(["chocolate", "vanilla", "banana"], "sell")', ['vanilla', 'banana']),
 ('021-Exam-Preparation/003_cupcake_shop.py',
  'stock_availability(["chocolate", "vanilla", "banana"], "sell", 3)', []),
 ('021-Exam-Preparation/003_cupcake_shop.py',
  'stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate")', ['banana']),
 ('021-Exam-Preparation/003_cupcake_shop.py',
  'stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie")',
  ['chocolate', 'vanilla', 'banana'])]

# (script, stdin lines, expected stdout before the error, exception name)
RAISES_CASES = [('014-Error-Handling/002_value_cannot_be_negative.py', [1, 4, -5, 3, 10], '', 'ValueCannotBeNegative'),
 ('015-Exercise-Error-Handling/002_email_validator.py', ['abc@abv.bg'], '', 'NameTooShortError'),
 ('015-Exercise-Error-Handling/002_email_validator.py', ['peter@gmail.com', 'petergmail.com'],
  'Email is valid', 'MustContainAtSymbolError'),
 ('015-Exercise-Error-Handling/002_email_validator.py', ['peter@gmail.hotmail'], '', 'InvalidDomainError')]

# Folders with their own unittest suites next to the code.
UNITTEST_FOLDERS = ["018-Workshop-Connect-Four", "019-Workshop-Tic-Tac-Toe", "020-Exercise-Modules-Gui-Shop"]

COMPILE_ONLY = {'006-Exercise-Multidimensional-Lists/007_bombs.py': 'the PDF example is cut off at a page break',
 '007-Comprehension': 'no PDF for this lesson in the current course',
 '008-Exercise-Comprehension': 'no PDF for this lesson in the current course',
 '012-Exercise-File-Handling': 'the exercise PDF contains no task text',
 '013-Modules': 'covered by tests/test_repo.py'}


def run(script, stdin, cwd=None):
    return subprocess.run(
        [sys.executable, str(ROOT / script)],
        input="\n".join(map(str, stdin)) + "\n",
        capture_output=True, text=True, timeout=10, cwd=cwd or (ROOT / script).parent,
    )


def lines(text, unordered=False):
    result = [line.rstrip() for line in text.strip().splitlines()]
    return sorted(result) if unordered else result


class TestStdinScripts(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, unordered in STDIN_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(lines(result.stdout, unordered), lines(expected, unordered))


class TestFunctions(unittest.TestCase):
    def test_examples(self):
        for script, expression, expected in FUNCTION_CASES:
            with self.subTest(script=script, expression=expression):
                with contextlib.redirect_stdout(io.StringIO()):
                    namespace = runpy.run_path(str(ROOT / script), run_name="lesson")
                    self.assertEqual(eval(expression, namespace), expected)


class TestRaises(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected, error in RAISES_CASES:
            with self.subTest(script=script, stdin=stdin):
                result = run(script, stdin)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(error, result.stderr)
                self.assertEqual(lines(result.stdout), lines(expected))


class TestFileHandling(unittest.TestCase):
    """Runs the scripts in a temporary copy, so files they create never touch the repo."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        shutil.copytree(ROOT / "Files", self.tmp / "Files")
        self.lesson = shutil.copytree(ROOT / "011-File-Handling", self.tmp / "011-File-Handling")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_script(self, name):
        return subprocess.run([sys.executable, name], capture_output=True, text=True, timeout=10, cwd=self.lesson)

    def test_opener_and_reader(self):
        self.assertEqual(self.run_script("001_file_opener.py").stdout.strip(), "File found")
        self.assertEqual(self.run_script("002_file_reader.py").stdout.strip(), "15")

    def test_writer_and_delete(self):
        self.run_script("003_file_writer.py")
        self.assertEqual((self.lesson / "my_first_file.txt").read_text(), "I just created my first file!")
        self.assertEqual(self.run_script("004_file_delete.py").stdout, "")
        self.assertEqual(self.run_script("004_file_delete.py").stdout.strip(), "File already deleted!")
        self.assertEqual(self.run_script("005_file_delete_if_exists.py").returncode, 0)

    def test_word_count(self):
        for name in ("006_word_count.py", "007_word_count_with_functions.py"):
            with self.subTest(name=name):
                self.run_script(name)
                self.assertEqual(lines((self.lesson / "output.txt").read_text()), ["is - 3", "quick - 2", "fault - 1"])


class TestUnittestFolders(unittest.TestCase):
    def test_suites_pass(self):
        for folder in UNITTEST_FOLDERS:
            with self.subTest(folder=folder):
                result = subprocess.run([sys.executable, "-m", "unittest", "-q"], cwd=ROOT / folder,
                                        capture_output=True, text=True, timeout=60)
                self.assertEqual(result.returncode, 0, result.stderr)


class TestEveryScriptIsCovered(unittest.TestCase):
    def test_coverage(self):
        covered = {c[0] for c in STDIN_CASES + RAISES_CASES} | {c[0] for c in FUNCTION_CASES}
        covered |= {f"011-File-Handling/{p.name}" for p in (ROOT / "011-File-Handling").glob("*.py")}
        missing = []
        for path in sorted(ROOT.glob("0*/**/*.py")):
            rel = path.relative_to(ROOT).as_posix()
            folder = rel.split("/")[0]
            if rel in covered or rel in COMPILE_ONLY or folder in COMPILE_ONLY or folder in UNITTEST_FOLDERS:
                continue
            missing.append(rel)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
