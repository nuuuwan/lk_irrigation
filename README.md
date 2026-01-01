# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_07:00:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 07:00:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-01-01 07:00:15 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.046 |  |
| 2026-01-01 07:00:11 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-01-01 06:52:36 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-01 06:52:34 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-01 06:36:54 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 06:22:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-01-01 06:22:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-01-01 06:22:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-01-01 06:17:55 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-01 06:16:01 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-01-01 06:14:36 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:14:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.040 |  |
| 2026-01-01 06:11:58 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:11:32 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 06:11:31 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 06:11:30 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 06:10:40 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.015 |  |
| 2026-01-01 06:09:15 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:08:11 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.031 |  |
| 2026-01-01 06:08:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -108.000 |  |
| 2026-01-01 06:08:08 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -108.000 |  |
| 2026-01-01 06:07:40 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.046 |  |
| 2026-01-01 06:07:38 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-01 06:07:30 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-01-01 06:06:40 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.333 |  |
| 2026-01-01 06:06:39 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-01 06:05:57 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:05:47 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 06:05:16 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:05:05 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:05:04 | Katharagama (Menik Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:04:53 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 06:04:36 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.032 |  |
| 2026-01-01 06:04:02 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.039 |  |
| 2026-01-01 06:03:51 | Katharagama (Menik Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:03:04 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | -0.107 |  |
| 2026-01-01 06:02:56 | Siyambalanduwa (Heda Oya) | 1.92 | 🟢 Normal | -0.117 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 06:11:32 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-01-01 06:52:36 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-01-01 06:22:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 4.235 | 🔺 Rising |
| 2026-01-01 06:17:55 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-01 06:02:20 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-01 06:06:39 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-01 06:00:28 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-01 06:04:53 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 06:00:37 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-01 06:05:47 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-01 06:36:54 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-01 06:05:16 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:11:58 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:14:36 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:05:04 | Katharagama (Menik Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 06:16:01 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.009 |  |
| 2026-01-01 06:09:15 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:05:05 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:02:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:02:21 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-01 06:00:58 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-01-01 06:10:40 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.015 |  |
| 2026-01-01 06:07:30 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.019 |  |
| 2026-01-01 06:07:38 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-01-01 06:00:49 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.023 |  |
| 2026-01-01 06:08:11 | Thanamalwila (Kirindi Oya) | 1.94 | 🟢 Normal | -0.031 |  |
| 2026-01-01 07:00:11 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-01-01 06:04:02 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.039 |  |
| 2026-01-01 07:00:26 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.040 |  |
| 2026-01-01 06:02:25 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.041 |  |
| 2026-01-01 07:00:15 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.046 |  |
| 2026-01-01 06:01:39 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.075 |  |
| 2026-01-01 06:03:04 | Kuda Oya (Kirindi Oya) | 2.08 | 🟢 Normal | -0.107 |  |
| 2026-01-01 06:02:56 | Siyambalanduwa (Heda Oya) | 1.92 | 🟢 Normal | -0.117 |  |
| 2026-01-01 06:02:19 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.137 |  |
| 2026-01-01 06:06:40 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.333 |  |
| 2026-01-01 06:02:22 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | -108.000 |  |
| 2026-01-01 06:08:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)