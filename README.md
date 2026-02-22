# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_14:08:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,040 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 14:08:39 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.018 |  |
| 2026-02-22 14:07:48 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.594 |  |
| 2026-02-22 14:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-02-22 14:07:24 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:07:23 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:05:59 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.073 |  |
| 2026-02-22 14:05:39 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:05:34 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:05:30 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.023 |  |
| 2026-02-22 14:04:56 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:04:52 | Rathnapura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.220 |  |
| 2026-02-22 14:04:43 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:04:27 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 2.884 | 🔺 Rising |
| 2026-02-22 14:04:22 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-02-22 14:04:10 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.103 |  |
| 2026-02-22 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-22 14:03:27 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-02-22 14:03:21 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.119 |  |
| 2026-02-22 14:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-02-22 14:03:07 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.124 |  |
| 2026-02-22 14:02:58 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-02-22 14:02:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:02:10 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-22 14:02:07 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.037 |  |
| 2026-02-22 14:02:01 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:02:00 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:01:59 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.082 |  |
| 2026-02-22 14:01:44 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:01:37 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.839 | 🔺 Rising |
| 2026-02-22 14:01:31 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-02-22 14:01:30 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:01:23 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 14:01:18 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:01:04 | Manampitiya (Mahaweli Ganga) | 4.05 | 🟡 Alert | -0.081 |  |
| 2026-02-22 14:00:57 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:00:40 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.033 |  |
| 2026-02-22 14:00:33 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-22 14:00:30 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-02-22 14:00:18 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 14:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-02-22 14:01:04 | Manampitiya (Mahaweli Ganga) | 4.05 | 🟡 Alert | -0.081 |  |
| 2026-02-22 14:04:27 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 2.884 | 🔺 Rising |
| 2026-02-22 14:01:37 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.839 | 🔺 Rising |
| 2026-02-22 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-02-22 14:02:10 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-22 14:01:23 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 14:05:39 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:02:00 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:00:57 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:02:01 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:07:24 | Magura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:01:18 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:04:56 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:02:18 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-22 14:04:43 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:01:44 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:05:34 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:01:30 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-22 14:08:39 | Thaldena (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.018 |  |
| 2026-02-22 14:04:22 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-02-22 14:00:33 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-22 14:05:30 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.023 |  |
| 2026-02-22 14:00:30 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.030 |  |
| 2026-02-22 14:00:40 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.033 |  |
| 2026-02-22 14:02:58 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.033 |  |
| 2026-02-22 14:02:07 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.037 |  |
| 2026-02-22 14:03:08 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.040 |  |
| 2026-02-22 14:00:18 | Weraganthota (Mahaweli Ganga) | -1.31 | 🟢 Normal | -0.040 |  |
| 2026-02-22 14:03:27 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.049 |  |
| 2026-02-22 14:05:59 | Badalgama (Maha Oya) | 3.09 | 🟢 Normal | -0.073 |  |
| 2026-02-22 14:01:59 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.082 |  |
| 2026-02-22 14:01:31 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.092 |  |
| 2026-02-22 13:01:21 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.095 |  |
| 2026-02-22 14:04:10 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | -0.103 |  |
| 2026-02-22 14:03:21 | Hanwella (Kelani Ganga) | 2.33 | 🟢 Normal | -0.119 |  |
| 2026-02-22 14:03:07 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.124 |  |
| 2026-02-22 14:04:52 | Rathnapura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.220 |  |
| 2026-02-22 14:07:48 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.594 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)