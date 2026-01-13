# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_13:06:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 13:06:51 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:05:34 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.018 |  |
| 2026-01-13 13:05:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:05:14 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-01-13 13:04:43 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:04:43 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:04:28 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:04:00 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-01-13 13:03:05 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:55 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:36 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-13 13:02:19 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:13 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:04 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:01:47 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-13 13:01:37 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:01:26 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:01:15 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:01:08 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-01-13 13:01:00 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:00:57 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:00:41 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-13 12:11:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 12:10:54 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:10:17 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-01-13 12:10:03 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-13 13:01:47 | Baddegama (Gin Ganga) | 0.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-13 13:02:36 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 12:08:34 | Horowpothana (Yan Oya) | 3.79 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 12:11:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 13:02:13 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:19 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:04 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:00:57 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:04:10 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:04:43 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:04:43 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:01:26 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:04:13 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:06:16 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:03:05 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:02:55 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:20 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:01:00 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:06:51 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:03:26 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 13:05:14 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-01-13 13:01:37 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:01:15 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:05:03 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:04:28 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:05:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-13 13:01:08 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-01-13 13:05:34 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.018 |  |
| 2026-01-13 12:09:07 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-01-13 13:00:41 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.020 |  |
| 2026-01-13 12:03:49 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-01-13 13:04:00 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-01-13 12:10:17 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-01-13 12:02:03 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.039 |  |
| 2026-01-13 12:04:17 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.043 |  |
| 2026-01-13 12:01:22 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)