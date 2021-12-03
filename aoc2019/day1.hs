getNumbers :: String -> [Int]
getNumbers str = map (read :: String -> Int) $ words str

-- round(num / 3) - 2
calcFuel :: Int -> Int
calcFuel x =
  if (div x 3 - 2) > 0
    then div x 3 - 2
    else 0

-- part 2
recursiveFuel :: Int -> Int
recursiveFuel 0 = 0
recursiveFuel x = calcFuel x + recursiveFuel (calcFuel x)

main :: IO ()
main = do
  content <- readFile "aoc2019/inputs/1.txt"
  let numberInput = getNumbers content
  print $ sum [calcFuel x | x <- numberInput]
    --part 2
  print $ sum [recursiveFuel x | x <- numberInput]
