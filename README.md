# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_22:20:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,415 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 22:20:49 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:20:36 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:19:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-29 22:18:52 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 22:16:42 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-29 22:14:21 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.027 |  |
| 2025-12-29 22:12:42 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-29 22:10:55 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:08:06 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:07:46 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:06:40 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:06:39 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:05:55 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:05:34 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:05:18 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2025-12-29 22:04:34 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.052 |  |
| 2025-12-29 22:04:02 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:45 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:37 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:03 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 22:02:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:42 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.015 |  |
| 2025-12-29 22:02:41 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:26 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:23 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-29 22:02:10 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:01:32 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 22:01:31 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:01:07 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:00:58 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:00:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:24:51 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 22:02:23 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2025-12-29 22:19:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-29 22:01:32 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 22:12:42 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-29 22:16:42 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-29 22:18:52 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 22:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 22:02:29 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:26 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:01:07 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:20:49 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:01:47 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:37 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:00:58 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:07:46 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:04:02 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:45 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:03 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:10:55 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:05:34 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:00:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:02:10 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:08:06 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:03:04 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:06:40 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:06:39 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:01:31 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:20:36 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-29 21:02:38 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:05:55 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 22:05:18 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | -0.010 |  |
| 2025-12-29 22:02:42 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.015 |  |
| 2025-12-29 22:14:21 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.027 |  |
| 2025-12-29 22:04:34 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.052 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)