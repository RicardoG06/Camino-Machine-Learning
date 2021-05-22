#Probabilidad de que tenga cancer: 1/ 100000
#Probabilidad de que no tenga cancer: 99999/100000
#Probabilidad de que tenga sintomas y sea cancer : 1
#Probabilidad de que no tenga sintomas y sea cancer : 0
#Probabilidad de que tenga sintomas y no sea cancer : 10/99999
#Probabilidad de que no tenga sintomas y no sea cancer : 99989/99999

#Queremos hallar: 
#Probabilidad de que una persona con sintomas pueda tener cancer

# Implementamos la P(B) = P(A)P(B|A) + P(¬A)P(B|¬A)
def prob_b(prob_a, prob_b_dado_a, prob_b_complemento_a):
    calculo = prob_a * prob_b_dado_a + (1-prob_a) * prob_b_complemento_a
    return calculo

# Implementamos la P(A|B) = P(B|A)P(A) / P(B)
def cal_bayes(prob_a, prob_b_dado_a, prob_b_complemento_a):
    prob_evento = prob_b(prob_a, prob_b_dado_a, prob_b_complemento_a)
    calculo = (prob_b_dado_a * prob_a)/prob_evento

    return calculo

if __name__ == "__main__":
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    
    resultado = cal_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma_dado_no_cancer)

    print(resultado)

