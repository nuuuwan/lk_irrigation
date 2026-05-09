# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_09:38:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 09:38:23 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.032 |  |
| 2026-05-09 09:29:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-09 09:29:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-09 09:28:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-09 09:28:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-09 09:11:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 09:10:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-05-09 09:09:43 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.009 |  |
| 2026-05-09 09:08:01 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.038 |  |
| 2026-05-09 09:07:59 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-05-09 09:07:36 | Galgamuwa (Mee Oya) | 2.79 | 🟢 Normal | -0.055 |  |
| 2026-05-09 09:06:53 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.348 |  |
| 2026-05-09 09:06:35 | Rathnapura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.199 |  |
| 2026-05-09 09:06:03 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.069 |  |
| 2026-05-09 09:06:01 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.301 |  |
| 2026-05-09 09:05:47 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 09:05:20 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.124 |  |
| 2026-05-09 09:05:19 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-05-09 09:04:56 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 09:04:35 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-09 09:04:26 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-09 09:04:24 | Thanamalwila (Kirindi Oya) | 2.54 | 🟢 Normal | -0.067 |  |
| 2026-05-09 09:04:20 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-05-09 09:04:06 | Thanthirimale (Malwathu Oya) | 3.42 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-09 09:03:44 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-05-09 09:03:13 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-05-09 09:03:09 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-05-09 09:03:03 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-09 09:03:01 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 09:02:49 | Katharagama (Menik Ganga) | 1.98 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-09 09:02:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 09:02:30 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.024 |  |
| 2026-05-09 09:02:21 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-05-09 09:02:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-09 09:02:10 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-09 09:02:09 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-09 09:02:04 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-09 09:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.031 |  |
| 2026-05-09 09:01:16 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.089 |  |
| 2026-05-09 09:00:18 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -1.144 |  |
| 2026-05-09 09:00:15 | Wellawaya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.160 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 09:29:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.83 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-09 09:02:49 | Katharagama (Menik Ganga) | 1.98 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-05-09 09:02:09 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-09 09:04:26 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-09 09:02:04 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-09 09:02:20 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-09 09:04:06 | Thanthirimale (Malwathu Oya) | 3.42 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-09 09:03:01 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 09:05:47 | Moragaswewa (Deduru Oya) | 3.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-09 09:04:56 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 09:02:40 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 09:04:35 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-09 09:11:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 09:09:43 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.009 |  |
| 2026-05-09 09:02:10 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-09 09:03:03 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-09 09:03:09 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-05-09 09:02:30 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.024 |  |
| 2026-05-09 09:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.031 |  |
| 2026-05-09 09:04:20 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-05-09 09:03:44 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-05-09 09:38:23 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.032 |  |
| 2026-05-09 09:08:01 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.038 |  |
| 2026-05-09 09:03:13 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.040 |  |
| 2026-05-09 09:02:21 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.049 |  |
| 2026-05-09 09:07:36 | Galgamuwa (Mee Oya) | 2.79 | 🟢 Normal | -0.055 |  |
| 2026-05-09 09:10:03 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-05-09 09:05:19 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-05-09 09:07:59 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.060 |  |
| 2026-05-09 09:04:24 | Thanamalwila (Kirindi Oya) | 2.54 | 🟢 Normal | -0.067 |  |
| 2026-05-09 09:06:03 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.069 |  |
| 2026-05-09 09:01:16 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.089 |  |
| 2026-05-09 08:02:39 | Weraganthota (Mahaweli Ganga) | -2.62 | 🟢 Normal | -0.118 |  |
| 2026-05-09 09:05:20 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.124 |  |
| 2026-05-09 09:00:15 | Wellawaya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.160 |  |
| 2026-05-09 09:06:35 | Rathnapura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.199 |  |
| 2026-05-09 09:06:01 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.301 |  |
| 2026-05-09 09:06:53 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | -0.348 |  |
| 2026-05-09 09:00:18 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -1.144 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)