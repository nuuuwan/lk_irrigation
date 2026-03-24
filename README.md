# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_16:01:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,177 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 16:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-24 16:01:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:41 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 16:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:12 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:10 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:00:57 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-24 16:00:55 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 16:00:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:13:37 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-24 15:11:18 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:10:46 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:08:21 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:07:17 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:07:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:06:50 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:06:25 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 15:03:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-24 15:03:22 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-24 15:13:37 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-24 15:01:35 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-24 16:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-24 15:02:30 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 16:00:55 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 16:01:41 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 15:02:24 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:00:28 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:03:17 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:37 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:42 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:00:28 | Horowpothana (Yan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:05:07 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:10:46 | Pitabeddara (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:03:41 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:03:47 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:04:19 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:02:59 | Baddegama (Gin Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:11:18 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:03:35 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:05:43 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:03:01 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:07:17 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:02:18 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:07:11 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:10 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:06:25 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 16:01:12 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:06:50 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-03-24 15:04:57 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-03-24 15:02:41 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-03-24 15:01:25 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-24 16:00:57 | Kithulgala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-03-24 15:04:19 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.029 |  |
| 2026-03-24 15:01:29 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.033 |  |
| 2026-03-24 15:02:02 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)