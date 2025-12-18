# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_22:09:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,640 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 22:09:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2025-12-18 22:09:07 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:08:40 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.030 |  |
| 2025-12-18 22:08:12 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:07:57 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-18 22:07:41 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:06:10 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.009 |  |
| 2025-12-18 22:05:46 | Padiyathalawa (Maduru Oya) | 1.93 | 🟢 Normal | -0.057 |  |
| 2025-12-18 22:05:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-18 22:04:59 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 22:04:46 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:04:00 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2025-12-18 22:03:56 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:25 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:07 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:06 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 22:03:05 | Manampitiya (Mahaweli Ganga) | 4.89 | 🟠 Minor Flood | 0.058 | 🔺 Rising |
| 2025-12-18 22:03:04 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 22:02:50 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:02:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:02:40 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2025-12-18 22:02:34 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:02:34 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:01:55 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:01:51 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:01:50 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.032 |  |
| 2025-12-18 22:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-18 22:01:18 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 22:01:17 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:01:16 | Horowpothana (Yan Oya) | 5.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 22:01:08 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2025-12-18 22:00:40 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | -0.080 |  |
| 2025-12-18 21:25:03 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 22:03:05 | Manampitiya (Mahaweli Ganga) | 4.89 | 🟠 Minor Flood | 0.058 | 🔺 Rising |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-18 22:07:57 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-18 22:05:31 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-18 22:01:16 | Horowpothana (Yan Oya) | 5.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 22:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-18 21:05:41 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 21:05:31 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 22:01:18 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 22:03:06 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 22:03:04 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 22:04:59 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 22:02:47 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:25 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:01:51 | Yaka Wewa (Ma Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:02:34 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:04:46 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:02:50 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:07 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:07:41 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:03:56 | Thaldena (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:08:12 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:01:17 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-18 22:09:56 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2025-12-18 22:06:10 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.009 |  |
| 2025-12-18 22:09:07 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:01:55 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:02:34 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-18 22:02:40 | Katharagama (Menik Ganga) | 0.26 | 🟢 Normal | -0.011 |  |
| 2025-12-18 22:01:08 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2025-12-18 22:08:40 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | -0.030 |  |
| 2025-12-18 22:01:50 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.032 |  |
| 2025-12-18 22:05:46 | Padiyathalawa (Maduru Oya) | 1.93 | 🟢 Normal | -0.057 |  |
| 2025-12-18 22:04:00 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2025-12-18 22:00:40 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)