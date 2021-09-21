# DCColonia Tycoon :bee:

Felicidades: ¡eres el nuevo apicultor del *DCC*! Se te ha encomendado la misión de modelar el comportamiento de una colonia de abejas virtuales.

El programa debe contar con tres entidades principales: <tt>Colonia</tt>, <tt>Abeja</tt> y <tt>Jardin</tt>. Con cada ejecución, la colonia debe instanciar cierta cantidad de abejas, las que saldrán a recolectar polen a un jardín cercano, para posteriormente regresar al interior de la colonia y producir miel.

A continuación, se presentan algunos requerimientos del programa:

:honey_pot: La clase <tt>Colonia</tt> debe instanciar a las abejas, y darles la orden de comenzar a trabajar al inicio de la simulación. Además, debe implementar una forma de almacenar polen y miel. Finalmente, cada cierta cantidad de tiempo debe instanciar nuevas abejas.

:bee: Las abejas salen de la colonia por una pequeña abertura, por lo que deberás cerciorarte que solo una pueda estar saliendo o entrando al mismo tiempo.

:sunflower: El Jardín debe producir polen cada cierto tiempo, para que las abejas puedan recolectarlo y la *DCColonia* sobreviva.

Las tres clases deben heredar de <tt>Thread</tt>.

Debe implementarse el patrón *productor-consumidor* entre el jardín y las abejas, y entre las abejas y la colonia. La estructura de datos <tt>Queueu</tt>, de la librería <tt>queue</tt> será de ayuda para evitar el uso excesivo de *locks* en zonas críticas.
