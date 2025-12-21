# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_19:07:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,175 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 19:07:21 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:07:17 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2025-12-21 19:06:59 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | -0.028 |  |
| 2025-12-21 19:06:12 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2025-12-21 19:05:33 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:05:31 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.019 |  |
| 2025-12-21 19:04:34 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.030 |  |
| 2025-12-21 19:04:34 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:04:33 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:04:17 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 19:04:09 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-21 19:03:53 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:03:47 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-21 19:02:47 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 19:02:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:02:33 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:02:03 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:47 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:43 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2025-12-21 19:01:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 19:01:19 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:12 | Horowpothana (Yan Oya) | 4.60 | 🟢 Normal | -0.077 |  |
| 2025-12-21 19:01:05 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:00:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.132 |  |
| 2025-12-21 19:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:00:12 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-21 18:37:54 | Horowpothana (Yan Oya) | 4.63 | 🟢 Normal | -0.077 |  |
| 2025-12-21 18:28:04 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 19:03:47 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 19:02:47 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 17:59:57 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 19:04:17 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 19:01:37 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 19:01:47 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:19 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:00:39 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:02:03 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:04:33 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:58 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:03:53 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:04:34 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 18:03:18 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:05:33 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:01:05 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:07:21 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:02:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:02:33 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 19:04:09 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-21 19:06:12 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2025-12-21 19:00:12 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-21 18:05:10 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.011 |  |
| 2025-12-21 19:07:17 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2025-12-21 19:05:31 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | -0.019 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 18:28:04 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.023 |  |
| 2025-12-21 19:06:59 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | -0.028 |  |
| 2025-12-21 19:04:34 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | -0.030 |  |
| 2025-12-21 18:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2025-12-21 18:06:05 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.037 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 19:01:43 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2025-12-21 18:04:33 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.057 |  |
| 2025-12-21 19:01:12 | Horowpothana (Yan Oya) | 4.60 | 🟢 Normal | -0.077 |  |
| 2025-12-21 18:01:25 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.092 |  |
| 2025-12-21 19:00:49 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)