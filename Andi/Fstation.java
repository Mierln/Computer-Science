import java.util.Scanner;

public class Fstation {
    public static void main(String[] args) {
        String[] Fire_Stations = {"ALPHA", "BETA", "THETA", "CENTER", "RAILWAY", "HARBOR", "SUBURB"};
        int[] Personnel = {12, 13, 23, 44, 23, 11, 43};

//Main function
        int min = Personnel[0];
        int b = 0;
        String understaffed = Fire_Stations[0];
        String input;
        int[] info = {0,0,0,0,0,0,0};
        int a = 0;
        {
            while (b < 52) {
                Scanner obj = new Scanner(System.in);
                System.out.println("(T)rue / (F)alse: ");
                input = obj.nextLine();


                if (input.equals("T")) {
                    while (a < 7) {
                        //Calculate method
                        if (Personnel[a]<25) {
                            info[a] = 25-Personnel[a];}
                        else{
                            info[a] = 0;}
                                if (min > Personnel[a]) {
                                    min = Personnel[a];
                                    understaffed = Fire_Stations[a];
                                    System.out.println("");
                                    System.out.println("====Station " + understaffed + " is understaffed====");

                                    System.out.println("");
                                } else {
                                    System.out.println("Station " + Fire_Stations[a]);
                                    System.out.println(Fire_Stations[a] + " has " + Personnel[a] + " personnels");
                                    if (info[a]>0) {
                                        System.out.println("Firestation " + Fire_Stations[a] + " lacks " + info[a] + " personnel" );
                                    System.out.println("");
                                    }
                                    else {
                                        System.out.println("");
                                    }
                                    a++;
                                }

                    }
                } else {
                    System.out.println("No station for you");
                    break;
                }
                b++;

            }

        }
    }
}