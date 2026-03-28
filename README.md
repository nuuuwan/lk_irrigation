# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--29_04:49:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **110,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 04:49:03 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.637 | 🔺 Rising |
| 2026-03-29 04:35:48 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:35:46 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:35:45 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:35:44 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:35:43 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:35:24 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-29 04:35:18 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-29 04:16:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:11:18 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-03-29 04:10:07 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-03-29 04:08:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-29 04:06:41 | Pitabeddara (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.637 | 🔺 Rising |
| 2026-03-29 04:06:28 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-03-29 04:05:53 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:05:45 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |
| 2026-03-29 04:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 04:04:47 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:04:18 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-29 04:03:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:03:02 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-29 04:02:52 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-29 04:02:49 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:02:45 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.040 |  |
| 2026-03-29 04:02:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 04:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:02:08 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:01:55 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:01:40 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-29 04:01:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-03-29 04:01:31 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:01:21 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | -0.022 |  |
| 2026-03-29 04:01:11 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:00:40 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-29 04:00:37 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.125 |  |
| 2026-03-29 04:00:33 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.086 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-29 04:49:03 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.637 | 🔺 Rising |
| 2026-03-29 04:10:07 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-03-29 04:35:24 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-29 04:04:18 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-03-29 04:35:18 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-03-29 04:01:40 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-29 04:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 04:02:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-29 03:04:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:01:55 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-29 01:03:14 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:02:49 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:01:31 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:03:02 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:35:48 | Magura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:02:15 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-29 02:05:15 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:03:32 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:16:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:02:28 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:05:53 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:04:47 | Badalgama (Maha Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-03-29 03:08:24 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-28 18:04:13 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:01:11 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:02:08 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-29 04:11:18 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-03-29 04:06:28 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-03-29 04:08:14 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-03-29 04:02:52 | Hanwella (Kelani Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-29 04:03:02 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-03-29 04:00:40 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-29 04:01:21 | Ellagawa (Kalu Ganga) | 3.64 | 🟢 Normal | -0.022 |  |
| 2026-03-29 04:01:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.033 |  |
| 2026-03-29 04:05:45 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |
| 2026-03-29 04:02:45 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.040 |  |
| 2026-03-29 04:00:37 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.125 |  |
| 2026-03-28 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)