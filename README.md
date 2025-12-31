# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_09:27:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,692 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 09:27:29 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:16:40 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.008 |  |
| 2025-12-31 09:12:49 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-31 09:11:50 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:10:06 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:08:30 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-31 09:07:37 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 09:07:31 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-31 09:07:06 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:06:38 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:06:17 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:06:15 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-31 09:04:36 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 09:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2025-12-31 09:04:29 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:04:16 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2025-12-31 09:03:58 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:48 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:37 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-31 09:03:19 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:10 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:07 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 09:03:04 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:47 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:44 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.127 |  |
| 2025-12-31 09:02:34 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:25 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 09:02:21 | Moraketiya (Walawe Ganga) | 1.59 | 🟢 Normal | -0.368 |  |
| 2025-12-31 09:02:18 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:05 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.309 |  |
| 2025-12-31 09:02:05 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:02 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-31 09:01:47 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:01:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:01:35 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.042 |  |
| 2025-12-31 09:01:32 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:00:58 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 09:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 09:00:11 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 08:56:16 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.309 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 09:06:15 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-31 09:07:31 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-31 09:00:58 | Nagalagam Street (Kelani Ganga) | 0.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 09:02:25 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 09:03:37 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-31 09:04:36 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-31 09:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 09:03:07 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 09:07:37 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-31 09:10:06 | Weraganthota (Mahaweli Ganga) | -1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:00:11 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:04 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:47 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:11:50 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:06:17 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:07:06 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:34 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:58 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:19 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:01:32 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:01:44 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:01:47 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:18 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:04:29 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:27:29 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:48 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:02:05 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:03:10 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 09:16:40 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.008 |  |
| 2025-12-31 09:12:49 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-31 09:02:02 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-31 09:08:30 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-31 09:04:16 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2025-12-31 09:01:35 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.042 |  |
| 2025-12-31 09:04:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.068 |  |
| 2025-12-31 09:02:44 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.127 |  |
| 2025-12-31 09:02:05 | Manampitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.309 |  |
| 2025-12-31 09:02:21 | Moraketiya (Walawe Ganga) | 1.59 | 🟢 Normal | -0.368 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)