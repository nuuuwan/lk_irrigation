# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_21:17:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,395 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 21:17:35 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-03-24 21:14:21 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:09:35 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.009 |  |
| 2026-03-24 21:07:29 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:07:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.085 |  |
| 2026-03-24 21:07:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.132 |  |
| 2026-03-24 21:06:47 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:05:50 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.186 |  |
| 2026-03-24 21:05:29 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.029 |  |
| 2026-03-24 21:05:13 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:05:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:04:54 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-24 21:04:22 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-03-24 21:03:23 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-24 21:03:22 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 21:03:20 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:03:20 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:57 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:56 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-24 21:02:54 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:49 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:43 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:20 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-24 21:02:13 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:09 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.039 |  |
| 2026-03-24 21:02:07 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:01:59 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:01:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 21:01:49 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:01:43 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-24 21:01:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:00:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:00:15 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:28:43 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:25:54 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 21:02:56 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-03-24 21:03:23 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-24 21:04:54 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-24 21:01:43 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-24 21:03:22 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 20:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 21:01:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 21:02:54 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:00:30 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:49 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:01:20 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:57 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:03:20 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:02:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:07 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:28:43 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:01:59 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:43 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:03:20 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:05:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:07:29 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:14:21 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:05:13 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:00:33 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:06:47 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:00:15 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:01:49 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:02:13 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 21:09:35 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.009 |  |
| 2026-03-24 21:02:20 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-24 20:08:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-24 21:05:29 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.029 |  |
| 2026-03-24 21:17:35 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.039 |  |
| 2026-03-24 21:04:22 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-03-24 21:07:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.085 |  |
| 2026-03-24 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.120 |  |
| 2026-03-24 21:07:13 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.132 |  |
| 2026-03-24 21:05:50 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)