open System

let input() = Int32.Parse(Console.ReadLine())

let rec game() =
    printfn "DEPTH CHARGE GAME"
    printfn "DIMENSION OF SEARCH AREA?"
    let g = input()
    let n = int ((log (float g)) / (log (float 2))) + 1
    printfn "YOU ARE CAPTAIN OF THE DESTROYER USS DIGITAL."
    printfn "AN ENEMY SUB HAS BEEN CAUSING YOU TROUBLE. YOUR"
    printfn "MISSION IS TO DESTROY IT. YOU HAVE %d SHOTS." n
    printfn "SPECIFY DEPTH CHARGE EXPLOSION POINT WITH A"
    printfn "TRIO OF NUMBERS -- THE FIRST TWO ARE THE"
    printfn "SURFACE COORDINATES; THE THIRD IS THE DEPTH."   
    printfn "GOOD LUCK !"
    let rnd = Random()
    let a, b, c = rnd.Next(1, g + 1), rnd.Next(1, g + 1), rnd.Next(1, g + 1)
    let report x y z =
        printf "SONAR REPORTS SHOT WAS "
        if y > b then printf "NORTH"
        if y < b then printf "SOUTH"
        if x > a then printf "EAST"
        if x < a then printf "WEST"
        if y <> b || x <> a then printf " AND "
        if z > c then printfn "TOO LOW."
        if z < c then printfn "TOO HIGH."
        if z = c then printfn "DEPTH OK." 
    let another() = 
        printfn "ANOTHER GAME (Y OR N)?"
        let o = Console.ReadLine().ToUpper()
        match o with 
        | "Y" -> game()
        | _   -> printfn "OK.  HOPE YOU ENJOYED YOURSELF."
                 exit 0
    for i = 1 to n do
        printfn "TRIAL #%d" i
        let x, y, z = input(), input(), input()
        if abs(a - x) = 0 && abs(b - y) = 0 && abs(z - c) = 0 then
            printfn "B O O M ! !  YOU FOUND IT IN %d TRIES!" i
            another()
        else report x y z
    printfn "YOU HAVE BEEN TORPEDOED! ABANDON SHIP!"
    printfn "THE SUBMARINE WAS AT %d %d %d" a b c
    another()

game()