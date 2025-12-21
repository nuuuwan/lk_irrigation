# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_13:13:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,950 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 13:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.085 |  |
| 2025-12-21 13:12:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-21 13:12:08 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2025-12-21 13:10:19 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.053 |  |
| 2025-12-21 13:09:16 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:08:25 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.027 |  |
| 2025-12-21 13:06:57 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-21 13:06:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:06:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-21 13:05:57 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:05:08 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:05:02 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.047 |  |
| 2025-12-21 13:04:55 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:04:52 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:40 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:39 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:30 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:04:02 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:00 | Weraganthota (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-21 13:04:00 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 13:03:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:03:53 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:03:20 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:03:16 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-21 13:02:59 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:45 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:34 | Thanthirimale (Malwathu Oya) | 5.10 | 🟡 Alert | -0.020 |  |
| 2025-12-21 13:02:04 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:37 | Horowpothana (Yan Oya) | 4.92 | 🟢 Normal | -0.059 |  |
| 2025-12-21 13:01:36 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:34 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2025-12-21 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:19 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:00:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.032 |  |
| 2025-12-21 13:00:54 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 12:40:18 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 13:02:34 | Thanthirimale (Malwathu Oya) | 5.10 | 🟡 Alert | -0.020 |  |
| 2025-12-21 13:06:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2025-12-21 13:03:16 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-21 13:12:47 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-21 13:06:57 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-21 13:04:00 | Weraganthota (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-21 13:00:54 | Thaldena (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 13:04:00 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 12:06:39 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 13:03:20 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:04:30 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:59 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:06:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:03:53 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:19 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:04:55 | Baddegama (Gin Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:03:54 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:45 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:05:57 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:01:36 | Manampitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 12:11:29 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:02:04 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 13:04:40 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:39 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:02 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:09:16 | Dunamale (Aththanagalu Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:04:52 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-21 13:05:08 | Galgamuwa (Mee Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-21 12:05:22 | Padiyathalawa (Maduru Oya) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-21 13:01:34 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2025-12-21 13:08:25 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.027 |  |
| 2025-12-21 13:00:56 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.032 |  |
| 2025-12-21 13:12:08 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.039 |  |
| 2025-12-21 13:05:02 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.047 |  |
| 2025-12-21 13:10:19 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | -0.053 |  |
| 2025-12-21 13:01:37 | Horowpothana (Yan Oya) | 4.92 | 🟢 Normal | -0.059 |  |
| 2025-12-21 13:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | -0.085 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)