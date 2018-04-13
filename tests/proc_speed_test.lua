--
-- Ez nem saját, köszönet tbs-nek a hup.hu-n
-- Forrás: https://hup.hu/node/158678#comment-2215500
--
require 'lfs'

sDir = '/proc'

ctr, err = 0, 0

for i = 0, 10000, 1 do

for sFileName in lfs.dir( sDir ) do
	if string.match( sFileName, '^[0-9]*$' ) then
		local fStatFile = io.open( sDir ..'/'.. sFileName ..'/stat', 'r' )
		if fStatFile then
			local sLine = fStatFile:read()
			if sLine then
					ctr = ctr +1
				else
					err = err +1
				end
			fStatFile:close()
			end
		end
	end

end

print( "Count:", ctr )
print( "Error:", err )
