# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_06:26:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,635 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 06:26:29 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.004 |  |
| 2026-01-09 06:12:15 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-09 06:11:23 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:09:04 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:08:52 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-01-09 06:08:10 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:07:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:07:03 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-09 06:06:57 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:05:35 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-09 06:05:33 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.109 |  |
| 2026-01-09 06:04:49 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-09 06:04:43 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-09 06:04:16 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:15 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:00 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:03:46 | Weraganthota (Mahaweli Ganga) | -1.09 | 🟢 Normal | 0.005 |  |
| 2026-01-09 06:03:42 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-09 06:03:34 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-09 06:03:32 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:03:25 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:03:08 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-09 06:02:53 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:48 | Moragaswewa (Deduru Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:44 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.090 |  |
| 2026-01-09 06:02:43 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-09 06:02:36 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-09 06:02:32 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-09 06:02:23 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 06:02:15 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-01-09 06:02:14 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-01-09 06:02:12 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-01-09 06:02:05 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:01:41 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:01:40 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-09 06:01:33 | Moragaswewa (Deduru Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:01:13 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:01:12 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-09 06:00:30 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 06:00:29 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.144 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 06:02:15 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-01-09 06:01:12 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-01-09 06:07:03 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-09 06:03:08 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-09 06:02:32 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-09 06:01:40 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-09 06:02:36 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-09 06:05:35 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-01-09 06:02:43 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-09 06:04:43 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-09 06:04:49 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-09 06:00:30 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 06:02:23 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 06:03:46 | Weraganthota (Mahaweli Ganga) | -1.09 | 🟢 Normal | 0.005 |  |
| 2026-01-09 06:26:29 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.004 |  |
| 2026-01-09 06:03:32 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:48 | Moragaswewa (Deduru Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:05:33 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:05 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:02:53 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:06:57 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:03:25 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:15 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:08:10 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:07:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:09:04 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:11:23 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:16 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:01:41 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:04:00 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:01:13 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 06:12:15 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.009 |  |
| 2026-01-09 06:03:34 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-09 06:03:42 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-09 06:08:52 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.011 |  |
| 2026-01-09 06:02:44 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.090 |  |
| 2026-01-09 06:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.109 |  |
| 2026-01-09 06:00:29 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)