# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_08:02:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,942 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 08:02:11 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2025-12-10 08:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:02:06 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:49 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:36 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.246 |  |
| 2025-12-10 08:01:19 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:01:15 | Horowpothana (Yan Oya) | 4.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-10 08:01:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:30:50 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 07:29:04 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.084 |  |
| 2025-12-10 07:15:58 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:09:21 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 07:08:39 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2025-12-10 07:08:12 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:07:07 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-10 07:06:34 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:06:15 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2025-12-10 07:05:54 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:05:33 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:05:19 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.020 |  |
| 2025-12-10 07:05:17 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2025-12-10 07:04:37 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:04:33 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.026 |  |
| 2025-12-10 07:04:27 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:04:26 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | -0.036 |  |
| 2025-12-10 07:04:26 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | -0.021 |  |
| 2025-12-10 07:04:07 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:04:03 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.032 |  |
| 2025-12-10 07:04:03 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2025-12-10 07:03:45 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2025-12-10 07:03:44 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-10 07:03:19 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 08:01:15 | Horowpothana (Yan Oya) | 4.59 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-10 07:09:21 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-10 07:07:07 | Katharagama (Menik Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-10 07:30:50 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-10 07:03:19 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-10 07:04:27 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:02:24 | Yaka Wewa (Ma Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:13 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:05:54 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:04:07 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:05:33 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:01:49 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-10 08:02:06 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:08:12 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:04:37 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:01:25 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-10 07:02:57 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:02:10 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2025-12-10 08:01:19 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-10 07:02:42 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.019 |  |
| 2025-12-10 07:08:39 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.019 |  |
| 2025-12-10 07:06:15 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-10 07:05:19 | Glencourse (Kelani Ganga) | 9.89 | 🟢 Normal | -0.020 |  |
| 2025-12-10 07:04:03 | Hanwella (Kelani Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2025-12-10 08:02:11 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2025-12-10 07:04:33 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.026 |  |
| 2025-12-10 07:01:12 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2025-12-10 07:05:17 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2025-12-10 07:04:03 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.032 |  |
| 2025-12-10 07:04:26 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | -0.036 |  |
| 2025-12-10 07:03:45 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.042 |  |
| 2025-12-10 07:01:03 | Weraganthota (Mahaweli Ganga) | -1.16 | 🟢 Normal | -0.048 |  |
| 2025-12-10 07:03:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.064 |  |
| 2025-12-10 07:00:11 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.070 |  |
| 2025-12-10 07:29:04 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.084 |  |
| 2025-12-10 07:01:37 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.093 |  |
| 2025-12-10 08:01:36 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.246 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)