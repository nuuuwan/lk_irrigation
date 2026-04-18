# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_15:04:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-04-18 14:19:03 | Urawa (Nilwala Ganga) | -0.80 | 🟢 Normal | -0.611 |  |
| 2026-04-18 14:16:07 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:13:23 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 15:03:21 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-18 15:03:07 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-18 15:01:56 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-18 14:04:37 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-18 14:03:16 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 15:03:17 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-18 14:08:36 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:02:30 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:55 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:02:34 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:24 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:16:07 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:09:14 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:04:00 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:55 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:01:15 | Ellagawa (Kalu Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:02:08 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:01:12 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:00:44 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:02:54 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:05:44 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:04:58 | Holombuwa (Kelani Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:00:55 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:03:34 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:06:15 | Peradeniya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 15:03:50 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-18 14:13:23 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.008 |  |
| 2026-04-18 15:03:38 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:45 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:46 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-18 14:02:47 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:03:23 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-18 15:02:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.031 |  |
| 2026-04-18 14:04:34 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.049 |  |
| 2026-04-18 15:02:13 | Giriulla (Maha Oya) | 0.30 | 🟢 Normal | -0.545 |  |
| 2026-04-18 14:19:03 | Urawa (Nilwala Ganga) | -0.80 | 🟢 Normal | -0.611 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)