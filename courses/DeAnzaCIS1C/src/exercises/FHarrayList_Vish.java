package exercises;

import java.util.*;

//generic FHarrayList class ------------------------------------
public class FHarrayList_Vish<E> implements Cloneable
{
   private static final int DEFAULT_CAPACITY = 100;
   private static final int NOT_FOUND = -1;

   private int m_size;
   private E[] m_objects;

   // constructors
   public FHarrayList_Vish()
   {
      clear();
   }

   public FHarrayList_Vish(int init_capacity)
   {
      ensureCapacity(init_capacity);
   }
   
   public void clear()
   {
      m_size = 0;
      m_objects = (E[])new Object[DEFAULT_CAPACITY];
   }
   
   public void ensureCapacity(int minCapacity)
   {
      if (m_objects != null)
      {
         if( minCapacity <= m_objects.length )
            return;
      }

      E[] src_array = m_objects;
      m_objects = (E[])new Object[minCapacity];
      if (m_size > 0)
         System.arraycopy(src_array, 0, m_objects, 0, m_size);
   }
   
   public boolean add(E x)
   {
      // low-level methods should be efficient - don't call other add() 
      if( m_objects.length == m_size )
         ensureCapacity(2*m_size + 1);
      m_objects[m_size++] = x;
      return true;
   }
   
   public void add(int index, E x)
   {
      if (index < 0 || index > m_size)
         throw new IndexOutOfBoundsException();
      
      if( m_objects.length == m_size )
         ensureCapacity(2*m_size + 1);
      
      System.arraycopy(m_objects, index, m_objects, index + 1,
         m_size - index);

      m_objects[index] = x;
      m_size++;
   }
   
   // accessors and mutators
   public E get(int index)
   {
      // can't rely on m_objects[] to throw because m_size is < m_capacity!
      if (index < 0 || index >= m_size)
         throw new IndexOutOfBoundsException();
      return m_objects[index];
   }
   
   public E set(int index, E x)
   {
      E ret_val;
      
      if (index < 0 || index >= m_size)
         throw new IndexOutOfBoundsException();
      ret_val = m_objects[index];
      m_objects[index] = x;
      return ret_val;
   }
   
   public E remove(int index)
   {
      E ret_val;
      
      if (index < 0 || index >= m_size)
         throw new IndexOutOfBoundsException();
         
      ret_val = m_objects[index];
      System.arraycopy(m_objects, index + 1, m_objects, index,
         m_size - index - 1);

      m_size--;
      return ret_val;
   }
   
   public int indexOf(Object o)
   {
      int k;
      
      if (o != null)
      {
         for(k = 0; k < m_size;  k++)
            if (o.equals(m_objects[k]) )
               return k;
      }
      else
      {
         for(k = 0; k < m_size;  k++)
            if (m_objects[k] == null )
               return k;
      }   
      return NOT_FOUND;
   }
   
   public boolean remove(Object o)
   {
      int k = indexOf(o);
      
      if (k == NOT_FOUND)
         return false;
      
      remove(k);
      return true;
   }
   
   public boolean contains(Object o)
   {
      return ( indexOf(o) != NOT_FOUND );
   }
   
   public Object clone() throws CloneNotSupportedException
   {
      FHarrayList_Vish<E> new_object = (FHarrayList_Vish<E>)super.clone();
      
      // shallow copy according to Java spec ... but not TOO shallow
      new_object.m_size = m_size;
      new_object.m_objects = (E[])new Object[m_objects.length];
      
      // this is a shallow copy - we are not duplicating/cloning objects
      System.arraycopy(m_objects, 0, new_object.m_objects, 0, m_size);
      return new_object;
   }
   
   public boolean equals(Object o)
   {
      int k;
      FHarrayList_Vish<E> that;
      
      if ( !(o instanceof FHarrayList_Vish<?>) )
         return false;
      
      that = (FHarrayList_Vish<E>)o;
      if (that.size()!= m_size)
         return false;
      
      for(k = 0; k < m_size;  k++)
         if ( ! m_objects[k].equals(that.get(k)) )
            return false;
      
      return true;
   }
   
   public int size()
   {
      return this.m_size;
   }
}
