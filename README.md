# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_23:20:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,994 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 23:20:01 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.096 |  |
| 2025-12-24 23:18:46 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:17:23 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:13:52 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2025-12-24 23:09:25 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-24 23:07:37 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-24 23:07:11 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-24 23:07:09 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:06:19 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-24 23:05:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2025-12-24 23:05:08 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:04:50 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-24 23:04:35 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:04:33 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:04:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.090 |  |
| 2025-12-24 23:03:45 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:03:32 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-24 23:03:27 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-24 23:03:14 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.049 |  |
| 2025-12-24 23:03:04 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-24 23:02:54 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:02:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:02:46 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:02:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:50 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:49 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-24 23:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2025-12-24 23:01:29 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:24 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:11 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:00:42 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:00:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.080 |  |
| 2025-12-24 23:00:10 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 23:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2025-12-24 23:06:19 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-24 23:01:49 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-24 23:07:11 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-24 23:03:32 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-24 23:04:50 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-24 23:03:04 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-24 23:04:33 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:00:10 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:02:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:05:08 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 23:01:50 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:24 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:04:35 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:11 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:17:23 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:03:45 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 22:01:55 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:07:09 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:02:54 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:02:15 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 22:04:05 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:00:42 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 22:25:45 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:18:46 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:29 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:02:46 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:09:25 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2025-12-24 23:07:37 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-24 23:03:27 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2025-12-24 23:13:52 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.018 |  |
| 2025-12-24 23:05:50 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-24 23:03:14 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.049 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-24 23:00:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.080 |  |
| 2025-12-24 23:04:20 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.090 |  |
| 2025-12-24 23:20:01 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)