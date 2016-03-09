(ns programming_praxis.core
  (:use clojure.contrib.combinatorics))

(defn collect-if-solution 
  [pair sum sums solutions]
  (if (contains? sums (- sum))
    (conj solutions (sort (concat pair (get sums (- sum)))))
    solutions))

(defn four-sum 
  [nums]
  "See http://programmingpraxis.com/2012/08/14/4sum/"
  (loop [sums {} pairs (selections nums 2) solutions ()]
    (if (empty? pairs)
      (distinct solutions)
      (let [pair (first pairs)
            sum  (apply + pair)]
          (recur
            (assoc sums sum pair)
            (rest pairs)
            (collect-if-solution pair sum sums solutions))))))

(defn -main 
  [& args]
  (println (four-sum '(2 3 1 0 -4 1))))
