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
		
		// Los metodos sincronizados dan turnos a los hilos
		
		// Si el codigo que accede al recurso compartido solo es una parte pero no una instruccion solo se sincroniza esa parte de codigo
		
		// Formas similares pueden ser los candados
		
		// Variables atomicas (Nueva palabra reservada volatil): Restringe acceso a variables
		
		// Transaccioes: Bloque de operaciones
		
		// Atomicidad
		// Cconsistencia
		// Isolation
		// Durabilidad
		
		Counter myCounter = new Counter();
		Thread hilo1 = new Thread( () -> { // Metodo para crear hilos
			
			// Este hilo va a llamar la funcion incrementar de Counter, 10 veces:
			for(int i=0; i<10; i++)
			{
				myCounter.increment1();
				System.out.println("Hilo actual: "+Thread.currentThread().getId()+" Valor del contador: "+myCounter.getValue1());
			}
		} );
		
		Thread hilo2 = new Thread( () -> {
			for(int i=0; i<10; i++)
			{
				myCounter.decrement1();
				System.out.println("Hilo actual: "+Thread.currentThread().getId()+" Valor del contador: "+myCounter.getValue1());
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
		System.out.println("\nValor final del contador: "+myCounter.getValue1());
	}
}