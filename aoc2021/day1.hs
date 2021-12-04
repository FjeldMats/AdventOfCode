import           System.IO
import           Text.Printf (printf)

getNumbers :: String -> [Int]
getNumbers str = map (read :: String -> Int) $ words str

isIncrement :: Int -> Int -> Int
isIncrement a b =
  if a < b
    then 1
    else 0

-- part 1
compareFirstTwo :: [Int] -> Int
compareFirstTwo (a:b:xs) = isIncrement a b
compareFirstTwo [x]      = 0
compareFirstTwo []       = 0

countIncrements :: [Int] -> Int
countIncrements [] = 0
countIncrements xs = compareFirstTwo xs + countIncrements (tail xs)

-- part 2
compareFirstThree :: [Int] -> Int
compareFirstThree (a:b:c:d:xs) = isIncrement (sum [a, b, c]) (sum [b, c, d])
compareFirstThree (x:xs)       = 0
compareFirstThree []           = 0

countSumOfIncrements :: [Int] -> Int
countSumOfIncrements [] = 0
countSumOfIncrements xs = compareFirstThree xs + countSumOfIncrements (tail xs)

main :: IO ()
main = do
  example <- readFile "aoc2021/inputs/ex1.txt"
  content <- readFile "aoc2021/inputs/1.txt"
  let numbers = getNumbers example
  let numberInput = getNumbers content
  putStrLn "test case: "
  print numbers
  putStrLn ""
    -- part 1
  let part1 = "part 1: " ++ show (countIncrements numberInput)
  putStrLn part1
  putStrLn ""
    -- part 2
  let part2 = "part 2: " ++ show (countSumOfIncrements numberInput)
  putStrLn part2
