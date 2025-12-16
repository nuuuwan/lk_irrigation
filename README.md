# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_01:03:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,929 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 01:03:37 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 01:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:33 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:03:33 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:03:22 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:02:45 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-17 01:02:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:01:00 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:57 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:00:44 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | 0.000 |  |
| 2025-12-17 01:00:26 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:12 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:52:21 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:10:26 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.027 |  |
| 2025-12-17 00:10:18 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 00:08:45 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2025-12-17 00:08:36 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:08:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:06:02 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-17 00:05:43 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:05:33 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:05:19 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-17 00:05:05 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.011 |  |
| 2025-12-17 00:05:04 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-17 00:04:52 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:04:49 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.134 |  |
| 2025-12-17 00:04:47 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 01:00:44 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | 0.000 |  |
| 2025-12-17 00:04:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-16 23:03:41 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-17 00:01:02 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-17 00:10:18 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 00:06:02 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-17 00:04:47 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 01:03:37 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 00:04:36 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:03:12 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:02:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:52:21 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:12 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:03:14 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:01:52 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:33 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:55:32 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:05:43 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:08:36 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 00:08:36 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:35 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:00:26 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:02:40 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 01:03:24 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 00:05:04 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:01:00 | Ellagawa (Kalu Ganga) | 4.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:05:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:03:33 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-17 01:00:57 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2025-12-17 01:03:22 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-16 22:09:53 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2025-12-17 01:02:45 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2025-12-17 00:10:26 | Katharagama (Menik Ganga) | 0.21 | 🟢 Normal | -0.027 |  |
| 2025-12-17 00:01:24 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.051 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-17 00:04:49 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.134 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)