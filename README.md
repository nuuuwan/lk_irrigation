# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_20:17:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,335 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 20:17:18 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:16:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:15:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-12 20:09:31 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.946 | 🔺 Rising |
| 2026-04-12 20:08:56 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.048 |  |
| 2026-04-12 20:06:38 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-12 20:06:03 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-04-12 20:05:33 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 20:05:28 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:05:16 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-04-12 20:04:47 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-12 20:04:44 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 20:04:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:04:13 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:04:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.081 |  |
| 2026-04-12 20:03:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:03:47 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:42 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.025 |  |
| 2026-04-12 20:03:14 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:10 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-04-12 20:03:04 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:02:49 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:02:35 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-12 20:02:28 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 20:02:15 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:01:58 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:01:47 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:01:24 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:01:12 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-12 20:00:11 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:26:29 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 20:09:31 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.946 | 🔺 Rising |
| 2026-04-12 20:05:16 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.515 | 🔺 Rising |
| 2026-04-12 18:07:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-12 20:15:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-12 20:01:12 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-12 20:06:38 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-12 19:03:09 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 20:02:28 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-12 20:05:33 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 20:04:44 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-12 20:01:24 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:03:56 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:05:28 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:04:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 20:00:11 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:02:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-12 19:09:12 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:04 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:01:47 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:17:18 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:47 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:14 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:16:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:01:58 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:03:42 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:06:03 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:04:13 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:02:49 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:02:15 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-12 20:04:47 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-12 20:02:35 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-12 20:03:10 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-04-12 20:03:30 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.025 |  |
| 2026-04-12 20:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-04-12 19:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.031 |  |
| 2026-04-12 18:12:59 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.033 |  |
| 2026-04-12 20:08:56 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.048 |  |
| 2026-04-12 20:04:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)