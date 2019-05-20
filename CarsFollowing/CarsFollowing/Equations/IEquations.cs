namespace CarsFollowing.Equations
{
    interface IEquations
    {
        float Equation(float time,float nextCarPosition, float carPosition);
    }
}
