package exercises;

import cs_1c.FHarrayList;

class FHstack<E> 
{
   private FHarrayList<E> m_array_list = new FHarrayList<E>();
   
   public void push(E x)
   {
      m_array_list.add(x);
   }
   
   public E pop()
   {
      try
      {
         return m_array_list.remove( m_array_list.size() - 1 );
      }
      catch (IndexOutOfBoundsException e)
      {
         return null;
      }
   }
   
   E top()
   {
      try
      {
         return m_array_list.get( m_array_list.size() - 1 );
      }
      catch (IndexOutOfBoundsException e)
      {
         return null;
      }
   }
}