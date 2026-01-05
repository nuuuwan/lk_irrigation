# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_07:31:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,092 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 07:31:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:22:55 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:17:47 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-05 07:16:58 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:15:21 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:14:46 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:11:40 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:09:49 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.086 |  |
| 2026-01-05 07:09:15 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.057 |  |
| 2026-01-05 07:08:10 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 07:06:38 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 07:06:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:05:27 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:05:20 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-01-05 07:04:57 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:04:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2026-01-05 07:03:56 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 07:03:15 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.057 |  |
| 2026-01-05 07:03:13 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:03:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:03:05 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:53 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 07:02:50 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:44 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-01-05 07:02:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:30 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.136 |  |
| 2026-01-05 07:02:07 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.021 |  |
| 2026-01-05 07:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:01 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:01:51 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.022 |  |
| 2026-01-05 07:00:50 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.002 |  |
| 2026-01-05 07:00:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:19 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:15 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 07:17:47 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-05 07:03:56 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 07:06:38 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 07:00:15 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 07:08:10 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 07:02:53 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 07:02:30 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:16:58 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:06 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:01 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:50 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:11:40 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:42 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:01:51 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:15:21 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:19 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:02:31 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:14:46 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:03:05 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:04:57 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:03:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:06:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:22:55 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:31:17 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:03:13 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:05:27 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-05 07:00:50 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.002 |  |
| 2026-01-05 06:04:16 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-05 07:05:20 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-01-05 07:02:07 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.021 |  |
| 2026-01-05 07:00:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | -0.022 |  |
| 2026-01-05 07:02:44 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-01-05 07:09:15 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.057 |  |
| 2026-01-05 07:03:15 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.057 |  |
| 2026-01-05 07:09:49 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.086 |  |
| 2026-01-05 07:04:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.087 |  |
| 2026-01-05 06:35:53 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-01-05 07:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)