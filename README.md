# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_21:14:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,398 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 21:14:37 | Horowpothana (Yan Oya) | 6.21 | 🟡 Alert | -0.016 |  |
| 2025-12-20 21:14:10 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:12:19 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:08:47 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-20 21:08:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.054 |  |
| 2025-12-20 21:08:03 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:07:27 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 21:07:18 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 21:06:33 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-20 21:05:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2025-12-20 21:05:02 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.157 |  |
| 2025-12-20 21:04:40 | Manampitiya (Mahaweli Ganga) | 3.19 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2025-12-20 21:04:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:04:24 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:04:19 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-20 21:04:16 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-20 21:04:07 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:53 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:39 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:38 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-20 21:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 21:02:39 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:36 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:31 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-20 21:02:18 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:09 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:01:46 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:37 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:25 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-20 21:01:24 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.021 |  |
| 2025-12-20 21:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-20 21:00:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:00:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 21:04:40 | Manampitiya (Mahaweli Ganga) | 3.19 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2025-12-20 21:14:37 | Horowpothana (Yan Oya) | 6.21 | 🟡 Alert | -0.016 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-20 21:04:16 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-20 21:06:33 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2025-12-20 21:03:38 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2025-12-20 21:04:19 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2025-12-20 21:02:31 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-20 21:01:25 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-20 21:07:27 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 21:08:47 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-20 21:07:18 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 20:08:05 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-20 21:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 21:00:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:46 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:37 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:39 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:12:19 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:04:26 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:00:45 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:08:03 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:03:53 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:14:10 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:01:15 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:04:07 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 21:05:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2025-12-20 21:04:24 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:36 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:18 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:09 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:02:39 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:00:17 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-20 21:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2025-12-20 21:01:24 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -0.021 |  |
| 2025-12-20 21:08:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.054 |  |
| 2025-12-20 21:05:02 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.157 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)