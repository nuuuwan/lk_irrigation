# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_16:09:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,601 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 16:09:07 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:06:27 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-01-13 16:06:13 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:06:12 | Horowpothana (Yan Oya) | 3.90 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-13 16:06:10 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.020 |  |
| 2026-01-13 16:05:28 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-13 16:04:43 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 16:04:01 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.097 |  |
| 2026-01-13 16:03:57 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:42 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 16:03:28 | Thanthirimale (Malwathu Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-01-13 16:03:09 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:06 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:06 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:02 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-13 16:03:01 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:00 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-01-13 16:03:00 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-01-13 16:02:50 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.019 |  |
| 2026-01-13 16:02:31 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:02:30 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-13 16:02:17 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-13 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-01-13 16:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-01-13 16:02:02 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:01:55 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-01-13 16:01:41 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:01:32 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-01-13 16:01:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:01:09 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-01-13 16:00:46 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:00:42 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:00:27 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 16:03:02 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-01-13 16:05:28 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-13 16:03:42 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-13 16:06:12 | Horowpothana (Yan Oya) | 3.90 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-13 16:04:43 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 16:01:41 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:02:02 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:00:42 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:00:46 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:09:07 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:02:31 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:06 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:09 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:06:13 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:42 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:06 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:57 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 15:08:59 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:03:01 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 16:06:27 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-01-13 15:08:22 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-13 16:03:28 | Thanthirimale (Malwathu Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-01-13 15:07:35 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-01-13 16:02:30 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-13 16:01:55 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-01-13 16:02:50 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.019 |  |
| 2026-01-13 15:06:58 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | -0.019 |  |
| 2026-01-13 16:06:10 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.020 |  |
| 2026-01-13 16:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-01-13 16:02:17 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-01-13 16:00:27 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-01-13 15:01:52 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.021 |  |
| 2026-01-13 16:01:09 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-01-13 16:01:32 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-01-13 16:03:00 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-01-13 16:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-01-13 15:09:56 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.035 |  |
| 2026-01-13 16:03:00 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.041 |  |
| 2026-01-13 16:04:01 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)