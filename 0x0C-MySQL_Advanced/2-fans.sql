-- metal_bands
-- metal_bands
SELECT origin,sum(fans) as nb_fans from metal_bands Group by origin order by nb_fans DESC;
