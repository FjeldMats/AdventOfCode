{-# OPTIONS_GHC -Wno-incomplete-patterns #-}

getCommands :: String -> [String]
getCommands str = [read x :: String | x <- wordsWhen (== '\n') str]

getCommandAndValue :: String -> (String, Int)
getCommandAndValue str =
  (head $ wordsWhen (== ' ') str, read (wordsWhen (== ' ') str !! 1) :: Int)

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =
  case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
      where (w, s'') = break p s'

-- pos = (Horizontal, Depth)
calcPos :: (String, Int) -> (Int, Int)
calcPos ("forward", b) = (b, 0)
calcPos ("up", b)      = (0, -b)
calcPos ("down", b)    = (0, b)

followInstructions :: [(String, Int)] -> [(Int, Int)] -> [(Int, Int)]
followInstructions [] pos = pos
followInstructions lst pos =
  calcPos (head lst) : followInstructions (tail lst) pos

-- part 2
-- pos = (Horizontal, Depth, aim)
calcPos2 :: (String, Int) -> (Int, Int, Int)
calcPos2 ("forward", b) = (b, 0, 0)
calcPos2 ("up", b)      = (0, 0, -b)
calcPos2 ("down", b)    = (0, 0, b)

followInstructions2 :: [(String, Int)] -> [(Int, Int, Int)] -> [(Int, Int, Int)]
followInstructions2 [] pos = pos
followInstructions2 lst pos =
  calcPos2 (head lst) : followInstructions2 (tail lst) pos

combine :: (Int, Int, Int) -> [(Int, Int, Int)] -> [(Int, Int, Int)]
combine (a, b, c) [] = [(a, b, c)]
combine (a, b, c) ((z, 0, 0):d) =
  (a + z, b + (z * c), c) : combine (a + z, b + (z * c), c) d
combine (a, b, c) ((0, 0, y):d) = (a, b, c + y) : combine (a, b, c + y) d

mult :: (Int, Int, Int) -> Int
mult (a, b, c) = a * b

main :: IO ()
main = do
  content <- readFile "aoc2021/inputs/2.txt"
  exampleContent <- readFile "aoc2021/inputs/ex2.txt"
  --step 1
  let commands = [getCommandAndValue x | x <- wordsWhen (== '\n') content]
  let steps = followInstructions commands []
  print $ sum (map fst steps) * sum (map snd steps)
  --step 2
  let commands = [getCommandAndValue x | x <- wordsWhen (== '\n') content]
  let steps = followInstructions2 commands []
  --print steps
  print $ mult $last $ combine (0, 0, 0) steps
