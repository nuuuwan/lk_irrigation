# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_05:08:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,317 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 05:08:07 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:06:46 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:06:37 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:06:10 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:05:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:04:59 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 05:04:15 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-31 05:04:07 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:04:06 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:58 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-31 05:03:38 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:37 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 05:03:33 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 05:03:26 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:12 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:02:38 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:02:28 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:02:12 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-31 05:01:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:01:16 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.154 |  |
| 2026-01-31 05:01:14 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:01:03 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.062 |  |
| 2026-01-31 05:00:32 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:59:37 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:43:52 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-31 04:38:54 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:33:25 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:31:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.042 |  |
| 2026-01-31 04:23:18 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-31 04:23:04 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 04:16:33 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:16:17 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:15:13 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -18.000 |  |
| 2026-01-31 04:15:11 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -18.000 |  |
| 2026-01-31 04:15:10 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | -18.000 |  |
| 2026-01-31 04:15:09 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -18.000 |  |
| 2026-01-31 04:12:23 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 05:04:15 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-31 05:03:58 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-31 04:23:18 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-31 05:04:59 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 05:03:33 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 05:03:37 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-30 18:02:48 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 04:23:04 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 05:01:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:02:38 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:06:23 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:01:49 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:10:31 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:26 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:03:49 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:08:07 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:06:10 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:02:28 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:01:14 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:43 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:38 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:04:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:00:32 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:34 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 04:04:39 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:03:12 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:04:07 | Manampitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:10 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:05:50 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:10:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:06:46 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 05:02:12 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-31 04:31:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.042 |  |
| 2026-01-31 05:01:03 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | -0.062 |  |
| 2026-01-31 05:01:16 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.154 |  |
| 2026-01-31 04:06:49 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -2.769 |  |
| 2026-01-31 04:15:13 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)