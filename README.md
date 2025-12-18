# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_12:12:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 12:12:13 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:08:56 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:08:42 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:07:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-18 12:07:06 | Thaldena (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 12:07:02 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:05:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:05:34 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:05:25 | Nakkala (Kumbukkan Oya) | 2.46 | 🟢 Normal | -0.074 |  |
| 2025-12-18 12:05:11 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.013 |  |
| 2025-12-18 12:04:50 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:04:33 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-18 12:04:30 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 12:04:23 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 12:03:47 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:03:32 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.079 |  |
| 2025-12-18 12:03:28 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 12:03:22 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.411 |  |
| 2025-12-18 12:03:14 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.039 |  |
| 2025-12-18 12:03:09 | Horowpothana (Yan Oya) | 5.34 | 🟢 Normal | -0.024 |  |
| 2025-12-18 12:02:55 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 12:02:51 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.053 |  |
| 2025-12-18 12:02:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 12:02:38 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:02:26 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2025-12-18 12:02:22 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 12:02:18 | Manampitiya (Mahaweli Ganga) | 3.93 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2025-12-18 12:02:11 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-18 12:02:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 12:01:59 | Thanthirimale (Malwathu Oya) | 4.80 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-18 12:01:59 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:01:25 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:01:12 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-18 12:00:41 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-18 12:00:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2025-12-18 11:18:43 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.013 |  |
| 2025-12-18 11:17:22 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.053 |  |
| 2025-12-18 11:15:02 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 12:02:18 | Manampitiya (Mahaweli Ganga) | 3.93 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2025-12-18 12:01:59 | Thanthirimale (Malwathu Oya) | 4.80 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-18 12:07:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-18 12:04:33 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-18 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 12:03:28 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-18 12:02:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 12:02:42 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 12:04:23 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 12:01:25 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 12:07:06 | Thaldena (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 12:02:55 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 12:04:30 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 12:03:47 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:04:50 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:02:22 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:02:38 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:07:02 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:15:02 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:01:59 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:08:56 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:08:42 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:12:13 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:05:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:01:12 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-18 12:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:09:32 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.011 |  |
| 2025-12-18 12:00:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.012 |  |
| 2025-12-18 12:05:11 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.013 |  |
| 2025-12-18 12:02:26 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2025-12-18 12:02:11 | Yaka Wewa (Ma Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-18 12:03:09 | Horowpothana (Yan Oya) | 5.34 | 🟢 Normal | -0.024 |  |
| 2025-12-18 12:03:14 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.039 |  |
| 2025-12-18 12:02:51 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.053 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 12:05:25 | Nakkala (Kumbukkan Oya) | 2.46 | 🟢 Normal | -0.074 |  |
| 2025-12-18 12:03:32 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.079 |  |
| 2025-12-18 12:03:22 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.411 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)