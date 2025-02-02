package mono;

import java.util.Scanner;

public class monoalpha {
	static char[] plain={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	static char[] cipher={'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'};
	public static String encrypt(String s) {
		char ch[]=new char[(s.length())];
		for(int i=0;i<s.length();i++) {
			for(int j=0;j<26;j++) {
				if(plain[j]==s.charAt(i)) {
					ch[i]=cipher[j];
					break;
				}
			}
		}
		return (new String(ch));
	}
	public static String decrypt(String s) {
		char ch[]=new char[(s.length())];
		for(int i=0;i<s.length();i++) {
			for(int j=0;j<26;j++) {
				if(cipher[j]==s.charAt(i)) {
					ch[i]=plain[j];
					break;
				}
			}
		}
		return (new String(ch));
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the string of your choice");
		String text=sc.next();
		String enc=encrypt(text);
		System.out.println("Encrypted text :"+enc);
		String dec=decrypt(enc);
		System.out.println("decrypted text :"+dec);
		
		
	}

}
