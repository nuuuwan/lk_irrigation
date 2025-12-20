# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_10:29:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 10:29:15 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:12:56 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2025-12-20 10:12:06 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:09:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2025-12-20 10:09:49 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2025-12-20 10:08:20 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | -0.009 |  |
| 2025-12-20 10:07:10 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:06:16 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:05:49 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:05:40 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-20 10:05:16 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:04:52 | Weraganthota (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-20 10:04:44 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:04:41 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:04:11 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-20 10:04:06 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:04:03 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:03:56 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:03:56 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2025-12-20 10:03:51 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:03:34 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.030 |  |
| 2025-12-20 10:03:30 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 10:03:17 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-20 10:02:53 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:02:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:02:41 | Thanthirimale (Malwathu Oya) | 5.55 | 🟡 Alert | -0.032 |  |
| 2025-12-20 10:02:39 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:02:30 | Manampitiya (Mahaweli Ganga) | 4.00 | 🟡 Alert | -0.070 |  |
| 2025-12-20 10:02:28 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.060 |  |
| 2025-12-20 10:01:55 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2025-12-20 10:01:54 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:42 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:42 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:41 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:39 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:00:45 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 09:59:57 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 09:02:17 | Horowpothana (Yan Oya) | 6.32 | 🟡 Alert | -0.023 |  |
| 2025-12-20 10:02:41 | Thanthirimale (Malwathu Oya) | 5.55 | 🟡 Alert | -0.032 |  |
| 2025-12-20 10:02:30 | Manampitiya (Mahaweli Ganga) | 4.00 | 🟡 Alert | -0.070 |  |
| 2025-12-20 10:04:11 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-20 10:04:52 | Weraganthota (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-20 10:03:30 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 10:05:40 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-20 10:01:54 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:29:15 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:42 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:05:16 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:04:41 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:02:39 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:04:06 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:42 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:00:45 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:12:06 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:02:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:02:28 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:05:49 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:07:10 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:03:56 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:01:41 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 10:12:56 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2025-12-20 10:08:20 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | -0.009 |  |
| 2025-12-20 10:09:49 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2025-12-20 10:06:16 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:04:03 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:02:53 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:03:51 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:01:39 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:04:44 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-20 10:03:56 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2025-12-20 10:03:17 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2025-12-20 10:01:55 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2025-12-20 10:09:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.029 |  |
| 2025-12-20 10:03:34 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | -0.030 |  |
| 2025-12-20 09:59:57 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.047 |  |
| 2025-12-20 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)