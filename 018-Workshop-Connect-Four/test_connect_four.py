import unittest

from connect_four import create_board, drop_piece, is_full, is_winner


class TestConnectFour(unittest.TestCase):
    def setUp(self):
        self.board = create_board()

    def test_pieces_stack_from_the_bottom(self):
        self.assertEqual(drop_piece(self.board, 0, "1"), 5)
        self.assertEqual(drop_piece(self.board, 0, "2"), 4)

    def test_invalid_and_full_columns(self):
        with self.assertRaises(ValueError):
            drop_piece(self.board, 7, "1")
        for _ in range(6):
            drop_piece(self.board, 0, "1")
        with self.assertRaises(ValueError):
            drop_piece(self.board, 0, "1")

    def test_horizontal_vertical_and_diagonal_wins(self):
        for col in range(4):
            row = drop_piece(self.board, col, "1")
        self.assertTrue(is_winner(self.board, row, 3, "1"))

        board = create_board()
        for _ in range(4):
            row = drop_piece(board, 6, "2")
        self.assertTrue(is_winner(board, row, 6, "2"))

        board = create_board()
        for col, fillers in enumerate(range(4)):
            for _ in range(fillers):
                drop_piece(board, col, "2")
            row = drop_piece(board, col, "1")
        self.assertTrue(is_winner(board, row, 3, "1"))

    def test_three_in_a_row_is_not_a_win(self):
        for col in range(3):
            row = drop_piece(self.board, col, "1")
        self.assertFalse(is_winner(self.board, row, 2, "1"))

    def test_full_board(self):
        self.assertFalse(is_full(self.board))
        for col in range(7):
            for _ in range(6):
                drop_piece(self.board, col, "1")
        self.assertTrue(is_full(self.board))


if __name__ == "__main__":
    unittest.main()
