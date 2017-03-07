package ocpjp.unit1;

public class VarArgsExample {

	public static int add(int... arr)
	{
		int result = 0;
		for(int i = 0; i< arr.length;i++)
		{
			result+=arr[i];
		}
		return result;
	}
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//int[] arr = new int[]{3,5,1,2,7,8};
		int result = add(new int[] {});

	}

}
