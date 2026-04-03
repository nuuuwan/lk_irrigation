# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_19:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,280 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 19:18:04 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.033 |  |
| 2026-04-03 19:13:18 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-03 19:11:22 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.114 |  |
| 2026-04-03 19:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-03 19:09:08 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-03 19:09:06 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-03 19:07:44 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-03 19:06:37 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 19:06:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-03 19:06:34 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 19:05:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.082 |  |
| 2026-04-03 19:05:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.183 |  |
| 2026-04-03 19:05:30 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-03 19:04:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 19:04:04 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-04-03 19:03:23 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:03:22 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-03 19:03:16 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:03:13 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-03 19:03:07 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:03:07 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.043 |  |
| 2026-04-03 19:03:06 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-03 19:02:59 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-03 19:02:43 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:34 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:24 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-04-03 19:02:19 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.020 |  |
| 2026-04-03 19:02:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:14 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:01 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 19:01:42 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:01:24 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:01:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:01:12 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:00:44 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:00:05 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.349 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 19:09:08 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-04-03 19:00:05 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-04-03 19:04:04 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-04-03 19:07:44 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-03 19:05:30 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-03 19:03:13 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 19:13:18 | Panadugama (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-03 19:06:34 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 19:04:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 19:06:37 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 19:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-03 19:03:22 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-03 19:02:01 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 19:00:44 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:34 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:00:51 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:01:42 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 17:19:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:03:16 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:01:12 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:43 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:15 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:14 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:03:23 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:01:12 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:03:07 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 19:02:24 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | -0.010 |  |
| 2026-04-03 19:02:59 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-04-03 19:03:06 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-03 19:06:35 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-04-03 19:02:19 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | -0.020 |  |
| 2026-04-03 19:18:04 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.033 |  |
| 2026-04-03 19:03:07 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.043 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 19:05:57 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.082 |  |
| 2026-04-03 19:11:22 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.114 |  |
| 2026-04-03 19:05:48 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)