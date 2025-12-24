# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_07:21:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,381 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 07:21:31 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-24 07:20:40 | Urawa (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.230 |  |
| 2025-12-24 07:20:32 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:19:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.016 |  |
| 2025-12-24 07:18:47 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.016 |  |
| 2025-12-24 07:11:19 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:11:04 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:09:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 07:09:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-24 07:09:35 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:09:34 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-24 07:08:41 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:08:38 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-24 07:08:35 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-24 07:08:10 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:07:26 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:07:13 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2025-12-24 07:06:56 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 07:06:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:06:30 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2025-12-24 07:06:23 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:06:13 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-24 07:06:09 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:05:38 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 07:05:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 07:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.099 |  |
| 2025-12-24 07:04:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:04:48 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2025-12-24 07:04:17 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:04:06 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 07:03:40 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-24 07:03:37 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.159 |  |
| 2025-12-24 07:02:39 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 07:02:32 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.128 |  |
| 2025-12-24 07:02:29 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 07:01:58 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:01:22 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:30:36 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 07:06:30 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2025-12-24 07:03:40 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-24 07:05:29 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-24 07:02:29 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-24 07:02:39 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 07:05:38 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-24 07:04:06 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 07:09:43 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 07:06:56 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 07:08:38 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-24 07:21:31 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-24 07:01:22 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:01:58 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:04:17 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:07:26 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:08:41 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 06:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:09:35 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:06:09 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:11:04 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:11:19 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:06:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:20:32 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:08:10 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:04:50 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:06:23 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-24 07:08:35 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.009 |  |
| 2025-12-24 07:09:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-24 07:09:34 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2025-12-24 07:18:47 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.016 |  |
| 2025-12-24 07:19:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.016 |  |
| 2025-12-24 07:06:13 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-24 07:07:13 | Thanthirimale (Malwathu Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2025-12-24 07:04:48 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | -0.040 |  |
| 2025-12-24 06:06:17 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.083 |  |
| 2025-12-24 07:05:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.099 |  |
| 2025-12-24 07:02:32 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.128 |  |
| 2025-12-24 07:03:37 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.159 |  |
| 2025-12-24 07:20:40 | Urawa (Nilwala Ganga) | 1.61 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)