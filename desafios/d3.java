public class d3 {

	public static void main(String[] args) {
        String frase = "DOUGLAS KELCZESKI"; 
        String inverte="";
        
        for(int x=frase.length()-1;x>=0;x--){
            inverte+= frase.charAt(x);
        }
        System.out.println(inverte);
    }
}
	
