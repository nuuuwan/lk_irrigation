# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_15:21:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,269 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 15:21:17 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:12:29 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:12:20 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-20 15:10:27 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-20 15:08:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-20 15:07:20 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-20 15:05:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:05:09 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:04:30 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:04:24 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-20 15:04:21 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-20 15:04:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:04:12 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.012 |  |
| 2026-02-20 15:03:54 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.034 |  |
| 2026-02-20 15:03:47 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-20 15:03:46 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -20.571 |  |
| 2026-02-20 15:03:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:16 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:16 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:02:59 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-20 15:02:57 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.039 |  |
| 2026-02-20 15:02:41 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-02-20 15:02:20 | Manampitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-02-20 15:02:18 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-02-20 15:01:54 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 15:01:51 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:46 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-20 15:01:37 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 15:01:35 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:35 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:28 | Weraganthota (Mahaweli Ganga) | -0.98 | 🟢 Normal | -0.208 |  |
| 2026-02-20 15:01:17 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:00:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-20 15:00:16 | Thaldena (Mahaweli Ganga) | 1.98 | 🟢 Normal | -20.571 |  |
| 2026-02-20 15:00:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 15:02:20 | Manampitiya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-02-20 15:12:20 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-20 15:04:21 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-20 15:03:47 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-20 15:02:59 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-20 15:01:46 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-20 15:08:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-20 15:00:43 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-20 15:01:54 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-20 15:12:29 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:35 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:35 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:16 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:02:18 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:00:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:16 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:17 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:04:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:05:09 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:21:17 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:12 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:05:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:51 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:04:30 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:10:27 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-02-20 15:01:37 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-20 15:04:24 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-02-20 15:07:20 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.011 |  |
| 2026-02-20 15:04:12 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.012 |  |
| 2026-02-20 15:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-02-20 15:02:41 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2026-02-20 15:03:54 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.034 |  |
| 2026-02-20 15:02:57 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.039 |  |
| 2026-02-20 15:01:28 | Weraganthota (Mahaweli Ganga) | -0.98 | 🟢 Normal | -0.208 |  |
| 2026-02-20 14:02:08 | Padiyathalawa (Maduru Oya) | 2.18 | 🟢 Normal | -0.217 |  |
| 2026-02-20 15:03:46 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -20.571 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)