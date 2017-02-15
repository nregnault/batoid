#include <memory>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "transformation.h"

namespace py = pybind11;

namespace jtrace {
    void pyExportTransformation(py::module &m) {
        py::class_<Transformation, std::shared_ptr<Transformation>, Surface>(m, "Transformation")
            .def(py::init<std::shared_ptr<Surface>,double,double,double>())
            .def("intersect", &Transformation::intersect)
            .def("__repr__", &Transformation::repr)
            .def_property_readonly("dr", &Transformation::getDr)
            .def_property_readonly("dx", &Transformation::getDx)
            .def_property_readonly("dy", &Transformation::getDy)
            .def_property_readonly("dz", &Transformation::getDz)
            .def_property_readonly("R", &Transformation::getR);
    }
}