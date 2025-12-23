# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_22:28:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,061 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 22:28:49 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:15:10 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.008 |  |
| 2025-12-23 22:13:55 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-23 22:13:47 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-23 22:12:29 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-23 22:10:18 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:09:41 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-23 22:09:20 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:06:42 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:05:59 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.099 |  |
| 2025-12-23 22:05:39 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-23 22:05:26 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2025-12-23 22:05:23 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:05:07 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 22:04:52 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:04:08 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-23 22:03:51 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:03:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2025-12-23 22:03:35 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:03:13 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:03:11 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:02:37 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2025-12-23 22:02:23 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:02:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:01:42 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:01:04 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:52 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 22:00:48 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:48 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:42 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 22:04:08 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-23 22:13:47 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-23 22:09:41 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-23 22:12:29 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-23 22:00:52 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 22:05:07 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 22:01:42 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:03:40 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:03:35 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:01:04 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:28:49 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:09:20 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:42 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:07:39 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:05:23 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:48 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 21:03:58 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:00:48 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:04:52 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:06:42 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:10:18 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:02:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:03:11 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 22:15:10 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | -0.008 |  |
| 2025-12-23 22:13:55 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-23 22:05:39 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-23 22:03:16 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:03:51 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:02:23 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:03:13 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 22:02:37 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.012 |  |
| 2025-12-23 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.013 |  |
| 2025-12-23 22:05:26 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2025-12-23 21:05:47 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.021 |  |
| 2025-12-23 22:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2025-12-23 22:05:59 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)