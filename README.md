# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_19:38:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 19:38:51 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 19:27:06 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:22:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2025-12-28 19:13:57 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2025-12-28 19:10:51 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:10:17 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-28 19:08:16 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:08:14 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:07:02 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:06:23 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.066 |  |
| 2025-12-28 19:06:17 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:06:08 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:06:03 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.118 |  |
| 2025-12-28 19:05:32 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:05:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:04:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:04:47 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:04:17 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 19:04:03 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.065 |  |
| 2025-12-28 19:03:11 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:03:11 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:50 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-28 19:02:30 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:27 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:25 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 19:02:17 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:07 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:06 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2025-12-28 19:01:53 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 19:01:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:01:13 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2025-12-28 19:01:09 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:00:45 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:00:38 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 19:10:17 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-28 19:04:17 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-28 19:38:51 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-28 19:02:25 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 19:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-28 19:03:11 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:27:06 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:01:53 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:07:02 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:00:38 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:12:51 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:05:24 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:04:47 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:03:11 | Hanwella (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:05:32 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:08:14 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:00:45 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:01:09 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:17 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:27 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:10:51 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:07 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:06:08 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:04:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:06:17 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:09:20 | Thanthirimale (Malwathu Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:08:16 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-28 19:01:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-28 18:14:30 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2025-12-28 18:02:15 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-28 19:13:57 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.016 |  |
| 2025-12-28 19:02:06 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.020 |  |
| 2025-12-28 19:02:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2025-12-28 19:22:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2025-12-28 19:01:13 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.051 |  |
| 2025-12-28 19:04:03 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.065 |  |
| 2025-12-28 19:06:23 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.066 |  |
| 2025-12-28 19:06:03 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)