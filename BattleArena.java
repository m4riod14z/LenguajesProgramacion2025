import java.util.List;
import java.util.ArrayList;

public class BattleArena {
    // PREGUNTA 1: ¿Qué tipo de variable debe ser battleActive y por qué?
	// Para que todos los hilos sepan que la batalla terminó
	
    private volatile boolean battleActive = false;
    
    private int totalDamageDealt = 0;
    private final List<Warrior> warriors = new ArrayList<>();
    
    // PREGUNTA 2: ¿Qué monitores específicos necesitamos?
    private final Object damageLock = new Object(); // Para el daño total
    private final Object warriorsLock = new Object(); // Para la lista de guerreros
    
    public static void main(String[] args) throws InterruptedException {
        BattleArena arena = new BattleArena();
        arena.startBattle();
        Thread.sleep(8000); // Esperar 8 segundos
    }
    
    // PREGUNTA 3: ¿Debe ser sincronizado este método? ¿Por qué?
    public synchronized void startBattle() {
        battleActive = true;
        System.out.println("⚔️ ¡La batalla ha comenzado!");
        
        // Crear hilos de guerreros
        for (int i = 0; i < 4; i++) {
            Warrior warrior = new Warrior("Warrior_" + i, this);
            
            // PREGUNTA 4: Complete la sincronización para agregar guerreros
            synchronized (warriorsLock) {
                warriors.add(warrior);
                warriorsLock.notifyAll();
                System.out.println("🛡️ " + warrior.getName() + " se unió a la batalla");
            }
            
            new Thread(warrior::fight, "Fighter_" + i).start();
        }
        
        // Iniciar hilo observador
        new Thread(this::battleObserver, "Observer").start();
    }
    
    public void dealDamage(int damage, String attackerName) {
        // PREGUNTA 5: Implemente usando candado implícito para totalDamageDealt
        synchronized (damageLock) {
            totalDamageDealt += damage;
            System.out.println("💥 " + attackerName + " causó " + damage + 
                             " de daño (Total: " + totalDamageDealt + ")");
            
            // Si el daño total supera 150, terminar batalla
            if (totalDamageDealt >= 150) {
                battleActive = false;
                System.out.println("🏆 ¡Batalla terminada! Daño total: " + totalDamageDealt);
                
                // Notificar a observadores
                damageLock.notifyAll(); // Despertar hilos esperando
            }
        }
    }
    
    /**
     * Observador que usa wait/notify pattern
     */
    private void battleObserver() {
        try {
            synchronized (damageLock) {
                while (battleActive && totalDamageDealt < 150) {
                    System.out.println("👁️ Observador esperando... (Daño actual: " + totalDamageDealt + ")");
                    damageLock.wait(3000); // Esperar máximo 3 segundos
                }
            }
            System.out.println("👁️ Observador: La batalla ha terminado!");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    
    public boolean isBattleActive() {
        return battleActive; // Variable volátil
    }
    
    public int getWarriorCount() {
        synchronized (warriorsLock) {
            return warriors.size();
        }
    }
    
    public int getTotalDamage() {
        synchronized (damageLock) {
            return totalDamageDealt;
        }
    }
}

class Warrior {
    private final String name;
    private final BattleArena arena;
    private int damageDealt = 0;
    
    public Warrior(String name, BattleArena arena) {
        this.name = name;
        this.arena = arena;
    }
    
    public void fight() {
        while (arena.isBattleActive()) {
            try {
                int damage = (int)(Math.random() * 25) + 5; // 5-30 daño
                arena.dealDamage(damage, name);
                damageDealt += damage;
                
                Thread.sleep(800 + (int)(Math.random() * 1200)); // 0.8-2.0 segundos
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
        System.out.println("⚡ " + name + " terminó la batalla (Daño total: " + damageDealt + ")");
    }
    
    public String getName() {
        return name;
    }
}