# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_06:08:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,121 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 06:08:47 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.010 |  |
| 2025-12-17 06:08:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2025-12-17 06:07:52 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-17 06:07:18 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-17 06:06:33 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:06:08 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-17 06:06:05 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -4.959 |  |
| 2025-12-17 06:05:47 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:05:44 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:05:31 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.019 |  |
| 2025-12-17 06:05:06 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2025-12-17 06:04:50 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2025-12-17 06:04:01 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-17 06:03:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:03:41 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 06:03:35 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:03:13 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-17 06:03:12 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:02:37 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.107 |  |
| 2025-12-17 06:02:21 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 06:02:19 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:02:04 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 06:01:54 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-17 06:01:47 | Horowpothana (Yan Oya) | 6.03 | 🟡 Alert | -0.046 |  |
| 2025-12-17 06:01:46 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:01:27 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:01:15 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.020 |  |
| 2025-12-17 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2025-12-17 06:00:29 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.012 |  |
| 2025-12-17 06:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:00:19 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:00:12 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-17 05:59:52 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:52:01 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:50:15 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.042 |  |
| 2025-12-17 05:46:53 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2025-12-17 05:41:53 | Panadugama (Nilwala Ganga) | 4.75 | 🟢 Normal | -4.959 |  |
| 2025-12-17 05:22:52 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | -0.046 |  |
| 2025-12-17 05:17:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.107 |  |
| 2025-12-17 05:13:31 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:13:30 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:11:26 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.012 |  |
| 2025-12-17 05:11:18 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | 0.075 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 06:01:47 | Horowpothana (Yan Oya) | 6.03 | 🟡 Alert | -0.046 |  |
| 2025-12-17 06:01:54 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2025-12-17 06:07:18 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2025-12-17 06:04:01 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-17 06:07:52 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-17 06:02:21 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 06:02:04 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 06:01:27 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:02:37 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:01:46 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:03:35 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:03:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:02:19 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:05:44 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:06:33 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:03:12 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:05:47 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:00:19 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:06:23 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 06:06:08 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2025-12-17 06:08:47 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.010 |  |
| 2025-12-17 06:03:41 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 06:00:12 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-17 05:46:53 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.011 |  |
| 2025-12-17 06:00:29 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.012 |  |
| 2025-12-17 06:05:31 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.019 |  |
| 2025-12-17 06:05:06 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2025-12-17 06:03:13 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2025-12-17 06:01:15 | Ellagawa (Kalu Ganga) | 4.72 | 🟢 Normal | -0.020 |  |
| 2025-12-17 06:01:11 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2025-12-17 06:08:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2025-12-17 05:50:15 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.042 |  |
| 2025-12-17 06:04:50 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.050 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-17 06:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.107 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |
| 2025-12-17 06:06:05 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -4.959 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)