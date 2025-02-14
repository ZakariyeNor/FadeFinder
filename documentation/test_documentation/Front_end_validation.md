# HTML Validator Results

## base.html

**Error**:  
Element `li` not allowed as a child of element `div` in this context.  
From line 122, column 25; to line 122, column 28

**Solution**:  
Created `li` items inside the `ul`.

**Result**:  
No errors or warnings to show.

---

## home.html

**Error**:  
Bad value for attribute `src` on element `img`: Must be non-empty.  
From line 111, column 29; to line 111, column 87

**Solution**:  
Added the path that Django created when the user uploaded the image from the backend (`/media/barbers/barber1.jpg`).

**Result**:  
No errors or warnings to show.

---

## book.html

**Error**:  
Attribute `today` not allowed on element `input` at this point.  
From line 145, column 67; to line 145, column 169

**Solution**:  
Removed the `today` attribute and updated the input field to use the following:  
`<input type="date" name="date" value="{{ booking.date|date:"Y-m-d" }}" class="dateinput form-control" required id="id_date">`

**Result**:  
No errors or warnings to show.

---

## edit_booking.html

**Error**:  
0 errors.

**Solution**:  
No errors found.

**Result**:  
No errors or warnings to show.

---

## about.html

**Error**:  
0 errors.

**Solution**:  
No errors found.

**Result**:  
No errors or warnings to show.

---

# CSS Validator Results
## style.css

**Error**:  
0 errors.

**Solution**:  
No errors found.

**Result**:  
No errors found.

---

## booking.css

**Error**:  
0 errors.

**Solution**:  
No errors found.

**Result**:  
No errors found.

---

# Javascript Validator Results

## script.js, maps.js and edit.js (Using JSHint)

**Warnings**:  
Warnings related to ES6 features like `let`, `const`, arrow functions, and template literals.
script.js (19)
maps.js (10)
edit.js (8)

**Solution**:  
Added the configuration for ES6:  
```json
{ "esversion": 6 }
