# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_15:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,179 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 15:10:50 | Katharagama (Menik Ganga) | 2.09 | 🟢 Normal | -0.117 |  |
| 2026-05-09 15:09:41 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-09 15:08:51 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 15:08:46 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 15:08:27 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.019 |  |
| 2026-05-09 15:07:40 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.050 |  |
| 2026-05-09 15:07:18 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 15:07:16 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.019 |  |
| 2026-05-09 15:06:53 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:06:52 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:06:51 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:06:15 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | -0.034 |  |
| 2026-05-09 15:06:10 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:06:08 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.040 |  |
| 2026-05-09 15:05:55 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.153 |  |
| 2026-05-09 15:05:24 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:05:24 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-05-09 15:04:47 | Thanthirimale (Malwathu Oya) | 3.36 | 🟢 Normal | -0.060 |  |
| 2026-05-09 15:04:43 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:03:58 | Moragaswewa (Deduru Oya) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:03:48 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:03:28 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 15:03:17 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-05-09 15:03:09 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-05-09 15:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 15:02:38 | Moragaswewa (Deduru Oya) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:02:37 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:02:27 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-05-09 15:02:20 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.55 | 🟢 Normal | -0.093 |  |
| 2026-05-09 15:01:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 15:01:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:01:26 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.060 |  |
| 2026-05-09 15:00:47 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-05-09 15:00:13 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:00:09 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:00:09 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | -0.074 |  |
| 2026-05-09 14:24:57 | Thanthirimale (Malwathu Oya) | 3.40 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 15:02:46 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 15:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-09 15:08:46 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 15:07:18 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 15:03:28 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-09 15:08:51 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 15:00:13 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:03:58 | Moragaswewa (Deduru Oya) | 3.39 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:01:28 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:05:24 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:06:52 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:01:54 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 14:01:57 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:02:37 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:06:10 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:00:09 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-09 15:03:48 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:04:43 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:02:20 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:06:51 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:06:53 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-09 15:07:16 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.019 |  |
| 2026-05-09 15:08:27 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.019 |  |
| 2026-05-09 15:09:41 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-09 14:05:54 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-05-09 15:00:47 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.030 |  |
| 2026-05-09 15:02:27 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.032 |  |
| 2026-05-09 15:06:15 | Galgamuwa (Mee Oya) | 2.45 | 🟢 Normal | -0.034 |  |
| 2026-05-09 15:06:08 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.040 |  |
| 2026-05-09 15:03:09 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.041 |  |
| 2026-05-09 15:03:17 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-05-09 15:07:40 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.050 |  |
| 2026-05-09 15:05:24 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.054 |  |
| 2026-05-09 15:01:26 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.060 |  |
| 2026-05-09 15:04:47 | Thanthirimale (Malwathu Oya) | 3.36 | 🟢 Normal | -0.060 |  |
| 2026-05-09 15:00:09 | Kuda Oya (Kirindi Oya) | 2.41 | 🟢 Normal | -0.074 |  |
| 2026-05-09 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.55 | 🟢 Normal | -0.093 |  |
| 2026-05-09 15:10:50 | Katharagama (Menik Ganga) | 2.09 | 🟢 Normal | -0.117 |  |
| 2026-05-09 15:05:55 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)