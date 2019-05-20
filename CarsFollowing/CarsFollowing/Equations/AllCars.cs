using System;

namespace CarsFollowing.Equations
{
    class AllCars : IEquations
    {
        private float _d;
        private float _lamda;

        public AllCars(float lamda, float d)
        {
            _lamda = lamda;
            _d = d;
        }

        public float Equation(float time, float nextCarPosition, float carPosition)
        {
            return _d * (nextCarPosition - carPosition - _lamda);
        }
    }
}
