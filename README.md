# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--27_07:22:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **190,543 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 07:22:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-27 07:16:41 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-27 07:16:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:12:52 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 07:12:31 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:12:21 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:12:14 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:11:34 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:09:36 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 07:08:10 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.088 |  |
| 2026-06-27 07:07:28 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:07:12 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:07:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:06:15 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.004 |  |
| 2026-06-27 07:06:10 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 07:05:53 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 07:05:46 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:05:45 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | -0.071 |  |
| 2026-06-27 07:05:31 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:05:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 07:04:16 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.096 |  |
| 2026-06-27 07:03:54 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 07:03:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:03:40 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:03:30 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:03:18 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:03:12 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-06-27 07:02:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:02:01 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-06-27 07:01:54 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:01:51 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-06-27 07:01:36 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:01:30 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-06-27 07:01:24 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 07:01:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:01:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:01:06 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-27 07:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-06-27 07:01:51 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-06-27 06:09:05 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-27 07:06:10 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 07:03:54 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-27 07:16:41 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-27 07:22:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-27 07:05:53 | Ellagawa (Kalu Ganga) | 5.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-27 07:01:24 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 07:09:36 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-27 07:05:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 07:12:52 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-27 07:01:06 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:01:54 | Moragaswewa (Deduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:02:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:01:36 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:12:31 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:03:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:11:34 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:12:14 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:07:12 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:07:28 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:03:12 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:16:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:05:46 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:12:21 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:07:08 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:01:09 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-06-27 07:03:18 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-27 06:01:46 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.002 |  |
| 2026-06-27 07:06:15 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | -0.004 |  |
| 2026-06-27 07:03:30 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:03:40 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:01:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-27 07:01:30 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-06-27 07:02:01 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.022 |  |
| 2026-06-27 07:05:45 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | -0.071 |  |
| 2026-06-27 07:08:10 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.088 |  |
| 2026-06-27 07:04:16 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)