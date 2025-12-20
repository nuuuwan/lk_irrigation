# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_13:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,093 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 13:14:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-20 13:12:48 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:11:00 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:09:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:08:18 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:07:28 | Horowpothana (Yan Oya) | 6.27 | 🟡 Alert | -0.009 |  |
| 2025-12-20 13:07:28 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:06:41 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:06:09 | Weraganthota (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2025-12-20 13:05:55 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:05:27 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:04:49 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:04:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-20 13:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-20 13:04:13 | Manampitiya (Mahaweli Ganga) | 3.66 | 🟡 Alert | -0.136 |  |
| 2025-12-20 13:04:01 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 13:03:49 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:42 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:03:32 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.022 |  |
| 2025-12-20 13:03:15 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:09 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:01 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:02:50 | Thanthirimale (Malwathu Oya) | 5.45 | 🟡 Alert | -0.033 |  |
| 2025-12-20 13:02:47 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.131 |  |
| 2025-12-20 13:02:44 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:02:35 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:02:06 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:01:45 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:01:42 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 13:01:40 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 13:01:34 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:01:31 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:01:30 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:01:13 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-20 13:01:08 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:00:54 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:00:53 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 13:07:28 | Horowpothana (Yan Oya) | 6.27 | 🟡 Alert | -0.009 |  |
| 2025-12-20 13:02:50 | Thanthirimale (Malwathu Oya) | 5.45 | 🟡 Alert | -0.033 |  |
| 2025-12-20 13:04:13 | Manampitiya (Mahaweli Ganga) | 3.66 | 🟡 Alert | -0.136 |  |
| 2025-12-20 13:06:09 | Weraganthota (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2025-12-20 13:04:30 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-20 13:01:13 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-20 13:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-20 13:14:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-20 13:04:01 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 13:01:40 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 13:01:42 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 13:01:45 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:02:06 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:01:30 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:08:18 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:01:34 | Galgamuwa (Mee Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:12:48 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:09:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:11:00 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:05:55 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:00:54 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:02:35 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:04:49 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:00:53 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:06:41 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:03:42 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-20 12:04:26 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:05:27 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 13:03:49 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:15 | Hanwella (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:01 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:07:28 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:01:31 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:02:44 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-20 12:02:07 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:01:08 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:09 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-20 13:03:32 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.022 |  |
| 2025-12-20 13:02:47 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)