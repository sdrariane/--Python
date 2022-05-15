<h1>📑 Introdução</h1>

<p>
Em sistemas operacionais UNIX (uniprogramáveis), quando um processo espera a realização de qualquer operação de E/S a CPU fica livre à espera de uma ação dado que os processos são interdependentes causando a problemática do starvation (um problema decorrente do cenário em que os processos de alta prioridade continuam em execução enquanto os demais processos são bloqueados por tempo indefinido). Porém, em sistemas multiprogramáveis, a CPU não fica ociosa durante o tempo de espera de qualquer operação E/S e passa a executar outros processos, e vice-versa. Dessa forma, fica a encargo do Sistema Operacional vigente definir qual processo a CPU receberá, escalonando os processos conforme sua prioridade.
</p>
<p>
Esta manobra tem como intuito maximizar a utilização da CPU (mantendo-a ocupada), além de alocar de forma justa seu processamento visando a transferência máxima dentro de um tempo mínimo de execução (Burst Time), assim como o de espera (Waiting Time) e de resposta (Turn Around Time). Além desses parâmetros, tem-se o responsável pelo monitoramento da duração de cada processo (Arrival Time) em unidade quantum ou milissegundos, e o opcional do cronômetro que cada processo, em geral, leva para finalizar.
</p>
<p>
Outo conceito presente no escalonamento de CPU’s seria a preemptividade caracterizado pelo momento de mudança de estado de um processo, seja ele do estado de execução para finalizado ou de espera para finalizado. Os recursos são alocados ao processo por um período limitado de tempo e, em seguida, retirados, sendo ele colocado novamente na fila de finalizados à espera de uma nova chance de execução. Em escalonamentos não preemptivos, o processo termina ou muda do estado de execução para o de espera, sendo os recursos alocados a um processo eu retém a CPU até que ela seja finalizada ou atinja o estado de espera – porém se interromper um processo em execução na CPU durante a execução, esperando a finalização do processo dentro do Burst Time.
</p>
<p>
Existem diversos algoritmos utilizados com o intuito de estimar o tempo necessário para alocar processos e threads, relembrando que o objetivo principal é manter a CPU o mais ocupada possível visando maximizar o processamento.
</p>
<p>
Quanto ao algoritmo de Robin Round, para cada processo é atribuído um tempo fixo (Time Quantum) a ser executado de forma cíclica, sendo projetado para o sistema de time-sharing. A fila pronta é tratada como uma fila circular (prevenindo starvation) do tipo FIFO e o escalonador percorre a fila, alocando a CPU para cada processo por um intervalo de tempo de até 1 quantum (ou 1 milissegundo) dando prioridade de fora uniforme a todos os processos, configurando um temporizador para interromper após 1 vez o quantum despachando-o. No caso de o processo ter um pico de CPU menor que 1, o próprio processo liberará a CPU voluntariamente, e o escalonador então prosseguirá para o próximo processo na fila de prontos. Caso contrário, se o pico de CPU do processo em execução no momento for maior que 1 vez o quantum, o cronômetro será desativado e causará uma interrupção no sistema operacional. Uma troca de contexto será executada e o processo será colocado no final da fila de prontos, por fim, o escalonador selecionará o próximo processo na fila de prontos.
</p>
<p>
Aprofundando-se no conceito de Quantum Time tendo como base a mecânica quântica, o tempo é entendido como um conceito externo (“clássico”). Assim, supõe-se, como na física clássica, que existe como um controlador de todo movimento – seja como tempo absoluto ou na forma de tempos próprios definidos por uma métrica clássica de espaço-tempo. No último caso, é aplicável a sistemas quânticos locais ao longo de suas linhas de mundo. De acordo com essa suposição, o tempo pode ser lido a partir de ‘relógios’ clássicos ou quase clássicos apropriados.
</p>

> "A ‘quantização do tempo’ assim alcançada não leva necessariamente a uma ***discretização*** (processo que divide algo em partes menores e menos complexas) do tempo – assim como  a quantização do movimento livre não requer uma discretização do espaço. [...] Uma quantização formal (canônica) do tempo também seria necessária em teorias dinâmicas não-relativistas machianas ('relacionais') – como a computação -, que consistentemente substituem o conceito de tempo por algum movimento de referência."

<p>
***Time in Quantum Theory***. Compendium of Quantum Physics.
</p>

<h1>📓 Código</h1>

<p>
Tudo começa com a importação de uma biblioteca do python `time` que provê várias funções relacionadas à tempo, sendo uma delas a captura do tempo epoch. O início dos tempos começa a ser medido a partir de 1º de janeiro, 12:00 am, 1970 e este mesmo horário é denominado como epoch em Python, cuja função `time()` a calcula a partir desta data até o exato momento em que é chamada.
</p>

    # o tempo geral que não irá ser modificado ao longo da execução do script
	start_p1_geral = time.time()
    
	#  tempo que irá ser modificado ao longo da execução do script
    start_p1 = time.time()
	
	# Time Start: 1651767653.4534123
	print("\nTime Start:", start_p1, "\n") 
	
<p>
Estabelecendo um loop for que vai de zero até 100.000 contabilizando o expoente atual como parâmetro.
</p>

    for exp_p1 in range(100000):
      
	  # estabelecimento do processo que deve ser repetido de acordo com o expoente atual dentro do loop
      var_p1 = 2*2
      
	  # adição do grupo quantum a ser analisado iniciando-se em 1 milissegundo (ou 0,001 s)
      start_p1 = start_p1 + quantumTime
  	
	# estabelecendo um comparativo com o tempo aual discorrido do processo e adição do tempo quantum
      tempoagora_p1 = time.time()
      
	  # se o tempo calculado antes do início do loop for maior que o calculado agora pouco...
      if start_p1 >= tempoagora_p1:
        
		#  o script deve analisar se o expoente é maior ou igual a 100.000
        if(exp_p1 == 100000):
		
		# se ele for o nosso objetivo de rodar a mesma operção 100.000 vezes de 1 em 1 está completa
          print("TEMPO P1 EXPIRADO")
          break
		  
		  # caso contrário ele continua a processa a partir do próximo laço subsequente - ao mesmo tempo que o segundo e quarto processos (3 e 5) rodam, sendo cada um contabilizado de forma individual
        else:
          continue
      
      else: 
	  # se o tempo calculado antes do início do loop NÃO for maior que o calculado agora pouco acrescenta-se ao laço e parte para a próxima
        exp_p1 = exp_p1+1
    
	# captura do tempo final para subtração do inicial geral e assim estabelcer o delta
    end_p1 = time.time()
	
<p>
Ao final com intuito de análise informa-se em qual laço o processo parou - neste código ele irá obrigatoriamente chegar até 100.000 - e o tempo discorrido entre o inicio e o final
</p>

    print("The process 1 has stopped at:", (exp_p1+1), "\n")
    print("The process take: ", (end_p1-start_p1_geral), "\n")

<h1>📄 Bibliografia</h1>
<p>
**01.**	NEEKHARA, Aman. Difference between Deadlock and Starvation in OS. Geeks for Geeks, 30 de setembro de 2019. Disponível em: <https://www.geeksforgeeks.org/difference-between-deadlock-and-starvation-in-os/>. Acessado em: 28 de abril de 2022.</p>
<p>**02.**	CPU Scheduling. Java T Point. Disponível em: <https://www.javatpoint.com/os-cpu-scheduling>. Acessado em: 28 de abril de 2022.</p>
<p>**03.**	BISHT, Ankit. Preemptive and Non-Preemptive Scheduling. Geeks for Geeks, 25 de agosto de 2021. Disponível em: <https://www.geeksforgeeks.org/preemptive-and-non-preemptive-scheduling/>. Acessado em: 28 de abril de 2022.</p>
<p>**04.**	ZEH, Dieter. Time in Quantum Theory. In: Greenberger, D., Hentschel, K., Weinert, F. (eds) Compendium of Quantum Physics. Springer, Berlin, Heidelberg, 2009. https://doi.org/10.1007/978-3-540-70626-7_221</p>
<p>**05.**	Difference between Arrival Time and Burst Time in CPU Scheduling. Geeks for Geeks, 10 de maio de 2020. Disponível em: <https://www.geeksforgeeks.org/difference-between-arrival-time-and-burst-time-in-cpu-scheduling/#:~:text=Burst%20Time%20(BT)%20%3A,running%20time%20of%20the%20process>. Acessado em: 28 de abril de 2022.</p>
<p>**06.**	Comparison of Different CPU Scheduling Algorithms in OS. Geeks for Geeks, 30 de novembro de 2021. Disponível em: < https://www.geeksforgeeks.org/comparison-of-different-cpu-scheduling-algorithms-in-os/ >. Acessado em: 28 de abril de 2022.</p>
<p>**07.**	CPU Scheduling in Operating Systems. Geeks for Geeks, 28 de junho de 2021. Disponível em: < https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/ >. Acessado em: 28 de abril de 2022.</p>
<p>**08.**	Types of Operating Systems. Geeks for Geeks, 21 de setembro de 2021. Disponível em: < https://www.geeksforgeeks.org/types-of-operating-systems/ >. Acessado em: 28 de abril de 2022.</p>
<p>**09.**	Introduction to UNIX System. Geeks for Geeks, 22 de janeiro de 2021. Disponível em: < https://www.geeksforgeeks.org/introduction-to-unix-system/ >. Acessado em: 28 de abril de 2022.</p>
<p>**10.**	Process Schedulers in Operating Systems. Geeks for Geeks, 21 de junho de 2021. Disponível em: < https://www.geeksforgeeks.org/process-schedulers-in-operating-system/ >. Acessado em: 28 de abril de 2022.</p>
<p>**11.**	Difference between Turn Around Time (TAT) and Wiaiting Time (WT) in CPU Scheduling. Geeks for Geeks, 28 de março de 2020. Disponível em: < https://www.geeksforgeeks.org/difference-between-turn-around-time-tat-and-waiting-time-wt-in-cpu-scheduling/ >. Acessado em: 28 de abril de 2022.
</p>