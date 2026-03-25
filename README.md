# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_07:17:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,747 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 07:17:28 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:16:12 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-25 07:12:34 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:11:53 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:11:17 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-25 07:10:22 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:08:54 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-25 07:06:42 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2026-03-25 07:06:27 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:05:02 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:04:05 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:04:02 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:03:44 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:03:35 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-25 07:03:25 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:03:18 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-25 07:03:07 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-03-25 07:03:05 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:02:56 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:02:48 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.097 |  |
| 2026-03-25 07:02:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-25 07:02:39 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:34 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.132 |  |
| 2026-03-25 07:02:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.022 |  |
| 2026-03-25 07:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.087 |  |
| 2026-03-25 07:01:46 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-03-25 07:01:45 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:01:21 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-03-25 07:01:15 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-03-25 07:01:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-25 07:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-25 07:00:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:31 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 07:03:07 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-03-25 07:01:08 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-25 07:16:12 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-25 07:03:35 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-25 07:11:17 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-03-25 07:08:54 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-03-25 07:00:31 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:02:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:02:56 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:04:02 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-25 07:00:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:03:25 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:01:45 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:04:05 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:10:22 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:12:34 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:39 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:11:53 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:03:05 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:07:11 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:05:02 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:06:27 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:03:44 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:00:43 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:17:28 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 07:02:34 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-25 06:04:02 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-25 07:03:18 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-25 07:02:42 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-03-25 07:01:46 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-03-25 07:01:15 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2026-03-25 07:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-03-25 07:02:20 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | -0.022 |  |
| 2026-03-25 07:01:21 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.032 |  |
| 2026-03-25 07:06:42 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2026-03-25 07:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.67 | 🟢 Normal | -0.087 |  |
| 2026-03-25 07:02:48 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.097 |  |
| 2026-03-25 07:02:34 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)