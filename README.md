# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_21:15:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 21:15:01 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:14:45 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:11:17 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:10:14 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:09:02 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 21:08:28 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:08:16 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-16 21:07:51 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:06:50 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:06:47 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:05:36 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:05:31 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 21:05:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:05:09 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-16 21:04:29 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-16 21:04:24 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:23 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 21:04:11 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:11 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.011 |  |
| 2025-12-16 21:04:05 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:05 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:03:59 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:03:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-16 21:03:21 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.029 |  |
| 2025-12-16 21:03:07 | Horowpothana (Yan Oya) | 6.01 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-16 21:03:04 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 21:02:52 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-16 21:02:40 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:32 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:06 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:01 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-16 21:01:26 | Yaka Wewa (Ma Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-16 21:01:01 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:00:31 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:24:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 21:03:07 | Horowpothana (Yan Oya) | 6.01 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-16 21:03:37 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-16 21:08:16 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-16 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-16 21:04:23 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 21:02:52 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-16 21:05:31 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-16 21:09:02 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-16 21:06:47 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:11 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:06 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:00:39 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 20:04:56 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:40 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:32 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:14:45 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:15:01 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:05 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:02:01 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:01:01 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:08:28 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:03:59 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:05:36 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:05:11 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:05 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:07:51 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:11:17 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:00:31 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:24 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 21:04:29 | Manampitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-16 20:01:59 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-16 21:05:09 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-16 21:04:11 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.011 |  |
| 2025-12-16 21:03:04 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2025-12-16 21:03:21 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.029 |  |
| 2025-12-16 21:01:26 | Yaka Wewa (Ma Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)