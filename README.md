# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_17:04:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 17:04:39 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:04:35 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 17:04:03 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:59 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:53 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-17 17:03:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:15 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-17 17:03:04 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:02 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.061 |  |
| 2025-12-17 17:02:41 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:02:12 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2025-12-17 17:02:09 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | -0.041 |  |
| 2025-12-17 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2025-12-17 17:02:07 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-17 17:02:04 | Yaka Wewa (Ma Oya) | 1.74 | 🟢 Normal | -0.081 |  |
| 2025-12-17 17:02:04 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:02:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-17 17:01:57 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 17:01:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:01:19 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:01:10 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 17:00:51 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-17 17:00:38 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-17 17:00:35 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 16:26:44 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:11:34 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:08:46 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.028 |  |
| 2025-12-17 16:07:14 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2025-12-17 16:06:15 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 17:00:38 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-17 17:02:07 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-17 16:00:30 | Horowpothana (Yan Oya) | 5.87 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-17 17:03:53 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-17 17:01:10 | Thanthirimale (Malwathu Oya) | 4.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 17:00:35 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 17:04:35 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 16:04:21 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 17:01:57 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 17:02:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-17 17:01:35 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:00:05 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:06:15 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:01:19 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:59 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:02:04 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:04:03 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:02:41 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:04:39 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:05:47 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:53 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:02:31 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 17:03:04 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:05:21 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:03:29 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 17:03:15 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:05:33 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-17 17:00:51 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:03:06 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 17:02:12 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.011 |  |
| 2025-12-17 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2025-12-17 16:08:46 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.028 |  |
| 2025-12-17 16:03:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-17 17:02:09 | Glencourse (Kelani Ganga) | 9.23 | 🟢 Normal | -0.041 |  |
| 2025-12-17 17:03:02 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.061 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 17:02:04 | Yaka Wewa (Ma Oya) | 1.74 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)