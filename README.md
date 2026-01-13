# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_17:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,646 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 17:18:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:16:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-13 17:14:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-13 17:14:02 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-01-13 17:13:26 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-01-13 17:11:47 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.009 |  |
| 2026-01-13 17:11:35 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:10:04 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:08:05 | Horowpothana (Yan Oya) | 3.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 17:07:56 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:07:45 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:07:44 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 17:07:34 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:07:15 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-13 17:06:52 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 17:06:43 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-01-13 17:06:17 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:05:45 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:05:37 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:05:36 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:05:30 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 17:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 17:04:06 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-13 17:03:47 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:03:39 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.060 |  |
| 2026-01-13 17:03:31 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:03:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-01-13 17:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 17:03:20 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 17:03:06 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:03:02 | Thanthirimale (Malwathu Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:02:55 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:02:38 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:02:26 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:02:01 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:01:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:01:11 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.031 |  |
| 2026-01-13 17:00:44 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:00:13 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 17:14:02 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-01-13 17:07:15 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-01-13 17:05:30 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 17:03:20 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 17:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 17:08:05 | Horowpothana (Yan Oya) | 3.92 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-13 17:14:59 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-13 17:16:44 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-13 17:06:52 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 17:07:44 | Dunamale (Aththanagalu Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 17:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 17:00:44 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:03:06 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:11:35 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:07:34 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:02:38 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:03:47 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:02:55 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:03:31 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:05:37 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:05:36 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:10:04 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:06:17 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:18:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:07:56 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:01:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 17:11:47 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.009 |  |
| 2026-01-13 17:05:45 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:02:26 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:02:01 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:03:02 | Thanthirimale (Malwathu Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:00:13 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:07:45 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-01-13 17:06:43 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-01-13 17:04:06 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-13 17:13:26 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-01-13 17:03:28 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.031 |  |
| 2026-01-13 17:01:11 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | -0.031 |  |
| 2026-01-13 17:03:39 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)