# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_19:13:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,178 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 19:13:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:11:22 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-28 19:10:23 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-28 19:09:28 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 19:06:56 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.038 |  |
| 2026-05-28 19:06:35 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 19:06:32 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:06:27 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 19:06:22 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:06:21 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.009 |  |
| 2026-05-28 19:06:01 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-28 19:05:46 | Rathnapura (Kalu Ganga) | 4.88 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-05-28 19:05:39 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 19:05:35 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-05-28 19:04:52 | Urawa (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.142 |  |
| 2026-05-28 19:04:50 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-28 19:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 19:04:38 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:04:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:04:06 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:03:56 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:03:43 | Baddegama (Gin Ganga) | 2.99 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 19:03:33 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 19:03:28 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:02:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-28 19:02:38 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-28 19:02:26 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:02:18 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-05-28 19:02:02 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:01:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:01:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-28 19:01:17 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:00:38 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 19:03:33 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-28 19:10:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.32 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-05-28 19:05:46 | Rathnapura (Kalu Ganga) | 4.88 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-05-28 19:05:35 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-05-28 19:00:38 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-05-28 19:10:23 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-28 19:02:38 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-28 19:06:01 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-28 19:03:43 | Baddegama (Gin Ganga) | 2.99 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-28 19:04:49 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-28 19:05:39 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 19:06:35 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-28 19:09:28 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 19:06:27 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 19:04:38 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:01:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:11:22 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:37 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:13:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:03:10 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:02:26 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:04:06 | Ellagawa (Kalu Ganga) | 8.54 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:04:09 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:01:17 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:03:28 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:06:22 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:06:32 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-05-28 18:02:12 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:02:02 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:03:56 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-28 19:06:21 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.009 |  |
| 2026-05-28 19:02:43 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-05-28 19:04:50 | Deraniyagala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-05-28 18:32:56 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.013 |  |
| 2026-05-28 18:20:47 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.023 |  |
| 2026-05-28 19:01:21 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-28 19:06:56 | Hanwella (Kelani Ganga) | 3.76 | 🟢 Normal | -0.038 |  |
| 2026-05-28 19:02:18 | Dunamale (Aththanagalu Oya) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-05-28 19:04:52 | Urawa (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)