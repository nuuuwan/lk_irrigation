# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_05:28:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 05:28:46 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:20:43 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:19:34 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:18:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:10:41 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:09:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:06:43 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.047 |  |
| 2026-01-20 05:06:12 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:06:11 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 05:05:54 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-01-20 05:05:34 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:25 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:23 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:07 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:06 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:04:29 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-20 05:04:24 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 05:03:56 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:03:23 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.119 |  |
| 2026-01-20 05:03:05 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:03:03 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 05:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:02:37 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-20 05:02:36 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-20 05:02:07 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:02:04 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:54 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:50 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:21 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:05 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:00:58 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:00:13 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:56:52 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 03:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-01-20 05:02:36 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-20 04:22:39 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-20 05:04:29 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-20 05:03:03 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 05:04:24 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 05:06:11 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-20 05:02:04 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:00:58 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:19:34 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:05 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:34 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:06:12 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:03:05 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:02:15 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:09:46 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:25 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:00:13 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:02:59 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:18:06 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:02:07 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:23 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-20 01:03:22 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-20 04:17:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:20:43 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:10:41 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:06 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-19 18:02:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:54 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:28:46 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:21 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:01:50 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-20 05:05:54 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.005 |  |
| 2026-01-19 18:01:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-20 05:02:37 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-19 18:00:21 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.010 |  |
| 2026-01-20 05:06:43 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.047 |  |
| 2026-01-20 05:03:23 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)