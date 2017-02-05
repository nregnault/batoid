import math
import jtrace


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def test_DotProduct():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        x2 = random.gauss(mu=0.13, sigma=3.3)
        y2 = random.gauss(mu=-0.5, sigma=1.21)
        z2 = random.gauss(mu=1.34, sigma=3.01)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = jtrace.Vec3(x2, y2, z2)

        assert isclose(jtrace.DotProduct(vec1, vec2),
                       x1*x2 + y1*y2 + z1*z2)
        assert isclose(jtrace.DotProduct(vec1, vec2),
                       vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z)


def test_CrossProduct():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        x2 = random.gauss(mu=0.13, sigma=3.3)
        y2 = random.gauss(mu=-0.5, sigma=1.21)
        z2 = random.gauss(mu=1.34, sigma=3.01)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = jtrace.Vec3(x2, y2, z2)

        # Cross product is orthogonal to input vectors
        assert isclose(
                jtrace.DotProduct(jtrace.CrossProduct(vec1, vec2), vec1),
                0.0,
                abs_tol=1e-12)
        assert isclose(
                jtrace.DotProduct(jtrace.CrossProduct(vec1, vec2), vec2),
                0.0,
                abs_tol=1e-12)

        # Auto cross product is "zero"
        assert isclose(
                jtrace.CrossProduct(vec1, vec1).Magnitude(), 0.0,
                abs_tol=1e-12)

        # Magnitude of cross product of orthogonal vectors is product of magnitudes
        vec3 = jtrace.CrossProduct(vec1, vec2)
        assert isclose(
                jtrace.CrossProduct(vec1, vec3).Magnitude(),
                vec1.Magnitude() * vec3.Magnitude())
        assert isclose(
                jtrace.CrossProduct(vec2, vec3).Magnitude(),
                vec2.Magnitude() * vec3.Magnitude())


def test_Magnitude():
    import random
    for i in range(100):
        x = random.gauss(mu=0.1, sigma=0.3)
        y = random.gauss(mu=-0.3, sigma=1.1)
        z = random.gauss(mu=10.34, sigma=13.0)

        vec = jtrace.Vec3(x, y, z)
        assert isclose(vec.Magnitude(), math.sqrt(x*x + y*y + z*z))
        assert isclose(vec.MagnitudeSquared(), x*x + y*y + z*z)
        assert isclose(vec.UnitVec3().Magnitude(), 1.0)


def test_add():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        x2 = random.gauss(mu=0.13, sigma=3.3)
        y2 = random.gauss(mu=-0.5, sigma=1.21)
        z2 = random.gauss(mu=1.34, sigma=3.01)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = jtrace.Vec3(x2, y2, z2)

        vec3 = vec1 + vec2
        assert isclose(vec1.x+vec2.x, vec3.x)
        assert isclose(vec1.y+vec2.y, vec3.y)
        assert isclose(vec1.z+vec2.z, vec3.z)

        vec1 += vec2
        assert isclose(x1+x2, vec1.x)
        assert isclose(y1+y2, vec1.y)
        assert isclose(z1+z2, vec1.z)


def test_sub():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        x2 = random.gauss(mu=0.13, sigma=3.3)
        y2 = random.gauss(mu=-0.5, sigma=1.21)
        z2 = random.gauss(mu=1.34, sigma=3.01)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = jtrace.Vec3(x2, y2, z2)

        vec3 = vec1 - vec2
        assert isclose(vec1.x-vec2.x, vec3.x)
        assert isclose(vec1.y-vec2.y, vec3.y)
        assert isclose(vec1.z-vec2.z, vec3.z)

        vec1 -= vec2
        assert isclose(x1-x2, vec1.x)
        assert isclose(y1-y2, vec1.y)
        assert isclose(z1-z2, vec1.z)


def test_mul():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        m = random.gauss(mu=2.3, sigma=0.31)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = vec1 * m
        assert isclose(vec1.x*m, vec2.x, rel_tol=1e-7)
        assert isclose(vec1.y*m, vec2.y, rel_tol=1e-7)
        assert isclose(vec1.z*m, vec2.z, rel_tol=1e-7)

        vec1 *= m
        assert isclose(x1*m, vec1.x, rel_tol=1e-7)
        assert isclose(y1*m, vec1.y, rel_tol=1e-7)
        assert isclose(z1*m, vec1.z, rel_tol=1e-7)


def test_div():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        m = random.gauss(mu=2.3, sigma=0.31)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = vec1/m
        assert isclose(vec1.x/m, vec2.x, rel_tol=1e-7)
        assert isclose(vec1.y/m, vec2.y, rel_tol=1e-7)
        assert isclose(vec1.z/m, vec2.z, rel_tol=1e-7)

        vec1 /= m
        assert isclose(x1/m, vec1.x, rel_tol=1e-7)
        assert isclose(y1/m, vec1.y, rel_tol=1e-7)
        assert isclose(z1/m, vec1.z, rel_tol=1e-7)


def test_eq():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = jtrace.Vec3(x1, y1, z1)

        assert vec1 == vec2


def test_ne():
    import random
    for i in range(100):
        x1 = random.gauss(mu=0.1, sigma=0.3)
        y1 = random.gauss(mu=-0.3, sigma=1.1)
        z1 = random.gauss(mu=10.34, sigma=13.0)

        vec1 = jtrace.Vec3(x1, y1, z1)
        vec2 = jtrace.Vec3(x1+1e-12, y1, z1)
        vec3 = jtrace.Vec3(x1, y1+1e-12, z1)
        vec4 = jtrace.Vec3(x1, y1, z1+1e-12)

        assert vec1 != vec2
        assert vec1 != vec3
        assert vec1 != vec4