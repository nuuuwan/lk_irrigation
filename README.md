# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_03:13:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,030 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 03:13:28 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.003 |  |
| 2026-04-18 03:12:46 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -72.000 |  |
| 2026-04-18 03:12:44 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -72.000 |  |
| 2026-04-18 03:12:43 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | -72.000 |  |
| 2026-04-18 03:12:41 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -72.000 |  |
| 2026-04-18 03:12:40 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -72.000 |  |
| 2026-04-18 03:12:26 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:07:23 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:07:21 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:06:30 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:05:25 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.115 |  |
| 2026-04-18 03:05:21 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-04-18 03:05:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 2.748 | 🔺 Rising |
| 2026-04-18 03:04:40 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:04:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:04:08 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 03:04:01 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:03:59 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:03:54 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.180 |  |
| 2026-04-18 03:03:36 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:03:04 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 2.748 | 🔺 Rising |
| 2026-04-18 03:03:01 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-18 03:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -18.000 |  |
| 2026-04-18 03:02:35 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -18.000 |  |
| 2026-04-18 03:02:30 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-18 03:02:26 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:46 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:08 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:07 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.011 |  |
| 2026-04-18 03:00:48 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 02:38:29 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 03:05:15 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 2.748 | 🔺 Rising |
| 2026-04-18 03:03:01 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-18 02:21:45 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-18 03:04:08 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-18 02:13:06 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-18 03:13:28 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.003 |  |
| 2026-04-17 18:04:21 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:16 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:46 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:02:26 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:02:55 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-18 01:05:01 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:07:23 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:03:59 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:08 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:03:36 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 22:04:03 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:04:40 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:07:21 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:04:31 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:12:26 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:01:58 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 18:00:41 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:06:30 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-18 03:04:01 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-18 02:03:14 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.007 |  |
| 2026-04-18 03:02:30 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-18 03:00:48 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 03:05:21 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-04-18 02:00:57 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-17 22:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-04-18 03:01:07 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.011 |  |
| 2026-04-18 00:03:00 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.021 |  |
| 2026-04-18 00:03:24 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.022 |  |
| 2026-04-18 03:05:25 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.115 |  |
| 2026-04-18 03:03:54 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.180 |  |
| 2026-04-18 03:02:37 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -18.000 |  |
| 2026-04-18 03:12:46 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)