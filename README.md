# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_09:10:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,242 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 09:10:31 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.017 |  |
| 2025-12-17 09:09:45 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-17 09:07:27 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:07:15 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.011 |  |
| 2025-12-17 09:07:04 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 09:06:26 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-17 09:05:32 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:05:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.059 |  |
| 2025-12-17 09:05:13 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:05:05 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.012 |  |
| 2025-12-17 09:04:54 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-17 09:04:42 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:04:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2025-12-17 09:04:32 | Horowpothana (Yan Oya) | 5.90 | 🟢 Normal | -0.038 |  |
| 2025-12-17 09:04:29 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 09:04:28 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.029 |  |
| 2025-12-17 09:04:26 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:04:24 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:04:07 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2025-12-17 09:04:05 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 09:03:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:03:21 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 09:03:07 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:02:44 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:02:39 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2025-12-17 09:02:32 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 09:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.081 |  |
| 2025-12-17 09:02:09 | Thanthirimale (Malwathu Oya) | 3.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 09:01:58 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.022 |  |
| 2025-12-17 09:01:49 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:40 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:36 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:25 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:19 | Yaka Wewa (Ma Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2025-12-17 09:00:48 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | 2.334 | 🔺 Rising |
| 2025-12-17 09:00:33 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2025-12-17 08:12:56 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 09:00:48 | Moraketiya (Walawe Ganga) | 3.20 | 🟡 Alert | 2.334 | 🔺 Rising |
| 2025-12-17 09:02:09 | Thanthirimale (Malwathu Oya) | 3.75 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 09:04:05 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 09:06:26 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-17 09:04:29 | Moragaswewa (Deduru Oya) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 09:09:45 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-17 09:02:32 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 09:03:21 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 09:07:04 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 09:01:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:04:42 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:02:46 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:02:44 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:40 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:03:07 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:03:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 08:02:06 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:25 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:49 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:01:36 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 09:07:27 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:05:32 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:05:13 | Hanwella (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:04:24 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:04:26 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-17 09:02:39 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2025-12-17 09:07:15 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.011 |  |
| 2025-12-17 09:04:54 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2025-12-17 09:05:05 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.012 |  |
| 2025-12-17 09:10:31 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.017 |  |
| 2025-12-17 09:01:19 | Yaka Wewa (Ma Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2025-12-17 09:01:58 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.022 |  |
| 2025-12-17 09:04:07 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2025-12-17 09:04:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.029 |  |
| 2025-12-17 09:04:28 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.029 |  |
| 2025-12-17 09:00:33 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.030 |  |
| 2025-12-17 09:04:32 | Horowpothana (Yan Oya) | 5.90 | 🟢 Normal | -0.038 |  |
| 2025-12-17 09:05:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.059 |  |
| 2025-12-17 09:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)