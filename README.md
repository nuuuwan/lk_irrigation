# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_11:17:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,877 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 11:17:50 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 11:16:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-04 11:13:42 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.054 |  |
| 2026-04-04 11:09:28 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:07:42 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-04-04 11:07:37 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 11:07:13 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:05:44 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-04 11:05:37 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:05:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-04 11:04:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -72.000 |  |
| 2026-04-04 11:04:57 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | -72.000 |  |
| 2026-04-04 11:04:27 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 11:04:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:04:12 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.042 |  |
| 2026-04-04 11:04:03 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:04:00 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-04-04 11:03:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:03:33 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-04-04 11:03:03 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:59 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:51 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:50 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:48 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-04 11:02:44 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 11:02:42 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:16 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.195 |  |
| 2026-04-04 11:02:11 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.092 |  |
| 2026-04-04 11:02:09 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-04-04 11:02:01 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-04-04 11:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-04 11:01:43 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:01:38 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-04 11:01:34 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 11:01:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:01:21 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.069 |  |
| 2026-04-04 11:01:19 | Thanthirimale (Malwathu Oya) | 2.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 11:00:55 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.208 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 11:02:01 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-04-04 11:05:10 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-04 11:02:48 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-04 11:01:19 | Thanthirimale (Malwathu Oya) | 2.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 11:17:50 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-04 11:04:27 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-04 11:01:34 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 11:07:37 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-04 11:02:50 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:42 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:20 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:01:43 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:04:18 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:59 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:02:51 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:07:13 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:03:33 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:03:03 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:04:03 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:05:37 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:01:26 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:09:28 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:03:35 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-04 11:16:02 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-04 11:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-04 11:01:38 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-04 11:02:44 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-04 11:05:44 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-04-04 11:02:09 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-04-04 11:07:42 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-04-04 11:04:00 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | -0.020 |  |
| 2026-04-04 11:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-04-04 11:04:12 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.042 |  |
| 2026-04-04 11:13:42 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.054 |  |
| 2026-04-04 11:01:21 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.069 |  |
| 2026-04-04 11:02:11 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.092 |  |
| 2026-04-04 11:02:16 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.195 |  |
| 2026-04-04 11:00:55 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.208 |  |
| 2026-04-04 11:04:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)