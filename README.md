# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_01:04:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,637 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 01:04:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-05-09 01:04:03 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-09 01:03:46 | Moraketiya (Walawe Ganga) | 2.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-09 01:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 01:03:34 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-05-09 01:02:53 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-09 01:02:29 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-09 01:02:20 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-05-09 01:02:13 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 01:01:35 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:01:27 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.110 |  |
| 2026-05-09 01:01:21 | Kuda Oya (Kirindi Oya) | 6.69 | 🟢 Normal | -0.121 |  |
| 2026-05-09 01:01:14 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.484 |  |
| 2026-05-09 01:01:13 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 01:01:09 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:01:04 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-05-09 01:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-09 00:32:05 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-09 00:12:12 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | 0.229 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 00:05:37 | Thanamalwila (Kirindi Oya) | 6.30 | 🔴 Major Flood | 0.407 | 🔺 Rising |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-09 01:02:20 | Rathnapura (Kalu Ganga) | 3.38 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-05-09 00:12:12 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-05-09 01:02:53 | Moragaswewa (Deduru Oya) | 2.24 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-09 00:04:08 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-09 00:00:42 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-09 01:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-08 23:34:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-09 00:03:37 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-09 01:03:46 | Moraketiya (Walawe Ganga) | 2.51 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 01:02:13 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 00:05:16 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 01:01:13 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 00:05:08 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-09 01:03:42 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 00:03:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-08 23:01:55 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 00:03:06 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:01:35 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-09 00:32:05 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:01:09 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-09 01:04:03 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-09 01:02:29 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-09 00:08:05 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.019 |  |
| 2026-05-09 00:01:45 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-09 01:01:04 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-05-09 01:04:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-05-09 00:10:38 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.036 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-09 00:01:51 | Wellawaya (Kirindi Oya) | 3.00 | 🟢 Normal | -0.049 |  |
| 2026-05-09 01:03:34 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.059 |  |
| 2026-05-09 00:06:06 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.068 |  |
| 2026-05-09 00:04:40 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.101 |  |
| 2026-05-09 01:01:27 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.110 |  |
| 2026-05-09 01:01:21 | Kuda Oya (Kirindi Oya) | 6.69 | 🟢 Normal | -0.121 |  |
| 2026-05-09 00:05:35 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | -0.139 |  |
| 2026-05-09 01:01:14 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.484 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)