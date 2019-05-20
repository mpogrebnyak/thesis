using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CarsFollowing.Equations;

namespace CarsFollowing
{
    class RungeKutta
    {
        const float H = 0.01F;
        IEquations _equation;

        public RungeKutta(IEquations equation)
        {
            _equation = equation;
        }

        public float RungeKutta4(float startPoint)
        {
            // float k1, k2, k3, k4;

            // PointF solution = startPoint;
            //Equations equations = new Equations();

            // k1 = H * _equation.Equation(solution.X, solution.Y);


            // k2 = H * _equations.FunctionU(solution.X + k1 / 2, solution.Y + l1 / 2);
            //  l2 = H * _equations.FunctionV(solution.X + k1 / 2, solution.Y + l1 / 2);

            //  k3 = H * _equations.FunctionU(solution.X + k2 / 2, solution.Y + l2 / 2);
            //   l3 = H * _equations.FunctionV(solution.X + k2 / 2, solution.Y + l2 / 2);

            //  k4 = H * _equations.FunctionU(solution.X + k3, solution.Y + l3);
//                l4 = H * _equations.FunctionV(solution.X + k3, solution.Y + l3);

            //   float u = solution.X + (k1 + 2 * k2 + 2 * k3 + k4) / 6;
            //     float v = solution.Y + (l1 + 2 * l2 + 2 * l3 + l4) / 6;


            return 0;
        }
    }
}
