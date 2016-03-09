(ns programming_praxis.core_test
  (:use clojure.test
        programming_praxis.core))

(deftest four-sum-test
  (testing "Testing sum solve"
    (is (= '((3 1 0 -4) (0 0 0 0)) (four-sum '(2 3 1 0 -4 1))))))