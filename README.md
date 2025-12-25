# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_18:12:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,712 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 18:12:39 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.090 |  |
| 2025-12-25 18:11:55 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.028 |  |
| 2025-12-25 18:11:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.081 |  |
| 2025-12-25 18:09:29 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:08:41 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2025-12-25 18:08:19 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 18:06:46 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.049 |  |
| 2025-12-25 18:06:19 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:18 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 18:06:07 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:01 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.030 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:00 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:53 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:45 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:29 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:27 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.101 |  |
| 2025-12-25 18:04:03 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:03:19 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 18:03:08 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.078 |  |
| 2025-12-25 18:02:46 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 18:02:20 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.020 |  |
| 2025-12-25 18:02:12 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2025-12-25 18:01:57 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:01:56 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2025-12-25 18:01:52 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.014 |  |
| 2025-12-25 18:01:31 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 18:01:20 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-25 18:00:31 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 18:00:15 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.056 |  |
| 2025-12-25 17:31:39 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-25 17:20:16 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.014 |  |
| 2025-12-25 17:19:33 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 18:01:20 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 17:31:39 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-25 18:03:19 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 18:01:31 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 18:06:18 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 17:03:19 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:09:29 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:03 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:00 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:29 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:02:12 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:19 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:45 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:53 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:04:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:08:19 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:12:11 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 17:05:32 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:01:57 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:07 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:08:41 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 17:03:33 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-25 18:01:52 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.014 |  |
| 2025-12-25 18:02:20 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.020 |  |
| 2025-12-25 18:00:31 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-25 18:11:55 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.028 |  |
| 2025-12-25 18:01:56 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.030 |  |
| 2025-12-25 18:06:01 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.030 |  |
| 2025-12-25 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2025-12-25 18:06:46 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.049 |  |
| 2025-12-25 18:00:15 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.056 |  |
| 2025-12-25 18:03:08 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.078 |  |
| 2025-12-25 18:11:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.081 |  |
| 2025-12-25 18:12:39 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.090 |  |
| 2025-12-25 18:04:27 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)