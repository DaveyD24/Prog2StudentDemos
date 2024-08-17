public class Patterns {
//(Patterns Book 1)

    //Sum Pattern
    /*
    <type> sum = 0;
    <for each item> {
        sum += <item>;
    }
    */

    //Output Pattern
    /*
    System.out.println("<label> + <value>");
    */

    //Read Pattern
    /*
    System.out.print("<prompt>");
    <type> <variable> = <read operation>;
    */

    //Read Pattern (if variable has already been declared)
    /*
    System.out.print("<prompt>");
    <variable> = <read operation>;
    */

    //Read Loop Pattern
    /*
    <read pattern>
    while (<value> != <end value>)
    {
        <use the value>
        <read pattern>
    }
    */

    //Array Loop Pattern
    /*
    for (int i = 0; i < <array>.length; i++)
    {
        <use the item array[i]>
    }
    */

    //Count Pattern (Without Guard)
    /*
    int count = 0;
    <for each item>
        count++;
    */

    //Count Pattern (With Guard)
    /*
    int count = 0;
    <for each item> {
        if (<guard>){
            count++
        }
    }
    */
}
