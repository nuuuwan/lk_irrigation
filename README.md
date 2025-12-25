# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_23:26:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 23:26:35 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:23:42 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.045 |  |
| 2025-12-25 23:09:42 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -13.714 |  |
| 2025-12-25 23:09:21 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -13.714 |  |
| 2025-12-25 23:09:06 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.077 |  |
| 2025-12-25 23:08:21 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:06:24 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:05:06 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:04:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:04:17 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:04:16 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-25 23:03:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2025-12-25 23:03:32 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-25 23:03:26 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:03:08 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:03:08 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:02:34 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.113 |  |
| 2025-12-25 23:02:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:02:30 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:02:09 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2025-12-25 23:02:08 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:56 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:01:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:30 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-25 23:01:24 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2025-12-25 23:01:18 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 23:01:16 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:07 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:00:56 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.075 |  |
| 2025-12-25 23:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:00:14 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-25 23:00:10 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-25 22:51:59 | Panadugama (Nilwala Ganga) | 2.95 | 🟢 Normal | -0.113 |  |
| 2025-12-25 22:51:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.012 |  |
| 2025-12-25 22:44:57 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.075 |  |
| 2025-12-25 22:36:43 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 23:01:24 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2025-12-25 23:04:16 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-25 23:00:14 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 23:03:32 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-25 23:01:18 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 23:01:16 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:07 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:02:08 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:05:06 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:26:35 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:06:24 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:03:08 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:08:21 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:04:40 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:12 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:02:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:01:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-25 23:03:26 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:36:43 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.007 |  |
| 2025-12-25 21:09:11 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 23:01:56 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:02:30 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:05:54 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:03:08 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-25 23:04:17 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:51:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.012 |  |
| 2025-12-25 23:01:30 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-25 23:02:09 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2025-12-25 23:00:10 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-25 23:03:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2025-12-25 23:23:42 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.045 |  |
| 2025-12-25 23:00:56 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.075 |  |
| 2025-12-25 23:09:06 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.077 |  |
| 2025-12-25 23:02:34 | Panadugama (Nilwala Ganga) | 2.93 | 🟢 Normal | -0.113 |  |
| 2025-12-25 23:09:42 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -13.714 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)