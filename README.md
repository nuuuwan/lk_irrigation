# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--29_23:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **31,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 23:22:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:19:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:17:36 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:15:17 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2025-12-29 23:15:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-29 23:13:59 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 23:11:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:10:55 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:10:21 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2025-12-29 23:08:24 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.013 |  |
| 2025-12-29 23:08:10 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-29 23:07:57 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:06:49 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:05:55 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:05:44 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-29 23:04:23 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:03:40 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:02:56 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2025-12-29 23:02:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2025-12-29 23:02:47 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:02:47 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-29 23:02:40 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-29 23:02:17 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:02:06 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:59 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:44 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:00:52 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:00:37 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.125 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-29 23:15:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-29 23:00:37 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-29 23:02:40 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-29 23:05:44 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-29 22:01:32 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 23:13:59 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-29 22:18:52 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-29 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 22:02:56 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-29 23:01:58 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:02:17 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:59 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:44 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:11:58 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:03:40 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:00:52 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2025-12-29 18:07:53 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:06:49 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:04:02 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:22:35 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:02:47 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:02:06 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:17:36 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:05:55 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:01:12 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:08:06 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:19:44 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:07:57 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:10:55 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:04:23 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-29 22:25:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-29 23:15:17 | Rathnapura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2025-12-29 23:08:10 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-29 18:06:51 | Thanthirimale (Malwathu Oya) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-29 23:02:47 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2025-12-29 23:08:24 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.013 |  |
| 2025-12-29 23:10:21 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2025-12-29 23:02:56 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.041 |  |
| 2025-12-29 23:02:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)