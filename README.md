# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_17:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,248 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 17:14:33 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.009 |  |
| 2025-12-20 17:11:59 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:10:16 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.093 |  |
| 2025-12-20 17:09:24 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:59 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:40 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:36 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:23 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:07:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.033 |  |
| 2025-12-20 17:06:19 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-20 17:06:17 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2025-12-20 17:05:59 | Weraganthota (Mahaweli Ganga) | -0.99 | 🟢 Normal | -1.468 |  |
| 2025-12-20 17:05:41 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.060 |  |
| 2025-12-20 17:05:33 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:04:44 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:04:21 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-20 17:04:19 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 17:04:14 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 17:03:43 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:03:29 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2025-12-20 17:03:13 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:03:09 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-20 17:02:42 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:02:38 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-20 17:02:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2025-12-20 17:02:04 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 17:01:53 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:51 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | -0.030 |  |
| 2025-12-20 17:01:50 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:43 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-20 17:01:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:32 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:13 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:00:54 | Horowpothana (Yan Oya) | 6.26 | 🟡 Alert | 0.000 |  |
| 2025-12-20 17:00:47 | Manampitiya (Mahaweli Ganga) | 3.22 | 🟡 Alert | -0.082 |  |
| 2025-12-20 16:25:07 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 17:00:54 | Horowpothana (Yan Oya) | 6.26 | 🟡 Alert | 0.000 |  |
| 2025-12-20 17:01:51 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | -0.030 |  |
| 2025-12-20 17:00:47 | Manampitiya (Mahaweli Ganga) | 3.22 | 🟡 Alert | -0.082 |  |
| 2025-12-20 17:06:19 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2025-12-20 17:03:29 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2025-12-20 17:01:43 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-20 16:25:07 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-20 17:04:19 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-20 17:02:04 | Ellagawa (Kalu Ganga) | 4.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 17:04:14 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 17:01:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:04:44 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:13 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:09:24 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 16:06:56 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:02:38 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:39 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:05:33 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:36 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:40 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:32 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:53 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:03:13 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:01:50 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:03:43 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:08:59 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:11:59 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:02:42 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 17:14:33 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | -0.009 |  |
| 2025-12-20 17:06:17 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.009 |  |
| 2025-12-20 17:02:38 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-20 17:03:09 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-20 17:04:21 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-20 17:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2025-12-20 17:07:20 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.033 |  |
| 2025-12-20 17:05:41 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.060 |  |
| 2025-12-20 17:10:16 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.093 |  |
| 2025-12-20 17:05:59 | Weraganthota (Mahaweli Ganga) | -0.99 | 🟢 Normal | -1.468 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)