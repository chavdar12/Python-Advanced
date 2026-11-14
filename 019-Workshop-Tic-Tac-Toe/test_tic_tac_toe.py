import unittest

from tic_tac_toe import check_if_won, create_board, is_full, place, position_to_cell


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.board = create_board()

    def test_position_to_cell(self):
        self.assertEqual(position_to_cell(1), (0, 0))
        self.assertEqual(position_to_cell(6), (1, 2))
        self.assertEqual(position_to_cell(9), (2, 2))

    def test_place_validates(self):
        place(self.board, 5, "X")
        with self.assertRaises(ValueError):
            place(self.board, 5, "O")
        with self.assertRaises(ValueError):
            place(self.board, 10, "O")

    def test_wins(self):
        for p in (1, 2, 3):
            place(self.board, p, "X")
        self.assertTrue(check_if_won(self.board, "X"))
        board = create_board()
        for p in (3, 5, 7):
            place(board, p, "O")
        self.assertTrue(check_if_won(board, "O"))
        board = create_board()
        for p in (2, 5, 8):
            place(board, p, "O")
        self.assertTrue(check_if_won(board, "O"))

    def test_no_win_and_draw(self):
        for p, s in zip(range(1, 10), "XOXXOOOXX"):
            place(self.board, p, s)
        self.assertFalse(check_if_won(self.board, "X"))
        self.assertFalse(check_if_won(self.board, "O"))
        self.assertTrue(is_full(self.board))


if __name__ == "__main__":
    unittest.main()
