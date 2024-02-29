package app;

import java.util.Scanner;
import java.util.Random;
import java.util.Date;
import java.util.Timer;
import java.util.Currency;
import java.util.Dictionary;

public class SortList {
    public static void main (String [] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter a list of numbers (Separate the values using a comma only): ");
        String stringOfNum = scan.next();
        int [] listOfNum = convertListToInt(stringOfNum);

        System.out.print("Enter number you want to find: ");
        int target = scan.nextInt();

        listOfNum = sortList(listOfNum);

        for (int i = 0; i < listOfNum.length; i++)
        {
            System.out.print(listOfNum[i] + " ");
        }
    }
    
    public static int [] convertListToInt (String string) {
        String [] splitString = string.split(",");
        int [] listOfNum = new int[splitString.length];
        for (int i = 0; i < listOfNum.length; i++) {
            listOfNum[i] = Integer.parseInt(splitString[i]);
        }
        return listOfNum;
    }

    public static int [] sortList (int [] listOfNum) {
            for (int i = 0; i < listOfNum.length; i++) {
                for (int j = i + 1; j < listOfNum.length; j++) {
                    if (listOfNum[i] > listOfNum[j]) {
                        int tempVar = listOfNum[i];
                        listOfNum[i] = listOfNum[j];
                        listOfNum[j] = tempVar;
                    }
                }
            }
        return listOfNum;
    }
}
