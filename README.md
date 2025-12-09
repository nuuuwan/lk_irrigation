# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_01:07:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,727 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 01:07:47 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.370 | 🔺 Rising |
| 2025-12-10 01:07:35 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-10 01:06:33 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.117 |  |
| 2025-12-10 01:06:16 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:06:14 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-10 01:06:12 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:05:35 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:05:12 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.023 |  |
| 2025-12-10 01:05:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:04:56 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:03:59 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 01:03:50 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 01:03:14 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 01:02:32 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:02:26 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2025-12-10 01:02:26 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-10 01:02:22 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2025-12-10 01:02:07 | Yaka Wewa (Ma Oya) | 1.57 | 🟢 Normal | -0.031 |  |
| 2025-12-10 01:02:06 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.019 |  |
| 2025-12-10 01:01:24 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-10 01:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-10 01:01:05 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 01:01:00 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-10 00:23:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-10 00:19:16 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 01:07:47 | Padiyathalawa (Maduru Oya) | 1.30 | 🟢 Normal | 0.370 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-10 01:07:35 | Panadugama (Nilwala Ganga) | 4.31 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2025-12-09 23:05:55 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-10 01:06:14 | Hanwella (Kelani Ganga) | 2.12 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-10 00:23:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-10 01:01:05 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 00:00:19 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 01:03:59 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 01:03:50 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 01:03:14 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 00:05:45 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 01:02:32 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:01:00 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:06:12 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 00:02:31 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:06:16 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:05:06 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-10 00:05:56 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:05:35 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:04:56 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-10 01:02:26 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-10 01:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-10 01:01:24 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-10 00:12:55 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-10 01:02:06 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.019 |  |
| 2025-12-10 01:02:22 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 01:02:26 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2025-12-10 00:03:14 | Rathnapura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.021 |  |
| 2025-12-10 01:05:12 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.023 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 01:02:07 | Yaka Wewa (Ma Oya) | 1.57 | 🟢 Normal | -0.031 |  |
| 2025-12-10 01:06:33 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.117 |  |
| 2025-12-10 00:02:06 | Urawa (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.270 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)