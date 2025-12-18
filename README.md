# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_20:08:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,564 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 20:08:18 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-18 20:07:42 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:07:30 | Horowpothana (Yan Oya) | 5.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-18 20:06:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 20:06:02 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:04:51 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.040 |  |
| 2025-12-18 20:04:47 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2025-12-18 20:04:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2025-12-18 20:04:22 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:04:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 20:04:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:04:09 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:03:37 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:02:43 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 20:02:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-18 20:02:33 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:02:31 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.083 |  |
| 2025-12-18 20:02:29 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-18 20:02:19 | Siyambalanduwa (Heda Oya) | 1.52 | 🟢 Normal | -0.031 |  |
| 2025-12-18 20:02:05 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-18 20:01:58 | Manampitiya (Mahaweli Ganga) | 4.78 | 🟠 Minor Flood | 0.059 | 🔺 Rising |
| 2025-12-18 20:01:43 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.020 |  |
| 2025-12-18 20:01:29 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:01:24 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 20:01:15 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:01:06 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-18 20:00:42 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:00:37 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-18 20:00:15 | Nakkala (Kumbukkan Oya) | 2.36 | 🟢 Normal | -0.120 |  |
| 2025-12-18 20:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.061 |  |
| 2025-12-18 19:47:28 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-18 19:33:07 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-18 19:32:51 | Horowpothana (Yan Oya) | 5.30 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-18 19:26:40 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2025-12-18 19:14:52 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:12:18 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-18 19:11:25 | Manampitiya (Mahaweli Ganga) | 4.73 | 🟠 Minor Flood | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 20:01:58 | Manampitiya (Mahaweli Ganga) | 4.78 | 🟠 Minor Flood | 0.059 | 🔺 Rising |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-18 20:01:06 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2025-12-18 20:07:30 | Horowpothana (Yan Oya) | 5.34 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-18 20:04:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 20:06:46 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 19:07:43 | Padiyathalawa (Maduru Oya) | 2.35 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-18 20:00:37 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-18 19:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 20:01:24 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 19:07:10 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 20:02:43 | Peradeniya (Mahaweli Ganga) | 2.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 19:07:16 | Badalgama (Maha Oya) | 2.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 20:03:37 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:07:42 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:04:22 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:04:09 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 20:02:33 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:00:42 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:06:02 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:01:29 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:04:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 19:02:25 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:01:15 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-18 20:08:18 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-18 20:02:29 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-18 20:02:05 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-18 20:01:43 | Ellagawa (Kalu Ganga) | 4.86 | 🟢 Normal | -0.020 |  |
| 2025-12-18 20:02:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2025-12-18 19:03:18 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2025-12-18 20:02:19 | Siyambalanduwa (Heda Oya) | 1.52 | 🟢 Normal | -0.031 |  |
| 2025-12-18 20:04:47 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2025-12-18 20:04:51 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | -0.040 |  |
| 2025-12-18 20:04:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.057 |  |
| 2025-12-18 20:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.061 |  |
| 2025-12-18 20:02:31 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.083 |  |
| 2025-12-18 20:00:15 | Nakkala (Kumbukkan Oya) | 2.36 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)