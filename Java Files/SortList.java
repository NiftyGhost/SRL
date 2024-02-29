package app;

import java.util.Scanner;
import java.util.Random;
import java.util.Date;
import java.util.Timer;
import java.util.Currency;
import java.util.Dictionary;

public class Controller {
    public static void main(String [] args){

        Scanner scanner = new Scanner(System.in);

        //scannerTester();
        //randomTester();
        //dateTester();

        question9();

        System.out.print("Enter 'Shoes', 'Pants', or 'Shirt': ");
        question11(scanner.next());


    }//End main

    public static void scannerTester(){

        System.out.println("---------------------------------Scanner-------------------------------");
        System.out.println("https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html");

        Scanner input = new Scanner(System.in);
        System.out.println();

    }

    public static void randomTester(){

        System.out.println("---------------------------------Randomizer-------------------------------");
        System.out.println("https://docs.oracle.com/javase/8/docs/api/java/util/Random.html");

        Random randomGen = new Random();
        System.out.printf("Random Int:\t\t\t\t %d \n", randomGen.nextInt());
        System.out.printf("Random Double:\t\t\t %f \n", randomGen.nextDouble());
        System.out.printf("Random Number 0 - 100:\t %d \n", randomGen.nextInt(100));
        System.out.println();

    }

    public static void dateTester(){

        System.out.println("---------------------------------Date-------------------------------");
        System.out.println("https://docs.oracle.com/javase/8/docs/api/java/util/Date.html");

        Date date = new Date();
        System.out.print("Today's date:\t" + date + "\n");
        System.out.println();

    }

    public static void timerTester(){

        System.out.println("---------------------------------Timer-------------------------------");
        System.out.println("https://docs.oracle.com/javase/8/docs/api/java/util/Timer.html");

        Timer timer = new Timer();
        System.out.println();

    }

    public static void currencyTester(){
        System.out.println("---------------------------------Currency-------------------------------");
        System.out.println("https://docs.oracle.com/javase/8/docs/api/java/util/Currency.html");

        System.out.println();

    }

    public static void dictionaryTester(){

        System.out.println("---------------------------------Dictionary-------------------------------");
        System.out.println("https://docs.oracle.com/javase/8/docs/api/java/util/Dictionary.html");

        System.out.println();

    }

    public static void question9(){

        for(int row = 1; row <= 10; row++){

            for(int column = 1; column <= 10; column++){

                if(row >= 5 && column < 6){
                    System.out.print("X\t");
                } else {
                    System.out.print("O\t");
                }

            }
            System.out.println();
        }

        System.out.println();

    }

    public static void question11(String purchase){

        if(purchase.equalsIgnoreCase("Shoes")){
            System.out.println("Buying Shoes");
        } else if (purchase.equalsIgnoreCase("Pants")) {
            System.out.println("Buying Pants");
        } else if (purchase.equalsIgnoreCase("Shirt")){
            System.out.println("Buying Shirt");
        }

        System.out.println();

    }

}//End Controller
