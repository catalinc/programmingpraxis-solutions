; Solution for http://programmingpraxis.com/2012/09/07/the-first-two-programs/

(use 'clojure.contrib.math)

(defn hello-world []
 (println "Hello World"))

(hello-world)

(defn fahrenheit-to-celsius
 [min max step]
  (let [k (/ 5 9) limit (- max step)]
    (loop [f min]
      (printf "%d\t%d\n" f (round (* (- f 32) k)))
      (if (<= f limit)
        (recur (+ f step))))))

(fahrenheit-to-celsius 0 300 20)