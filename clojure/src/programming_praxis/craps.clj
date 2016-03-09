; See http://programmingpraxis.com/2011/11/04/craps/

(defn dice []
  (+ (inc (rand-int 6)) (inc (rand-int 6))))

(def win? #{7 11})
(def lose? #{2 3 12})

(defn game []
  (loop [rolls 1 result (dice)]
    (cond
      (win? result) (list true rolls)
      (lose? result) (list false rolls)
      :else (recur (inc rolls) (dice)))))

(defn games [n]
  (loop [i 0 results ()]
    (if (= i n) results
      (recur (inc i) (conj results (game))))))

(defn stats [results]
  (let [rolls (map #(second %1) results) ngames (count results)]
    (println "Wins:" (count (filter #(first %1) results)) "/" ngames)
    (println "Avg rolls:" (/ (double (apply + rolls)) ngames))
    (println "Max rolls:" (reduce max rolls))))

(stats (games 1000))