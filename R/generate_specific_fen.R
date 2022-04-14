place_kings <- function(brd){
  ###
  #  Function that puts the two kings on the board
  #  and makes sure that they are not adjacent
  ###
  
  while (TRUE) {
    # generate positions for white and black kings
    rank_white <- sample(1:8, 1) ; file_white <- sample(1:8, 1)
    rank_black <- sample(1:8, 1) ; file_black <- sample(1:8, 1)
    
    # compute the differences between ranks and files
    diff_vec <- c(abs(rank_white - rank_black), abs(file_white - file_black))
    
    # if the two kings are not adjacent, place them on the board
    if (sum(diff_vec) > 2 | setequal(diff_vec, c(0,2))) {
      brd[rank_white, file_white] <- "K"
      brd[rank_black, file_black] <- "k"
      break
    }
  }
  
  return(brd)
}



pawn_on_extreme_ranks <- function(pc, pr){
  ###
  #  Function that checks whether a pawn is on the first or eight rank
  #  (such a situation is not possible in chess)
  ### 
  
  if (pc %in% c("P","p") & pr %in% c(1,8))
    return(TRUE)
  
  else
    return(FALSE)
}



populate_board <- function(brd, pcs){
  ###
  #  Function that puts pieces on the board making sure that they
  #  are not on the same squares, and verifying for pawn_on_extreme_ranks
  ###
  
  pieces <- pcs
    
  # place pieces one by one until we have them
  while (length(pieces) > 0){
    piece_rank <- sample(1:8, 1) ; piece_file <- sample(1:8, 1)
    piece <- pieces[1]
    # check if square is empty and it is not a pawn on an extreme rank
    if (brd[piece_rank, piece_file] == " " & !pawn_on_extreme_ranks(piece, piece_rank)){
      brd[piece_rank, piece_file] <- piece
      pieces <- pieces[-1]
    }
  }
  
  return(brd)
}



fen_from_board <- function(brd){
  ###
  #  Function that prints out the FEN of a given input board
  ###
  
  # create vector of FEN positions by row
  fen <- apply(brd, 1, function(x) {
    r <- rle(x) 
    paste(ifelse(r$values == " ", r$lengths, r$values), collapse = "")
  })
  
  # paste them together with separator '/' and add the final string
  fen <- paste(paste(fen, collapse = "/"), "w - - 0 1")
  
  return(fen)
}



generate_specific_fen <- function(
  white_pawns = 0, white_knights = 0, white_bishops = 0, white_rooks = 0, white_queens = 0,
  black_pawns = 0, black_knights = 0, black_bishops = 0, black_rooks = 0, black_queens = 0
){
  ###
  #  This function calls all the functions above and generates the board representation,
  #  with a specific number of pieces, along with its FEN.
  #  Inputs of this function are the number of specific pieces chosen by the user (default: 0)
  ###
  
  # initialization
  board <- matrix(" ", nrow = 8, ncol = 8)
  
  # generate vector of pieces to be placed on the board
  piece_list <- c("P", "N", "B", "R", "Q", "p", "n", "b", "r", "q")
  piece_numbers <- c(white_pawns, white_knights, white_bishops, white_rooks, white_queens,
                     black_pawns, black_knights, black_bishops, black_rooks, black_queens)
  pieces <- rep(piece_list, piece_numbers)
  
  # place kings on board
  board <- place_kings(board)
  
  # put other pieces on board
  board <- populate_board(board, pieces)
  
  # print board and FEN
  print(board)
  cat("\n")
  cat(fen_from_board(board))
}
