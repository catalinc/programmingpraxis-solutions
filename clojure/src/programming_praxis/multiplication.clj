; See http://programmingpraxis.com/2011/11/18/grade-school-multiplication/

(defn digits [n]
	(loop [k n acc ()]
		(if (zero? k) 
			acc 
			(recur (quot k 10) (conj acc (rem k 10))))))

(defn partials [a b]
	(map #(* % a) (digits b)))

(defn repeated [n x]
	(apply str (repeat n x)))

(defn rpad [len pad n]
	(str (repeated (- len (count (digits n))) pad) n))

(defn print-multiplication [a b]
	(let [r (* a b) rlen (count (digits r)) ps (reverse (partials a b))]
		(println  (rpad rlen " " a))
		(println  (rpad rlen " " b))
        (when (not (= 1 (count (filter #(not (zero? %)) ps))))
		  (println  (repeated rlen "-"))
          (loop [p ps i 0 suffix ""]
              (when (seq p)
                  (when (not (zero? (first p)))
                      (println (str (rpad (- rlen i) " " (first p)) suffix)))
                  (recur 
                      (rest p) 
                      (inc i)
                      (if (zero? (first p)) (str suffix "0") "")))))
                      (println (repeated rlen "-"))
		(println r)))

(defn problem-a [filename]
  (let [stream (java.util.Scanner. (java.io.File. filename))]
        (while (.hasNextInt stream)
          (let [a (.nextInt stream) b (.nextInt stream)]
            (when (and (> a 0) (> b 0)
              (print-multiplication a b))))))

(problem-a "multiplication.in")