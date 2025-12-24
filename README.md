# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_05:24:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,302 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 05:24:42 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.492 |  |
| 2025-12-24 05:23:04 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2025-12-24 05:19:24 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2025-12-24 05:13:45 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-24 05:10:52 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:09:15 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:08:54 | Urawa (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.279 |  |
| 2025-12-24 05:07:25 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-24 05:07:04 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:07:01 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-24 05:06:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:05:39 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:05:26 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:05:18 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-24 05:04:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 05:04:45 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:04:17 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:03:56 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -36.000 |  |
| 2025-12-24 05:03:55 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -36.000 |  |
| 2025-12-24 05:03:28 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.005 |  |
| 2025-12-24 05:02:48 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.049 |  |
| 2025-12-24 05:02:44 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.492 |  |
| 2025-12-24 05:02:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:02:00 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:01:54 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.040 |  |
| 2025-12-24 05:01:51 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:01:41 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 05:01:38 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-24 05:01:26 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.114 |  |
| 2025-12-24 05:00:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:00:44 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-24 05:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-24 04:47:03 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.040 |  |
| 2025-12-24 04:37:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.099 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 04:04:17 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2025-12-24 05:01:38 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-24 05:07:25 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-24 05:07:01 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-24 05:05:18 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-24 05:13:45 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-24 05:04:48 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-24 05:00:44 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-24 05:01:41 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 05:02:24 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:07:04 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:00:54 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:10:52 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:02:00 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:09:15 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-24 04:06:15 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:05:39 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:06:07 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:04:17 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-24 04:06:46 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-24 03:12:06 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-24 04:04:19 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:04:45 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:01:51 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:05:26 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-24 05:03:28 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.005 |  |
| 2025-12-24 05:19:24 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-24 05:01:54 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.040 |  |
| 2025-12-24 05:23:04 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.041 |  |
| 2025-12-24 05:02:48 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.049 |  |
| 2025-12-24 04:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -0.074 |  |
| 2025-12-24 05:01:26 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.114 |  |
| 2025-12-24 05:08:54 | Urawa (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.279 |  |
| 2025-12-24 05:24:42 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.492 |  |
| 2025-12-24 05:03:56 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)