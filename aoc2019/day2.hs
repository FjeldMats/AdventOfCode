getNumbers :: String -> [Int]
getNumbers str = [read x :: Int | x <- wordsWhen (== ',') str]

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
  "" -> []
  s' -> w : wordsWhen p s''
    where
      (w, s'') = break p s'

getNumber :: [Int] -> Int -> Int
getNumber lst n = lst !! n

getSubList :: [Int] -> Int -> Int -> [Int]
getSubList lst start end = drop start . take end $ lst

find :: Eq t => t -> [t] -> Bool
find _ [] = False
find n (x : xs)
  | x == n = True
  | otherwise = find n xs

checkHalt :: [Int] -> Int -> Bool
{-

checkHalt lst index =
  99 `elem` [x | x <- getSubList lst index (index + 3)]
    || null [x | x <- getSubList lst index (index + 3)]
-}

checkHalt lst index = getNumber lst index == 99

doStep :: [Int] -> Int -> Int
doStep lst n =
  if getNumber lst n == 1
    then getNumber lst (lst !! (n + 1)) + getNumber lst (lst !! (n + 2))
    else getNumber lst (lst !! (n + 1)) * getNumber lst (lst !! (n + 2))

replace :: Int -> a -> [a] -> [a]
replace pos newVal list = take pos list ++ newVal : drop (pos + 1) list

intCode lst index =
  if checkHalt lst index
    then head lst
    else intCode (replace (getNumber lst (index + 3)) (doStep lst index) lst) (index + 4)

runProgram lst = intCode lst 0

main = do
  content <- readFile "aoc2019/inputs/2.txt"
  let numbers = getNumbers content

  let newNumbers1 = replace 1 12 numbers
  let newNumbers2 = replace 2 2 newNumbers1

  print $ runProgram newNumbers2