namespace CarsFollowing.Equations
{
    class FirstCar : IEquations
    {
        private float _d;
        private float _vMax;
        private float _lamda;

        public FirstCar(float vMax, float lamda, float d)
        {
            _vMax = vMax;
            _lamda = lamda;
            _d = d;
        }

        public float Equation(float time, float nextCarPosition, float carPosition)
        {
            return _d * (_vMax * time - carPosition - _lamda);
        }
    }
}
