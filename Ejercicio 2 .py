import argparse


if __name__ == '__main__':
	parser= argparse.ArgumentParser('valor')
	parser.add_argument('Nombre')

args = parser.parse_args()

datos = {
	'Nombre': {
	    'edad': 21,
	    'direccion': 'Nicaragua' 
	    }
	}

if args.Nombre in datos:
	print 'La llave {Nombre} existe'.format(Nombre=args.Nombre)	
else:
	print 'La llave {Nombre} no existe'.format(Nombre=args.Nombre)	

	