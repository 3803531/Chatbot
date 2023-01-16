import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;  
 
public class Test
{   
    static void modifyFile(String filePath, String oldString, String newString)
    {
        File fileToBeModified = new File(filePath);
         
        String oldContent = "";
         
        BufferedReader reader = null;
         
        FileWriter writer = null;
         
        try
        {
            reader = new BufferedReader(new FileReader(fileToBeModified));
             
            //Reading all the lines of input text file into oldContent
             
            String line = reader.readLine();
             
            while (line != null) 
            {
                oldContent = oldContent + line + System.lineSeparator();
                 
                line = reader.readLine();
            }
             
            //Replacing oldString with newString in the oldContent
             
            String newContent = oldContent.replaceAll(oldString, newString);
             
            //Rewriting the input text file with newContent
             
            writer = new FileWriter(fileToBeModified);
             
            writer.write(newContent);
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        finally
        {
            try
            {
                //Closing the resources
                 
                reader.close();
                 
                writer.close();
            } 
            catch (IOException e) 
            {
                e.printStackTrace();
            }
        }
    }


    public static void main(String[] args)
    {
        BufferedReader reader;

		try {
			reader = new BufferedReader(new FileReader("VALEURS.txt"));
			String line = reader.readLine();
            String Reponse = "";
            String Ancienne_question = "";
            Integer rep = 0;

            System.out.println("Chat GPT a repondu: ");
            

			while (line != null) {
				//System.out.println(line);
				// read next line

                if (line.equals("#")){
                    rep = 1;
                }

                if (rep == 1) {
                Reponse = Reponse + line;
                }
                else {
                    Ancienne_question = Ancienne_question + line;
                }

                line = reader.readLine();
			}

            System.out.println(Reponse);

			reader.close();

            Scanner sc= new Scanner(System.in); //System.in is a standard input stream  
            
            System.out.println("Répond a chat GPT: ");

            String Question= sc.nextLine();              //reads string  
            //System.out.println(Question);
            //System.out.println(Ancienne_question);
            modifyFile("C:/Users/enzos/Desktop/Master/PFE/VALEURS.txt",Ancienne_question,Question); // Ne pas oublier de mettre le nouveau PATH !!!
         
            
		} catch (IOException e) {
			e.printStackTrace();
		}

    }
}