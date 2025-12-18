# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_13:26:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,299 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 13:26:39 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-18 13:21:52 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.023 |  |
| 2025-12-18 13:18:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-18 13:10:53 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:10:51 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:10:26 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:09:13 | Thaldena (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 13:08:48 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 13:07:59 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:07:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.023 |  |
| 2025-12-18 13:06:46 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.009 |  |
| 2025-12-18 13:06:09 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:05:37 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:04:49 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 13:04:48 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:04:17 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.591 |  |
| 2025-12-18 13:03:44 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 13:03:38 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-18 13:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2025-12-18 13:03:21 | Nakkala (Kumbukkan Oya) | 2.42 | 🟢 Normal | -0.041 |  |
| 2025-12-18 13:02:52 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:02:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:02:30 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-18 13:02:29 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | -0.031 |  |
| 2025-12-18 13:02:15 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 13:02:07 | Manampitiya (Mahaweli Ganga) | 4.03 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2025-12-18 13:01:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:32 | Horowpothana (Yan Oya) | 5.33 | 🟢 Normal | -0.010 |  |
| 2025-12-18 13:01:32 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:32 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:29 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-18 13:01:21 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 13:01:16 | Siyambalanduwa (Heda Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 13:01:16 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:00:52 | Thanthirimale (Malwathu Oya) | 4.90 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-18 13:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 13:02:07 | Manampitiya (Mahaweli Ganga) | 4.03 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2025-12-18 13:00:52 | Thanthirimale (Malwathu Oya) | 4.90 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-18 13:18:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-18 13:01:29 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-18 13:03:38 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-18 12:02:08 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-18 13:09:13 | Thaldena (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-18 13:04:49 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 13:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 13:08:48 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 13:01:16 | Siyambalanduwa (Heda Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 13:01:21 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 13:02:15 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 13:26:39 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-18 13:02:51 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:16 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:04:48 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:07:59 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:05:37 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:32 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:02:52 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:10:53 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:37 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:10:26 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 12:08:42 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:01:32 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:06:09 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:03:44 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-18 13:06:46 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | -0.009 |  |
| 2025-12-18 13:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-18 13:01:32 | Horowpothana (Yan Oya) | 5.33 | 🟢 Normal | -0.010 |  |
| 2025-12-18 13:03:30 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2025-12-18 13:02:30 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-18 13:07:13 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.023 |  |
| 2025-12-18 13:21:52 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.023 |  |
| 2025-12-18 13:02:29 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | -0.031 |  |
| 2025-12-18 13:03:21 | Nakkala (Kumbukkan Oya) | 2.42 | 🟢 Normal | -0.041 |  |
| 2025-12-17 13:11:29⌛ | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 13:04:17 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.591 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)