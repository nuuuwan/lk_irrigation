# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_01:04:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 01:04:55 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-01 01:04:43 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.024 |  |
| 2026-04-01 01:04:34 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:04:29 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-01 01:03:42 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:03:40 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:03:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-01 01:02:55 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 01:02:39 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:37 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:32 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:30 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:00:24 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.195 |  |
| 2026-04-01 00:37:24 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:17:42 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:14:43 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.024 |  |
| 2026-04-01 00:12:10 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 00:10:22 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 612.000 | 🔺 Rising |
| 2026-04-01 01:03:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-31 23:59:03 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-04-01 01:04:29 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-01 00:04:18 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-01 01:02:55 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 00:05:46 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:00:54 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:37 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:02:22 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:01:42 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:04:34 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:13 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 18:04:31 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:06:54 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:05:15 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:02:21 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:17:42 | Panadugama (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:00:44 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:03:42 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:03:05 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:02:39 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:07:38 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:32 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:02:49 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:01:30 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:12:10 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-01 01:03:40 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:06:48 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 00:05:03 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-03-31 18:01:49 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-01 01:04:55 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-01 00:01:56 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-03-31 22:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-04-01 00:00:13 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.021 |  |
| 2026-04-01 01:04:43 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.024 |  |
| 2026-03-31 18:01:04 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.088 |  |
| 2026-04-01 01:00:24 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.195 |  |
| 2026-04-01 00:08:17 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.326 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)