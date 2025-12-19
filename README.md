# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_00:19:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **22,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 00:19:20 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:16:56 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.016 |  |
| 2025-12-20 00:14:08 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2025-12-20 00:10:55 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-20 00:09:54 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-20 00:09:52 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-20 00:07:27 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -1.060 |  |
| 2025-12-20 00:06:10 | Manampitiya (Mahaweli Ganga) | 4.21 | 🟡 Alert | 0.056 | 🔺 Rising |
| 2025-12-20 00:06:02 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:05:36 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:05:33 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:56 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:04:47 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:29 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:04:22 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:13 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:03:52 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 00:03:23 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:03:12 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -0.050 |  |
| 2025-12-20 00:03:02 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -1.060 |  |
| 2025-12-20 00:02:25 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:02:10 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:52 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:48 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:39 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:01:36 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:25 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-20 00:01:06 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.037 |  |
| 2025-12-20 00:01:01 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:40 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:33 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:28 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:28 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:08 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-19 23:43:27 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 18:02:45 | Thanthirimale (Malwathu Oya) | 5.54 | 🟡 Alert | 0.064 | 🔺 Rising |
| 2025-12-20 00:06:10 | Manampitiya (Mahaweli Ganga) | 4.21 | 🟡 Alert | 0.056 | 🔺 Rising |
| 2025-12-20 00:14:08 | Horowpothana (Yan Oya) | 6.35 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2025-12-20 00:09:54 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-19 21:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2025-12-19 18:08:20 | Weraganthota (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-20 00:10:55 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-20 00:01:20 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-19 23:03:07 | Nakkala (Kumbukkan Oya) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 00:03:52 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 00:00:28 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:25 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:56 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:01 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-19 18:03:13 | Galgamuwa (Mee Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:02:10 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:19:20 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:05:36 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:47 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:08 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:36 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:33 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:06:02 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:05:33 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:48 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:00:28 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:01:52 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-20 00:04:50 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:04:29 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:03:23 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:02:25 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:01:39 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:04:13 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2025-12-20 00:16:56 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.016 |  |
| 2025-12-19 23:05:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.022 |  |
| 2025-12-20 00:01:06 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.037 |  |
| 2025-12-20 00:03:12 | Padiyathalawa (Maduru Oya) | 1.70 | 🟢 Normal | -0.050 |  |
| 2025-12-20 00:07:27 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -1.060 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)