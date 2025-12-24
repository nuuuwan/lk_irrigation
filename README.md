# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--24_19:08:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **26,844 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 19:08:43 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:08:10 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:06:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:18 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:12 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.056 |  |
| 2025-12-24 19:05:07 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:05 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:04:55 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.029 |  |
| 2025-12-24 19:04:27 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-24 19:04:11 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:03:41 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-24 19:03:39 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-24 19:03:02 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-24 19:03:02 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:02:41 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-24 19:02:37 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 19:02:27 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:02:26 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:02:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |
| 2025-12-24 19:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:13 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 19:01:07 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:02 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2025-12-24 19:00:58 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2025-12-24 19:00:43 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:00:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2025-12-24 19:00:30 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:32:02 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2025-12-24 18:24:26 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-24 18:17:15 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-24 19:02:41 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-24 19:03:02 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-24 19:04:27 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-24 18:11:09 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 19:02:37 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-24 18:24:26 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-24 19:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-24 19:02:26 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:02:27 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:43 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:06:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:13 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:07:47 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:03:02 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:05 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:07 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:17:15 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:08:10 | Padiyathalawa (Maduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:00:30 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:17 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:08:43 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:02:23 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-24 18:04:42 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:04:11 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:05:18 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:01:07 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-24 19:00:43 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.005 |  |
| 2025-12-24 19:03:41 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-24 19:03:39 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-24 18:03:33 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-24 19:04:55 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.029 |  |
| 2025-12-24 19:00:58 | Manampitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2025-12-24 18:32:02 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.040 |  |
| 2025-12-24 19:01:02 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.043 |  |
| 2025-12-24 18:01:19 | Thanthirimale (Malwathu Oya) | 2.11 | 🟢 Normal | -0.051 |  |
| 2025-12-24 18:06:36 | Panadugama (Nilwala Ganga) | 3.58 | 🟢 Normal | -0.052 |  |
| 2025-12-24 19:05:12 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.056 |  |
| 2025-12-24 19:01:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)