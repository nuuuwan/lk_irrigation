# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_15:19:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,504 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 15:19:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:16:39 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:12:48 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:08:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:07:20 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:07:16 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:06:20 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:05:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.922 | 🔺 Rising |
| 2026-04-18 15:05:37 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:05:36 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:05:30 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 15:04:59 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:04:52 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:04:32 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-04-18 15:04:25 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:04:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:55 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:50 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:38 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:03:23 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:03:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-18 15:03:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-18 15:02:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-18 15:02:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:02:46 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:45 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:30 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:13 | Giriulla (Maha Oya) | 0.30 | 🟢 Normal | -0.545 |  |
| 2026-04-18 15:01:56 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-18 15:01:39 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:15 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:00:55 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:00:44 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:00:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 15:05:54 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.922 | 🔺 Rising |
| 2026-04-18 15:03:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-18 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-18 15:01:56 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-18 15:05:30 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 15:07:20 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:03:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:04:52 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:02:30 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:55 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:02:34 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:19:36 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:16:39 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:04:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:15 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:06:20 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:08:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:12:48 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:02:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:05:37 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:04:59 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:05:36 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:00:55 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:04:25 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:50 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:38 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:45 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:07:16 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:46 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:03:23 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:04:32 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.023 |  |
| 2026-04-18 15:02:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-18 14:04:34 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.049 |  |
| 2026-04-18 15:02:13 | Giriulla (Maha Oya) | 0.30 | 🟢 Normal | -0.545 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)