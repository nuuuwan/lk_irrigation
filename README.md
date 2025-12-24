# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_00:41:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,028 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 00:41:43 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:25:30 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 00:16:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2025-12-25 00:16:14 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2025-12-25 00:14:53 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:10:52 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-25 00:10:52 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-25 00:09:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:08:18 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:06:40 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.034 |  |
| 2025-12-25 00:06:24 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:05:31 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.079 |  |
| 2025-12-25 00:05:26 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.037 |  |
| 2025-12-25 00:05:04 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:04:48 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 00:04:46 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:03:57 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 00:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-25 00:03:29 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.048 |  |
| 2025-12-25 00:03:28 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 00:02:55 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-25 00:02:41 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:32 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:23 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:22 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:18 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-25 00:02:09 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2025-12-25 00:02:07 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 00:02:00 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:01:52 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-25 00:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:01:23 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-25 00:01:00 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-25 00:00:06 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 00:16:54 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2025-12-25 00:10:52 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-25 00:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-25 00:02:18 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-25 00:02:55 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-25 00:10:52 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-25 00:01:00 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-25 00:25:30 | Glencourse (Kelani Ganga) | 8.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-25 00:04:48 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-25 00:03:28 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 23:02:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 00:02:07 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 00:03:57 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 00:02:23 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:04:46 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:06:24 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:22 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:09:50 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:08:18 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:07:09 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:00 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:02:41 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:14:53 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:41:43 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-24 23:01:29 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:05:04 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 00:01:23 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-25 00:00:06 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.011 |  |
| 2025-12-25 00:01:52 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 00:02:09 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2025-12-25 00:06:40 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.034 |  |
| 2025-12-25 00:05:26 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.037 |  |
| 2025-12-25 00:03:29 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.048 |  |
| 2025-12-24 23:03:14 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.049 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-25 00:05:31 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)