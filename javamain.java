// "static void main" must be defined in a public class.
public class Main {
    
    public static int[] stringToIntegerArray(String input)
    {
        input= input.trim();
        input= input.substring(1,input.length()-1);
        if(input.length()==0){return new int[0]}
        
        String[] parts=input.split(",");
        int[] output= new int[parts.length];//length=ge shu
        for(int index=0; index<parts.length; index++)
        {
            String part=parts[index].trim();
            output[index]=Integer.parseInt(part);
        }
        return output;
    }
    
    public static String integerArrayToString(int[] nums)
    {
        if(nums.length==0){return "[]";}
        
        String result="";
        for(int index=0; index<num.length; index++)
        {
            int number= nums[index];
            result+= Integer.toString(number)+ ",";
        }
        return "["+result.substring(0,result.length()-2)+"]";
    }
    
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
        String line;
        while((line=in.readLine())!=null)
        {
            int[] nums= stringToIntegerArray(line);
            line= in.readLine();
            int target= Integer.parseInt(line);
            
            int[] ret= new Solution().twoSum(nums,target);//Solution().function()
            
            String out= integerArrayToString(ret);
            System.out.print(out);
        }
    }
}