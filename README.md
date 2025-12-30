# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_04:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 04:15:08 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:15:04 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2025-12-31 04:12:49 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:10:17 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-31 04:09:32 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 04:08:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:07:45 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:07:45 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:06:49 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-31 04:06:38 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:06:11 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:04:59 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-31 04:04:15 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:03:42 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-31 04:03:41 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-31 04:03:37 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-31 04:03:35 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.060 |  |
| 2025-12-31 04:03:32 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-31 04:03:32 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:03:29 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-31 04:03:23 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:03:21 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:02:47 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:02:29 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-31 04:02:27 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-31 04:02:13 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:01:52 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 04:01:39 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.041 |  |
| 2025-12-31 04:01:21 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 04:01:12 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:52:09 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:47:49 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:34:53 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.015 |  |
| 2025-12-31 03:23:33 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 04:03:42 | Manampitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2025-12-31 04:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-31 04:06:49 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-31 04:03:37 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-31 04:09:32 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-31 04:02:29 | Hanwella (Kelani Ganga) | 0.53 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-31 04:10:17 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-31 04:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 04:01:21 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 03:01:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:12:49 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:04:51 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:04:15 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:02:13 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-31 02:28:17 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:03:32 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:15:06 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:01:12 | Ellagawa (Kalu Ganga) | 4.27 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:07:45 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:06:19 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:01:52 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:08:45 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:07:45 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:02:47 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:06:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:03:23 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:06:11 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:06:38 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:03:21 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:15:08 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-31 03:07:53 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-31 04:02:27 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-31 04:15:04 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.015 |  |
| 2025-12-31 04:01:39 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.041 |  |
| 2025-12-31 04:03:35 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.060 |  |
| 2025-12-31 03:04:00 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)