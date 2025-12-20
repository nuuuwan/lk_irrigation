# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_23:16:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 23:16:22 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:13:42 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:13:13 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-20 23:11:57 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2025-12-20 23:11:42 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-20 23:08:33 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 23:07:14 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 23:07:12 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:06:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-20 23:06:12 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-20 23:05:14 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-20 23:04:31 | Manampitiya (Mahaweli Ganga) | 3.38 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2025-12-20 23:04:09 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 23:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:03:16 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-20 23:02:45 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:02:16 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2025-12-20 23:02:16 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:02:05 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 23:01:56 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:56 | Dunamale (Aththanagalu Oya) | 0.97 | 🟢 Normal | -0.034 |  |
| 2025-12-20 23:01:43 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:42 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:41 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:38 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:31 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:26 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 23:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |
| 2025-12-20 23:00:40 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:21:27 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.038 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 23:04:31 | Manampitiya (Mahaweli Ganga) | 3.38 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2025-12-20 22:00:50 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | -0.039 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-20 23:11:57 | Magura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2025-12-20 23:05:14 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-20 23:11:42 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-20 23:06:48 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-20 22:02:30 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-20 23:06:12 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-20 23:08:33 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 23:13:13 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-20 23:01:26 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 23:02:05 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 23:07:14 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 23:01:31 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:41 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:02:16 | Moragaswewa (Deduru Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:43 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:07:12 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:04:08 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:56 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:16:22 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:02:45 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:38 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:13:42 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 22:05:27 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:01:42 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:04:09 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 23:03:16 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-20 23:02:16 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2025-12-20 22:06:41 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | -0.018 |  |
| 2025-12-20 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-20 23:01:56 | Dunamale (Aththanagalu Oya) | 0.97 | 🟢 Normal | -0.034 |  |
| 2025-12-20 23:01:08 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)