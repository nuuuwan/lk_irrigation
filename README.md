# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--17_16:01:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,913 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 16:01:43 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-17 16:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:08 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:00:21 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-17 15:21:38 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:11:21 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-03-17 15:11:02 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-03-17 15:08:58 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:08:33 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-17 15:11:21 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-03-17 15:06:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-03-17 16:01:43 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-17 16:00:21 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-17 15:03:34 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-17 15:08:33 | Rathnapura (Kalu Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-17 15:02:15 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-17 15:03:25 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-17 15:02:39 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-17 15:02:30 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:02:36 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-17 16:01:09 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:05:44 | Galgamuwa (Mee Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:08:58 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:03:43 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:02:19 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:05:01 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:04:23 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:05:38 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:03:32 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:01:51 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:06:53 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:03:14 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:02:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:02:11 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:05:11 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:21:38 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-17 15:03:30 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-03-17 15:04:29 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-03-17 16:01:08 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-17 15:06:21 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.018 |  |
| 2026-03-17 15:02:17 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-03-17 15:04:14 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-03-17 15:00:52 | Weraganthota (Mahaweli Ganga) | -2.64 | 🟢 Normal | -0.082 |  |
| 2026-03-17 15:02:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)