# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_20:28:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,362 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 20:28:43 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:25:54 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:21:48 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:21:42 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:19:30 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:17:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-03-24 20:14:51 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:11:28 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:11:00 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.026 |  |
| 2026-03-24 20:10:06 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:09:34 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:08:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-24 20:06:56 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-24 20:06:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:06:13 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-03-24 20:05:58 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-24 20:05:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:04:30 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:04:19 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:49 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-24 20:03:33 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.040 |  |
| 2026-03-24 20:03:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:25 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.077 |  |
| 2026-03-24 20:03:22 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:17 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |
| 2026-03-24 20:03:16 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-24 20:02:29 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-24 20:02:28 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:20 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:12 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:08 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:55 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:10 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 20:02:29 | Manampitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-24 20:06:56 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-24 20:05:58 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-24 20:03:49 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-24 20:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 20:01:10 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:55 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:21:42 | Moragaswewa (Deduru Oya) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:35 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:28 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:25:54 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:02:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:04:19 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:28:43 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:05:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:08 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:20 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:55 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:32 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:12 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:10:06 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:01:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:06:42 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:19:30 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:04:30 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:00:33 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:09:34 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:14:51 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:16 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:03:22 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 20:02:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-03-24 20:06:13 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-03-24 20:17:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.017 |  |
| 2026-03-24 20:08:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.022 |  |
| 2026-03-24 20:11:00 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.026 |  |
| 2026-03-24 20:03:33 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.040 |  |
| 2026-03-24 20:03:25 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.077 |  |
| 2026-03-24 20:03:17 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.096 |  |
| 2026-03-24 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)