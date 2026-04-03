# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_20:23:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **115,317 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 20:23:33 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-03 20:09:36 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.075 |  |
| 2026-04-03 20:07:25 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.018 |  |
| 2026-04-03 20:06:36 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:06:29 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:32 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:31 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:27 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:23 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:14 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.037 |  |
| 2026-04-03 20:05:03 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:04:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 20:04:38 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-03 20:04:14 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.019 |  |
| 2026-04-03 20:03:38 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:03:37 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-03 20:03:23 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-03 20:03:19 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-04-03 20:03:16 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.053 |  |
| 2026-04-03 20:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 20:03:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.159 |  |
| 2026-04-03 20:02:54 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 20:02:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 20:02:27 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-03 20:02:27 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:27 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 20:02:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:11 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:54 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:49 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 20:01:42 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:34 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-03 20:01:24 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.028 |  |
| 2026-04-03 20:01:04 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 20:03:37 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-04-03 20:02:27 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-03 18:05:32 | Thanthirimale (Malwathu Oya) | 3.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-03 20:04:38 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-03 20:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 20:01:49 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 20:02:54 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 20:23:33 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-03 20:02:27 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 18:02:55 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 20:02:27 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 20:04:39 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 20:06:29 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:26 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:42 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:11 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:27 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:06:36 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:03 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:23 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:18 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:31 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:05:32 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:03:38 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:54 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:02:27 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 20:01:04 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-04-03 20:01:34 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-04-03 20:03:19 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-04-03 20:07:25 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.018 |  |
| 2026-04-03 20:04:14 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.019 |  |
| 2026-04-03 20:03:23 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-04-03 20:01:24 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.028 |  |
| 2026-04-03 20:05:14 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.037 |  |
| 2026-04-03 20:03:16 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.053 |  |
| 2026-04-03 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.060 |  |
| 2026-04-03 20:09:36 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.075 |  |
| 2026-04-03 20:03:11 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)