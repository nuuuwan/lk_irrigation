# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_16:05:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,203 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 16:05:56 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:05:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-20 16:05:21 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2025-12-20 16:05:11 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:05:06 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:04:59 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-20 16:04:58 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:04:25 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.028 |  |
| 2025-12-20 16:04:19 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 16:04:15 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:03:33 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2025-12-20 16:03:09 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2025-12-20 16:03:03 | Weraganthota (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2025-12-20 16:02:50 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:02:37 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 16:02:18 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:02:15 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:02:14 | Manampitiya (Mahaweli Ganga) | 3.30 | 🟡 Alert | -0.127 |  |
| 2025-12-20 16:01:51 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:34 | Thanthirimale (Malwathu Oya) | 5.38 | 🟡 Alert | -0.030 |  |
| 2025-12-20 16:01:32 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:28 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:26 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:18 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:10 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 16:01:10 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 16:00:41 | Horowpothana (Yan Oya) | 6.26 | 🟡 Alert | -0.011 |  |
| 2025-12-20 16:00:36 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:00:26 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-20 15:09:54 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 15:08:14 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-20 15:07:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.116 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 16:00:41 | Horowpothana (Yan Oya) | 6.26 | 🟡 Alert | -0.011 |  |
| 2025-12-20 16:01:34 | Thanthirimale (Malwathu Oya) | 5.38 | 🟡 Alert | -0.030 |  |
| 2025-12-20 16:02:14 | Manampitiya (Mahaweli Ganga) | 3.30 | 🟡 Alert | -0.127 |  |
| 2025-12-20 15:07:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2025-12-20 16:05:28 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-20 15:08:14 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-20 16:02:37 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-20 16:04:19 | Galgamuwa (Mee Oya) | 1.87 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 16:04:59 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-20 16:01:10 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 16:01:10 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 16:01:26 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:12 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:51 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 15:09:54 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:02:50 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:03:33 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 15:06:56 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:02:18 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:00:36 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 14:03:08 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:02:15 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:28 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:04:58 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:05:56 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:01:32 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:05:11 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:04:15 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-20 15:01:51 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:05:06 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:00:26 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-20 16:01:18 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-20 15:06:02 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.011 |  |
| 2025-12-20 15:03:30 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.014 |  |
| 2025-12-20 16:05:21 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2025-12-20 16:03:09 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2025-12-20 16:04:25 | Padiyathalawa (Maduru Oya) | 1.42 | 🟢 Normal | -0.028 |  |
| 2025-12-20 16:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.029 |  |
| 2025-12-20 16:03:03 | Weraganthota (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)