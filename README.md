# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_07:19:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,023 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 07:19:58 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.016 |  |
| 2026-01-15 07:15:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:12:24 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-01-15 07:10:30 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.128 |  |
| 2026-01-15 07:08:59 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-15 07:08:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.126 |  |
| 2026-01-15 07:08:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-01-15 07:07:53 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-15 07:07:52 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:07:29 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:05:24 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:05:13 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-01-15 07:05:00 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-01-15 07:04:53 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:43 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-01-15 07:04:40 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:31 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:29 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.009 |  |
| 2026-01-15 07:04:21 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:00 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:03:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:03:37 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-01-15 07:03:34 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:02:59 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 07:02:55 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.156 |  |
| 2026-01-15 07:02:53 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 07:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 07:02:24 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-15 07:02:13 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.015 |  |
| 2026-01-15 07:01:51 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:36 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:26 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:05 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:00:23 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:00:12 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.086 |  |
| 2026-01-15 06:32:37 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:24:32 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.156 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 07:07:53 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-15 07:02:53 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 06:07:27 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 07:02:59 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 07:02:45 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 06:03:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:53 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:00:23 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:15:12 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:07:52 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:03:34 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:05:24 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:03:45 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:51 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:31 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:00 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:05 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:07:29 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:21 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:04:40 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:26 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 06:01:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:01:36 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-15 07:08:59 | Pitabeddara (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-15 07:04:29 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.009 |  |
| 2026-01-15 07:02:24 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-01-15 07:03:37 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-01-15 07:02:13 | Thanthirimale (Malwathu Oya) | 2.00 | 🟢 Normal | -0.015 |  |
| 2026-01-15 07:19:58 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.016 |  |
| 2026-01-15 07:05:13 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-01-15 07:12:24 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-01-15 07:05:00 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-01-15 07:04:43 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-01-15 07:08:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-01-15 06:01:19 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-15 07:00:12 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | -0.086 |  |
| 2026-01-15 07:08:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.03 | 🟢 Normal | -0.126 |  |
| 2026-01-15 07:10:30 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.128 |  |
| 2026-01-15 07:02:55 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)