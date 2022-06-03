
public class Generate {
	public void generate(String p_name, String a_name) {
		Runtime rt = Runtime.getRuntime();
		
		//String p_name= "taskmate";
		//String a_name= "todoapp";
		try
        { 
            rt.exec("cmd /c start cmd.exe /K "
            		+ "\"django2\\Scripts\\activate && cd output && django-admin startproject " 
            		+ p_name + " && cd " + p_name + " &&  python manage.py startapp " + a_name + " && cd ..\\..\\helper && python main.py "
            		+ p_name + " " + a_name		+ "           && chdir && mysql -u root -p\"");	  
        } 
        catch (Exception ess) 
        { 
            ess.printStackTrace(); 
        }
	}
}
