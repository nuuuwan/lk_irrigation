# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_18:10:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,035 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 18:10:59 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:09:32 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:09:04 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:08:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.059 |  |
| 2025-12-22 18:08:04 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:07:02 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:06:41 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.029 |  |
| 2025-12-22 18:06:02 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-22 18:05:46 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:05:28 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:04:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-22 18:04:21 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:04:14 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 3.746 | 🔺 Rising |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:03:28 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.100 |  |
| 2025-12-22 18:03:25 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:03:12 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -1.800 |  |
| 2025-12-22 18:03:07 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:57 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:52 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.021 |  |
| 2025-12-22 18:02:43 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |
| 2025-12-22 18:02:30 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:25 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-22 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.060 |  |
| 2025-12-22 18:02:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:14 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:13 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:12 | Horowpothana (Yan Oya) | 3.31 | 🟢 Normal | -1.800 |  |
| 2025-12-22 18:02:09 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2025-12-22 18:02:09 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.013 |  |
| 2025-12-22 18:02:05 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.080 |  |
| 2025-12-22 18:01:44 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2025-12-22 18:01:42 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:01:40 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.051 |  |
| 2025-12-22 18:01:34 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:01:21 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 3.746 | 🔺 Rising |
| 2025-12-22 18:00:42 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.247 |  |
| 2025-12-22 18:00:12 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:00:10 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.074 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 18:04:14 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 3.746 | 🔺 Rising |
| 2025-12-22 18:06:02 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2025-12-22 18:04:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-22 18:02:14 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:00:12 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:01:34 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:03:07 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:00:42 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:01:42 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:43 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:04:21 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:10:59 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:05:28 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:13 | Dunamale (Aththanagalu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:30 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:03:25 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:09:04 | Rathnapura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:09:32 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:08:04 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:18 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:05:46 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-22 18:02:25 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-22 18:01:44 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2025-12-22 18:02:09 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.013 |  |
| 2025-12-22 18:02:09 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2025-12-22 18:02:52 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | -0.021 |  |
| 2025-12-22 17:04:49 | Padiyathalawa (Maduru Oya) | 1.14 | 🟢 Normal | -0.028 |  |
| 2025-12-22 18:06:41 | Manampitiya (Mahaweli Ganga) | 2.32 | 🟢 Normal | -0.029 |  |
| 2025-12-22 18:01:40 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | -0.051 |  |
| 2025-12-22 18:08:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.059 |  |
| 2025-12-22 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.060 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:00:10 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.074 |  |
| 2025-12-22 18:02:05 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.080 |  |
| 2025-12-22 18:03:28 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.100 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |
| 2025-12-22 18:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.247 |  |
| 2025-12-22 18:03:12 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)