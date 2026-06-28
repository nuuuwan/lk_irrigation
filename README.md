# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_19:18:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,907 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 19:18:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.048 |  |
| 2026-06-28 19:17:38 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.008 |  |
| 2026-06-28 19:16:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-28 19:14:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:14:07 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.024 |  |
| 2026-06-28 19:09:20 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:08:46 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:08:00 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-28 19:06:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:06:41 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:06:32 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:05:37 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 19:05:17 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:05:16 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-28 19:04:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-28 19:04:25 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:04:20 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:04:08 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 19:04:02 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-28 19:03:37 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:03:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-28 19:03:02 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 19:02:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:02:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:02:20 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-28 19:02:20 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:02:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.034 |  |
| 2026-06-28 19:02:12 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:02:08 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:01:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:01:30 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:00:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:00:53 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:00:12 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 19:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-06-28 19:05:16 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-06-28 19:04:02 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-28 19:04:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-28 19:02:20 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-06-28 19:08:00 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-28 19:16:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-28 19:05:37 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 19:03:02 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 19:04:08 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:00:12 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:01:45 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:05:17 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:06:32 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:04:59 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-28 18:01:02 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:02:12 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:01:30 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:14:18 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:08:46 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:04:20 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:00:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:09:20 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:04:25 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:06:41 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:06:44 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:03:37 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:02:31 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:00:53 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-28 19:17:38 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.008 |  |
| 2026-06-28 19:03:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:02:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:02:20 | Dunamale (Aththanagalu Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-06-28 18:01:23 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:02:08 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 19:14:07 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.024 |  |
| 2026-06-28 19:02:13 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.034 |  |
| 2026-06-28 19:18:41 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)