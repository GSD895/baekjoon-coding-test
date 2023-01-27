
for(int i=0; i<3; i++){
   for(int j=0; j<3; j++){
      System.out.println("i="+i + " j="+j);
      if (j==1){
         break Loop1;     // end of Loop1(i)
         //break;         // end of Loop2(j)
         //break Loop2;   // end of Loop2(j)
      }
   }
}