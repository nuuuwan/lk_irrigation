# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--05_01:20:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **143,103 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 01:20:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-05 01:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-05 01:11:28 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.063 |  |
| 2026-05-05 01:09:42 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.101 |  |
| 2026-05-05 01:09:07 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-05-05 01:07:55 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:07:03 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-05-05 01:06:40 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 01:05:53 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-05 01:04:43 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 01:04:38 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.091 |  |
| 2026-05-05 01:04:27 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.130 |  |
| 2026-05-05 01:03:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:03:40 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:03:25 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:56 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-05 01:02:50 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:43 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-05-05 01:02:43 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.729 | 🔺 Rising |
| 2026-05-05 01:02:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:36 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:16 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:01:46 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-05 01:01:11 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:00:55 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:00:50 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-05 00:45:51 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.101 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-05 01:02:43 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.729 | 🔺 Rising |
| 2026-05-05 01:05:53 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-05-05 01:20:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-05-05 01:16:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-04 23:06:27 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-05 00:01:28 | Yaka Wewa (Ma Oya) | 1.30 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-05 01:02:56 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-05 01:06:40 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-05 01:04:43 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-05 01:01:17 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:02:34 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:00:50 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:03:25 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:01:46 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:00:55 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:01:37 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:36 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:03:47 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:00:46 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:01:11 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:02:16 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:03:40 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-04 18:03:48 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:10:32 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-05 01:07:55 | Thanamalwila (Kirindi Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-05-04 23:07:19 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-05-05 01:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-05-05 00:07:01 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-05 00:02:52 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-05-05 01:09:07 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-05-05 01:02:43 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-05-05 01:07:03 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-05-05 00:02:25 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.062 |  |
| 2026-05-05 01:11:28 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.063 |  |
| 2026-05-05 01:04:38 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.091 |  |
| 2026-05-05 01:09:42 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.101 |  |
| 2026-05-05 01:04:27 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)