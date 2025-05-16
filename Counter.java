/**
 * Esta clase representa el recurso compartido y varias formas de sincronizacion:
 * @author Mariecito
 * 
 */
public class Counter {
	
	private int value1 = 10;
	private int value2 = 50;
	
	// Crear un candado para sincronizar el acceso a la variable 2:
	private Object lock2 = new Object();
	
	//Metodos sincronizados
	public synchronized void increment1()
	{
		value1++;
	}
	
	public void decrement1()
	{
		// Instrucciones sincronizadas (para todo el objeto)
		synchronized(this)
		{
			value1--;
		}
	}
	
	public void decrement2() {
		synchronized (lock2) {
			value2--;
		}
	}
	
	public int getValue1()
	{
		return this.value1;
	}
	
	public int getValue2() {
		return this.value2;
	}
}
