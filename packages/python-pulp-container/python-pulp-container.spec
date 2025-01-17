%{?python_disable_dependency_generator}
%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11

# Created by pyp2rpm-3.3.3
%global pypi_name pulp-container

Name:           python-%{pypi_name}
Version:        2.20.2
Release:        1%{?dist}
Summary:        Container plugin for the Pulp Project

License:        GPLv2+
URL:            https://pulpproject.org/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-ecdsa >= 0.14
Conflicts:      python%{python3_pkgversion}-ecdsa >= 0.18.1
Requires:       python%{python3_pkgversion}-pulpcore < 3.55
Requires:       python%{python3_pkgversion}-pulpcore >= 3.49.0
Requires:       python%{python3_pkgversion}-pyjwkest >= 1.4
Conflicts:      python%{python3_pkgversion}-pyjwkest >= 1.4.3
Requires:       python%{python3_pkgversion}-pyjwt >= 2.4
Conflicts:      python%{python3_pkgversion}-pyjwt >= 2.9
Requires:       python%{python3_pkgversion}-jsonschema >= 4.4
Conflicts:      python%{python3_pkgversion}-jsonschema >= 4.22
Requires:       python%{python3_pkgversion}-setuptools

Provides:       pulpcore-plugin(container) = %{version}
Obsoletes:      python3-%{pypi_name} < %{version}-%{release}
%if 0%{?rhel} == 8
Obsoletes:      python39-%{pypi_name} < %{version}-%{release}
%endif


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pulp_container
%{python3_sitelib}/pulp_container-%{version}-py%{python3_version}.egg-info


%changelog
* Wed Jul 31 2024 Odilon Sousa <osousa@redhat.com> - 2.20.2-1
- Release python-pulp-container 2.20.2

* Thu Jul 25 2024 Odilon Sousa <osousa@redhat.com> - 2.20.1-1
- Release python-pulp-container 2.20.1

* Mon May 06 2024 Odilon Sousa <osousa@redhat.com> - 2.20.0-1
- Release python-pulp-container 2.20.0

* Wed Apr 24 2024 Odilon Sousa <osousa@redhat.com> - 2.19.3-1
- Release python-pulp-container 2.19.3

* Tue Mar 26 2024 Odilon Sousa <osousa@redhat.com> - 2.19.2-1
- Release python-pulp-container 2.19.2

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 2.16.3-2
- Remove SCL bits

* Thu Jan 04 2024 Odilon Sousa <osousa@redhat.com> - 2.16.3-1
- Release python-pulp-container 2.16.3

* Fri Nov 17 2023 Odilon Sousa <osousa@redhat.com> - 2.16.2-2
- Obsolete python39 packages for a smooth upgrade

* Tue Nov 14 2023 Odilon Sousa <osousa@redhat.com> - 2.16.2-1
- Release python-pulp-container 2.16.2

* Thu Jul 27 2023 Odilon Sousa <osousa@redhat.com> - 2.15.2-1
- Release python-pulp-container 2.15.2

* Thu Apr 27 2023 Evgeni Golov - 2.14.5-1
- Release python-pulp-container 2.14.5

* Tue Feb 14 2023 Odilon Sousa <osousa@redhat.com> - 2.14.3-2
- Bump python-ecdsa requirement

* Wed Jan 04 2023 Odilon Sousa <osousa@redhat.com> - 2.14.3-1
- Release python-pulp-container 2.14.3

* Tue Nov 01 2022 Ian Ballou <ianballou67@gmail.com> - 2.14.2-1
- Update to 2.14.2

* Fri Sep 30 2022 Odilon Sousa <osousa@redhat.com> - 2.14.0-2
- Fixing Loosen requirements for jsonschema

* Tue Sep 20 2022 Odilon Sousa 2.14.0-1
- Update to 2.14.0

* Mon Aug 22 2022 Odilon Sousa <osousa@redhat.com> - 2.10.7-1
- Release python-pulp-container 2.10.7

* Tue May 10 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.3-4
- Obsolete the old Python 3.8 package for smooth upgrade

* Fri May 06 2022 Odilon Sousa <osousa@redhat.com> - 2.10.3-3
- Rebuilding with python_disable_dependency_generator macro

* Mon May 02 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.3-2
- Build against python 3.9

* Mon May 02 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.3-1
- Release python-pulp-container 2.10.3

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 2.10.0-2
- Build against python 3.9

* Tue Feb 08 2022 Odilon Sousa <osousa@redhat.com> - 2.10.0-1
- Release python-pulp-container 2.10.0

* Tue Nov 16 2021 Odilon Sousa <osousa@redhat.com> - 2.9.0-1
- Release python-pulp-container 2.9.0

* Mon Oct 18 2021 Evgeni Golov - 2.8.1-2
- Add provides for 'pulpcore-plugin' and obsolete old name

* Mon Sep 13 2021 Evgeni Golov 2.8.1-1
- Update to 2.8.1

* Wed Sep 08 2021 Evgeni Golov 2.8.0-1
- Update to 2.8.0

* Wed Jul 28 2021 Odilon Sousa <osousa@redhat.com> - 2.7.1-1
- Release python-pulp-container 2.7.1

* Fri Jul 02 2021 Evgeni Golov - 2.7.0-1
- Release python-pulp-container 2.7.0

* Fri Jun 11 2021 Evgeni Golov 2.6.0-1
- Update to 2.6.0

* Mon May 31 2021 Evgeni Golov - 2.5.3-1
- Release python-pulp-container 2.5.3

* Wed May 05 2021 Justin Sherrill <jsherril@redhat.com> 2.5.2-2
- add patch for issue 8672

* Mon Apr 26 2021 Evgeni Golov - 2.5.2-1
- Release python-pulp-container 2.5.2

* Mon Apr 19 2021 Evgeni Golov - 2.5.1-1
- Release python-pulp-container 2.5.1

* Tue Apr 13 2021 Evgeni Golov - 2.5.0-1
- Release python-pulp-container 2.5.0

* Fri Mar 19 2021 Evgeni Golov 2.4.0-1
- Update to 2.4.0

* Mon Jan 11 2021 Evgeni Golov 2.2.0-1
- Update to 2.2.0

* Mon Sep 28 2020 Evgeni Golov 2.1.0-1
- Update to 2.1.0

* Tue Sep 08 2020 Justin Sherrill <jsherril@redhat.com> 2.0.1-1
- update to 2.0.1

* Tue Aug 25 2020 Evgeni Golov 2.0.0-1
- Update to 2.0.0

* Fri Jul 17 2020 Justin Sherrill <jsherril@redhat.com> 1.4.2-1
- upgrade to 1.4.2

* Thu Jun 04 2020 Evgeni Golov 1.4.1-1
- Update to 1.4.1

* Tue Apr 28 2020 Evgeni Golov 1.3.0-1
- Update to 1.3.0

* Wed Mar 18 2020 Samir Jha 1.2.0-1
- Update to 1.2.0

* Fri Feb 28 2020 Zach Huntington-Meath <zhunting@redhat.com> - 1.0.0-2
- Bump release to build for el8

* Fri Dec 13 2019 Evgeni Golov 1.0.0-1
- Update to 1.0.0

* Tue Nov 19 2019 Evgeni Golov - 1.0.0rc1-1
- Initial package.
