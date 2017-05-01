file_name = 'MYD04_3K.A2017118.2210.006.NRT.hdf';

lat = hdfread(file_name, 'Latitude');
lng = hdfread(file_name, 'Longitude');

wind = hdfread(file_name, 'Wind_Speed_Ncep_Ocean');
aerosol_type = hdfread(file_name, 'Aerosol_Type_Land');
aerosol_size = hdfread(file_name, 'Angstrom_Exponent_1_Ocean');

dlmwrite('lat.txt', lat)
dlmwrite('lng.txt', lng)
dlmwrite('wind.txt', wind)
dlmwrite('type.txt', aerosol_type)
dlmwrite('size.txt', aerosol_size)