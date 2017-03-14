class ArrInsertion
{
int arr[];
int nElem;


public ArrInsertion(int N)
{
arr=new int[N];
nElem=0;
}

public void insert(int value)
{
arr[nElem]=value;
nElem+=1;
}

public void display()
{
for(int i=0;i<nElem;i++)
{
System.out.print(" "+arr[i]);
}
System.out.println();
}

public void insSort()
{
int outer,inner,temp;
for(outer=1;outer<nElem;outer++)
{
temp=arr[outer];
inner=outer;
while(inner>0 && arr[inner-1]>=temp)
{
arr[inner]=arr[inner-1];
--inner;
}
arr[inner]=temp;
}
}



}

public class ArrInsertionApp
{
public static void main(String[] args)
{
ArrInsertion ab=new ArrInsertion(11);
ab.insert(22);
ab.insert(33);
ab.insert(11);
ab.insert(66);
ab.insert(0);
ab.insert(24);
ab.insert(67);
ab.insert(99);
ab.insert(12);
ab.insert(44);

ab.display();
ab.insSort();
ab.display();
}
}