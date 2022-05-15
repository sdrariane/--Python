import time

# Em milissegundos
quantumTime = 0.1

################# PROCESSO DO P1 ################
exp_p1 = 0

start_p1_geral = time.time()

start_p1 = time.time()

print("\nTime Start:", start_p1, "\n") 
 
for exp_p1 in range(100000):
  var_p1 = 2*2
  start_p1 = start_p1 + quantumTime
  tempoagora_p1 = time.time()
  if start_p1 >= tempoagora_p1:
    if(exp_p1 == 100000):
      print("TEMPO P1 EXPIRADO")
      break
    else:
      continue
  else: 
    exp_p1 = exp_p1+1

end_p1 = time.time()

################# PROCESSO DO P2 ################
exp_p2 = 0

start_p2_geral = time.time()

start_p2 = time.time()

for exp_p2 in range(100000):
  var_p2 = 3*3
  start_p2 = start_p2 + quantumTime
  tempoagora_p2 = time.time()
  if start_p2 >= tempoagora_p2:
    if(exp_p2 == 100000):
      print("TEMPO P1 EXPIRADO")
      break
    else:
      continue
  else: 
    exp_p2 = exp_p2+1
		
end_p2 = time.time()

################# PROCESSO DO P3 ################
exp_p3 = 0

start_p3_geral = time.time()

start_p3 = time.time()

for exp_p3 in range(100000):
  var_p3 = 5*5
  start_p3 = start_p3 + quantumTime
  tempoagora_p3 = time.time()
  if start_p3 >= tempoagora_p3:
    if(exp_p3 == 100000):
      print("TEMPO P1 EXPIRADO")
      break
    else:
      continue
  else: 
    exp_p3 = exp_p3+1
		
end_p3 = time.time()

###############################################

print("O Processo 1 parou no expoente:", (exp_p1+1), "\n")
print("O Processo 2 parou no expoente:", (exp_p2+1), "\n")
print("O Processo 3 parou no expoente:", (exp_p3+1), "\n")
print("Quanto o P1 Demorou", (end_p1-start_p1_geral), "\n")
print("Quanto o P2 Demorou", (end_p2-start_p2_geral), "\n")
print("Quanto o P3 Demorou", (end_p3-start_p3_geral), "\n")

###############################################