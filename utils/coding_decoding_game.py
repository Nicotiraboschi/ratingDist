import chess
import re
import io 


def encoding_game (game):
    
    pgn_moves = game['pgn']
    # Extract only the moves from the PGN without additional information
    cleaned_pgn = re.sub(r'\[.*?\]|\{.*?\}', "", pgn_moves).strip()
    cleaned_moves = re.sub(r'\d+\.\.\s*', '', cleaned_pgn)
    cleaned_moves = re.sub(r'\s\s\.\s', ' ', cleaned_moves)
    cleaned_moves = re.sub(r'\s\s', ' ', cleaned_moves)
    cleaned_moves = re.sub(r'\d+\-\d+', '', cleaned_moves)
    
    # MAIN ENCODING THE GAME
    def encode_game(pgn):
        # Parse the PGN to get the moves
        board = chess.Board()
        game = chess.pgn.read_game(io.StringIO(pgn))
        moves = [move for move in game.mainline_moves()]
        # Initialize variables
        encoded_moves = ""

        for move in moves:
            # Check the number of legal moves in the current position
            legal_moves = list(board.legal_moves)
            num_legal_moves = len(legal_moves)
            # Dynamically adjust the number of bits
            dynamic_bits = num_legal_moves.bit_length()
            # Encode the move index using the dynamic number of bits
            move_index = legal_moves.index(move)
            encoded_moves += format(move_index, f'0{dynamic_bits}b')
            # Make the move on the board
            board.push(move)

        return encoded_moves

    # MAIN DECODING THE GAME
    def decode_game(encoded_moves):
        # Initialize variables
        board = chess.Board()
        decoded_moves = ""

        # Initialize dynamic bits
        legal_moves = list(board.legal_moves)
        dynamic_bits = len(legal_moves).bit_length()

        while encoded_moves:
            # Check if there are enough characters in encoded_moves
            if len(encoded_moves) >= dynamic_bits:
                # Extract the next move index using the dynamic number of bits
                move_index = int(encoded_moves[:dynamic_bits], 2) % 256
                encoded_moves = encoded_moves[dynamic_bits:]

                # Check if move_index is within the range of legal_moves
                if move_index < len(legal_moves):
                    # Get the move from the move index
                    move = legal_moves[move_index]
                    # Make the move on the board
                    board.push(move)
                    # Update the dynamic bits based on the number of legal moves
                    legal_moves = list(board.legal_moves)
                    dynamic_bits = len(legal_moves).bit_length()
                    # Append the UCI representation of the move to the decoded moves string
                    decoded_moves += move.uci()
                else:
                    # Handle the case where move_index is out of range
                    print(f"Warning: Move index {move_index} is out of range. Skipping the move. ⬆️")
            else:
                # Break out of the loop if there are not enough characters
                break

        def insert_space(string, every_x):
            return ' '.join([string[i:i+every_x] for i in range(0, len(string), every_x)])

        # Example usage
        encoded_game_with_spaces = insert_space(decoded_moves, 4)

        return encoded_game_with_spaces

    # Example usage
    # encoded_game = encode_game(cleaned_moves)
    # decoded_game = decode_game(encoded_game)
    return encode_game(cleaned_moves)
