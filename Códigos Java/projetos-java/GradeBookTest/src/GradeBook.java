public class GradeBook {
    
    private String courseName; // nome do curso para esse GradeBook

    // método para configurar o nome do curso
    public void setCourseName(String name){
        courseName = name; // armazena o nome do curso
    } // fim do método setCourseName

    // método para recuperar o nome do curso
    public String getCourseName(){
        return courseName;
    } // fim do método getCourseName

    // exibe uma mensagem de boas-vindas para o usuário GradeBook
    public void displayMessage(){
        // chama getCourseName para obter o nome do
        // o curso que essa GradeBook representa
        System.out.printf("Welcome to the GradeBook for \n%s!\n", getCourseName());
    } // fim do método displayMessage

}
