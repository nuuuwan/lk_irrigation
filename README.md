# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_00:10:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,918 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 00:10:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.017 |  |
| 2025-12-26 00:08:17 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:07:33 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-26 00:06:16 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.028 |  |
| 2025-12-26 00:05:31 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:05:16 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.007 |  |
| 2025-12-26 00:05:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-26 00:05:07 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.020 |  |
| 2025-12-26 00:04:28 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-26 00:04:12 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 00:04:02 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.099 |  |
| 2025-12-26 00:03:30 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2025-12-26 00:03:26 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-26 00:03:25 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.351 |  |
| 2025-12-26 00:03:24 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-26 00:03:21 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.038 |  |
| 2025-12-26 00:03:16 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:11 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:03 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.101 |  |
| 2025-12-26 00:02:37 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:02:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:01:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:01:56 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:01:08 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 00:00:06 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:57:59 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:26:35 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:23:42 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 00:04:12 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-26 00:05:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-26 00:01:08 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 23:01:18 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 00:01:58 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:02:37 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:02:08 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:14 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:26:35 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:11 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:05:31 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:16 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:02:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:00:06 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:01:56 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:03:15 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:12 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:08:17 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 00:05:16 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.007 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-26 00:07:33 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-26 00:04:28 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:01:56 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:05:54 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-26 00:03:24 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:51:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.012 |  |
| 2025-12-26 00:10:14 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.017 |  |
| 2025-12-26 00:03:30 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | -0.019 |  |
| 2025-12-26 00:05:07 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.020 |  |
| 2025-12-26 00:06:16 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.028 |  |
| 2025-12-26 00:03:26 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-25 23:03:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2025-12-26 00:03:21 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.038 |  |
| 2025-12-26 00:04:02 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.099 |  |
| 2025-12-26 00:03:03 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.101 |  |
| 2025-12-26 00:03:25 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.351 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)