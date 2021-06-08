"""pyeuclid unit tests"""
import math
import euclid as eu


def test_200_quaternion():
    """
    Exercise Quaternion class.
    """

    q1 = eu.Quaternion(1,2,3,4).normalize()
    q2 = eu.Quaternion.new_rotate_axis(*q1.get_angle_axis()).normalize()

    #
    # check get_angle_axis(), new_rotate_axis(), normalize()
    #
    assert ((q1.conjugated()*q2).normalized()).w == 1.0

    #
    # check interpolation of equal quaternions
    #
    q3 = eu.Quaternion.new_interpolate(q1, q2, 0.5)

    #
    # check interpolation of non-normalized quaternions
    #
    q4 = eu.Quaternion(4,3,2,1)
    # rotation angle from q1 to normalized q4
    full_angle, _ = (q4.normalized()*q1.conjugated()).get_angle_axis()
    # check a few interpolations
    alphas = [0.0, 0.5, 1.0]
    for alpha in alphas:
        # rotation angle from q1 to interpolate
        interp_angle, _ = (eu.Quaternion.new_interpolate(q1, q4, alpha)
                           * q1.conjugated()).get_angle_axis()
        assert interp_angle - alpha*full_angle < 1e-6
