[online validator](https://jsonformatter.org/xml-validator)


### VALID EXAMPLE 1: 
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Rýchlokurz geniality</title>
    <lang>sk</lang>
    <author>Ľudovít Ódor</author>
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  </book>
  <book>
    <title>Nespútaná duša</title>
    <lang>sk</lang>
    <author>Michael A. Singer</author>
    <category>self-development</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```


### VALID EXAMPLE 2
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
</bookstore>
```

### VALID EXAMPLE 3:
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title_orig>Rýchlokurz geniality</title_orig>
    <LANG>sk</LANG>
    <author-1>Ľudovít Ódor</author-1>
    <category>non-fiction</category>
    <year-released>2022</year-released>
    <price>26.00</price>
  </book>
</bookstore>
```

### INVALID EXAMPLE 1 (wrong version number):
```
<?xml version="1" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Rýchlokurz geniality</title>
    <lang>sk</lang>
    <author>Ľudovít Ódor</author>
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  </book>
  <book>
    <title>Nespútaná duša</title>
    <lang>sk</lang>
    <author>Michael A. Singer</author>
    <category>self-development</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```

### INVALID EXAMPLE 2 (missing close tags):
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Rýchlokurz geniality</title>
    <lang>sk</lang>
    <author>Ľudovít Ódor
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  </book>
  <book>
    <title>Nespútaná duša</title>
    <lang>sk</lang>
    <author>Michael A. Singer</author>
    <category>self-development</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```

### INVALID EXAMPLE 3 (wrong characters in tags & unescaped characters):
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book lang="sk">
    <title>Rýchlokurz geniality</title>
    <author>Ľudovít Ódor</author>
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  </book>
  <book lang="sk">
    <title>Nespútaná duša</title>
    <author>Michael A. Singer & Someone else</author>
    <category>self-dev'</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```

### INVALID EXAMPLE 4 (missing encoding):
```
<?xml version="1.0"?>
<bookstore>
  <book>
    <title>Rýchlokurz geniality</title>
    <lang>sk</lang>
    <author>Ľudovít Ódor</author>
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  </book>
  <book>
    <title>Nespútaná duša</title>
    <lang>sk</lang>
    <author>Michael A. Singer</author>
    <category>self-development</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```

### INVALID EXAMPLE 5 (end tag with wrong name):
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Rýchlokurz geniality</title>
    <lang>sk</lang>
    <author>Ľudovít Ódor</author>
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  </boook>
  <book>
    <title>Nespútaná duša</title>
    <lang>sk</lang>
    <author>Michael A. Singer</author>
    <category>self-development</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```

### INVALID EXAMPLE 6 (tag not closed):
```
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book>
    <title>Rýchlokurz geniality</title>
    <lang>sk</lang>
    <author>Ľudovít Ódor</author>
    <category>non-fiction</category>
    <year>2022</year>
    <price>26.00</price>
  <book>
  <book>
    <title>Nespútaná duša</title>
    <lang>sk</lang>
    <author>Michael A. Singer</author>
    <category>self-development</category>
    <year>2024</year>
    <price>14.58</price>
  </book>
</bookstore>
```