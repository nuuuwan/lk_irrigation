# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_14:30:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 14:30:18 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:29:18 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-31 14:18:52 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-31 14:11:56 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-31 14:09:28 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 14:09:04 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-07-31 14:08:55 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-07-31 14:08:22 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:08:21 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-07-31 14:08:20 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-07-31 14:07:10 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 14:08:21 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-07-31 14:05:31 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-07-31 14:08:55 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-07-31 14:29:18 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-07-31 14:06:50 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-31 14:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-31 14:11:56 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-31 14:09:04 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-07-31 14:02:12 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 14:02:14 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 14:18:52 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-31 14:09:28 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-31 13:03:31 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 14:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 14:01:10 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 14:03:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:02:47 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:00:50 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:04:46 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:05:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:06:05 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:03:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:08:22 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:07:10 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:03:01 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 13:03:28 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:05:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:30:18 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:03:14 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:02:09 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:02:13 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:02:53 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:00:51 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:04:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:01:00 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 14:02:21 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-07-31 14:02:57 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-07-31 14:04:19 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-07-31 14:06:16 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)