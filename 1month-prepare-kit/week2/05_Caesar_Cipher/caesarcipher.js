function caesarCipher(s, k) {               
    const atoz = 'abcdefghijklmnopqrstuvwxyz';
    let cipher='';
    cipher=s.split('').map(char => {
         const charIndex = atoz.indexOf(char.toLowerCase());
         if (charIndex === -1) {
            return char;
         }
         const shiftIndex = (charIndex + k);
         const idx = shiftIndex < atoz.length ? shiftIndex : shiftIndex % atoz.length;
         const shiftedChar = atoz.charAt(idx);
         return char === char.toLowerCase() ? shiftedChar : shiftedChar.toUpperCase();
     }).join('');
   return cipher;
 }