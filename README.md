# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_19:17:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 19:17:04 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.008 |  |
| 2025-12-16 19:16:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:15:48 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:09:40 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:09:21 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:08:06 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.020 |  |
| 2025-12-16 19:07:54 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:07:32 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:07:28 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:06:38 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-16 19:05:58 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.018 |  |
| 2025-12-16 19:05:28 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:05:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-16 19:04:16 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2025-12-16 19:04:00 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2025-12-16 19:03:55 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:51 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:39 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-16 19:03:13 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:03 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:02:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2025-12-16 19:02:51 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 19:02:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 19:02:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:02:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 19:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:02:14 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:02:13 | Yaka Wewa (Ma Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-16 19:01:52 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:38 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:30 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:27 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2025-12-16 19:01:16 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:15 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:00:58 | Horowpothana (Yan Oya) | 5.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-16 19:00:09 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 19:04:00 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2025-12-16 19:06:38 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-16 19:02:51 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-16 19:00:58 | Horowpothana (Yan Oya) | 5.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-16 19:02:39 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-16 19:02:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 19:02:14 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:38 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:02:21 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:15:48 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:13 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:07:28 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:05:28 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:03 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:07:54 | Panadugama (Nilwala Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:52 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:16 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:51 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:09:40 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:07:32 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:03:55 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:09:21 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:02:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:30 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:00:09 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:01:15 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:16:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-16 19:17:04 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.008 |  |
| 2025-12-16 19:05:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2025-12-16 19:02:13 | Yaka Wewa (Ma Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-16 19:03:39 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-16 19:05:58 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.018 |  |
| 2025-12-16 19:02:51 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2025-12-16 19:08:06 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.020 |  |
| 2025-12-16 19:04:16 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2025-12-16 19:01:27 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)