# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_19:01:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 19:01:14 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-07 19:01:14 | Kuda Oya (Kirindi Oya) | 3.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-07 19:00:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.090 |  |
| 2026-05-07 19:00:36 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.118 |  |
| 2026-05-07 19:00:18 | Wellawaya (Kirindi Oya) | 3.18 | 🟢 Normal | 0.970 | 🔺 Rising |
| 2026-05-07 18:20:17 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:10:01 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-07 18:08:59 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-05-07 18:08:33 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:08:28 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.084 |  |
| 2026-05-07 18:07:54 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 18:06:56 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 648.000 | 🔺 Rising |
| 2026-05-07 19:00:18 | Wellawaya (Kirindi Oya) | 3.18 | 🟢 Normal | 0.970 | 🔺 Rising |
| 2026-05-07 18:07:31 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | 0.619 | 🔺 Rising |
| 2026-05-07 18:08:59 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-05-07 18:03:17 | Norwood (Kelani Ganga) | 1.48 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-07 18:02:12 | Peradeniya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-07 18:10:01 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-07 18:01:15 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-07 19:01:14 | Kuda Oya (Kirindi Oya) | 3.90 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-07 18:01:19 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 18:03:53 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 18:02:44 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 19:01:14 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:03:27 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:05:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:05:17 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:43 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:29 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:59 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:05:51 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:20:17 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-07 18:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-05-07 18:01:54 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-07 18:03:24 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.011 |  |
| 2026-05-07 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.020 |  |
| 2026-05-07 18:02:19 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.021 |  |
| 2026-05-07 18:06:04 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.028 |  |
| 2026-05-07 18:02:13 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.029 |  |
| 2026-05-07 18:03:31 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.029 |  |
| 2026-05-07 18:07:54 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-07 18:06:52 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.031 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-07 18:03:28 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | -0.071 |  |
| 2026-05-07 18:08:28 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.084 |  |
| 2026-05-07 19:00:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.090 |  |
| 2026-05-07 18:01:35 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.097 |  |
| 2026-05-07 19:00:36 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | -0.118 |  |
| 2026-05-07 18:02:26 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)