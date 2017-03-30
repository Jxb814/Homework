from ReadData import *
import Analysis
import LinearRegression

readdata()
printdata()

Analysis.avexy()
Analysis.varxy()
Analysis.corrcoefxy()

ans = LinearRegression.linear_model_main(x[0],y[0],10)

print(ans)

LinearRegression.show_linear_line(x[3],y[3])