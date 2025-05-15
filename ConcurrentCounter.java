public class ConcurrentCounter {
	
	// Programacion concurrente
	public static void main(String[] args) {
		
		// Concurrencia diferente a Paralelismo
		
		// Solo trabajaremos concurrencia
		
		// Concurrencia es como un paralelismo simulado, maneja turnos para los distintos procesos (intercalamiento)
		
		// Conceptos:
		// Proceso: Instancia de 1 programa en ejecucion
		
		// Dentro de un proceso los hilos funcionan de forma colaborativa, los hilos deben compartir informacion
		
		// Hilo: Unidad minima de ejecucion
		
		// Problemas:
		
		//Seccion critica: Codigo que accede al recurso compartido
		
		// a) Condiciones de carrera
		// b) Deadlocks (bloqueos): Bloqueos permanentes
		// c) Livelocks: Tipo de bloqueo pero un poco menos drastico
		// d) Startuation
		
		Counter myCounter = new Counter();
		Thread hilo1 = new Thread( () -> { // Metodo para crear hilos
			
			// Este hilo va a llamar la funcion incrementar de Counter, 10 veces:
			for(int i=0; i<10; i++)
			{
				myCounter.increment();
				System.out.println("Hilo actual: "+Thread.currentThread().getId()+"Valor del contador: "+myCounter.getValue());
			}
		} );
		
		Thread hilo2 = new Thread( () -> {
			for(int i=0; i<10; i++)
			{
				myCounter.decrement();
				System.out.println("Hilo actual: "+Thread.currentThread().getId()+" Valor del contador: "+myCounter.getValue());
			}
		} );
		
		// Inicia la ejecucion de los hilos:
		hilo1.start();
		hilo2.start();
		
		// Este hilo principal va a esperar que hilo1 e hilo2 terminen su ejecucion (ponerlos en un try-catch)
		try {
			hilo1.join();
			hilo2.join();
		}
		catch(InterruptedException ex)
		{
			
		}
		
		// Imprimir valor final del contador:
		System.out.println("\nValor final del contador:"+myCounter.getValue());
	}
}