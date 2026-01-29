# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_10:15:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 10:15:31 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:11:40 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:11:30 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-29 10:10:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:10:07 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:09:47 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-01-29 10:09:46 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:09:34 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-01-29 10:09:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.045 |  |
| 2026-01-29 10:08:31 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.040 |  |
| 2026-01-29 10:08:24 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:07:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:07:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-29 10:06:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:06:25 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-29 10:06:17 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:05:33 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:57 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:03:43 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:34 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:30 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-29 10:03:19 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:03:04 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:04 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-29 10:02:40 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:39 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:18 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:11 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:01:57 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.011 |  |
| 2026-01-29 10:01:26 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-01-29 10:01:16 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-29 10:01:06 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:00:55 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-29 10:00:35 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:00:21 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:00:16 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 10:09:47 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-01-29 10:06:25 | Kithulgala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-29 10:01:26 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-01-29 10:03:30 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-29 10:07:04 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-29 10:03:04 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-29 10:01:06 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:00:35 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:03:19 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:03:57 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 10:02:11 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:00:21 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:43 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:06 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:11:40 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:15:31 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:10:07 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:40 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:09:46 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:06:46 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:04 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:07:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:22 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:36 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:03:34 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:05:33 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:18 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:06:17 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:10:19 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:02:39 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 10:09:34 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-01-29 10:11:30 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-29 10:00:16 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-01-29 10:00:55 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-29 10:01:57 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.011 |  |
| 2026-01-29 10:01:16 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-01-29 10:08:31 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.040 |  |
| 2026-01-29 10:09:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)