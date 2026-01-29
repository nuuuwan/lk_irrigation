# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_06:18:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,580 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **46** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 06:18:14 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:17:41 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:15:09 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:11:12 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:10:47 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 06:08:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-29 06:08:53 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:07:54 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:07:42 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:06:47 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:06:15 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:06:13 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:06:11 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:04:52 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:48 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:33 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:23 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:03:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:03:46 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:03:06 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:03:00 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:02:55 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.051 |  |
| 2026-01-29 06:02:52 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.048 |  |
| 2026-01-29 06:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-01-29 06:02:32 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:02:30 | Hanwella (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-01-29 06:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-01-29 06:01:58 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-29 06:01:57 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:01:56 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-29 06:01:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:01:31 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 06:01:12 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-29 06:01:08 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-01-29 06:00:50 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:00:48 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:00:42 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:00:38 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:00:07 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.129 |  |
| 2026-01-29 05:42:28 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 05:35:25 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 05:34:26 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 05:30:20 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 06:02:33 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-01-29 06:01:58 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-29 06:08:55 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-29 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-29 06:01:56 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-29 06:01:31 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 18:04:28 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 06:10:47 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 06:03:00 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:01:12 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 05:01:16 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:06:13 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:15:09 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:52 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:33 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:03:46 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:11:12 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:48 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:06:15 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:18:14 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:01:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:03:06 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:08:53 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:07:54 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:17:41 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-29 06:04:23 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 05:34:26 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-28 18:00:30 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:03:54 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:02:32 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:06:11 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:00:38 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:00:42 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:04:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-01-29 06:02:30 | Hanwella (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-01-29 06:02:52 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.048 |  |
| 2026-01-29 06:02:55 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.051 |  |
| 2026-01-29 06:01:08 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-01-29 06:00:07 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)