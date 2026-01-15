# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_15:08:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **46,340 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 15:08:48 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:07:16 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:07:03 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.011 |  |
| 2026-01-15 15:06:39 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:05:57 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:05:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-01-15 15:05:38 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.028 |  |
| 2026-01-15 15:05:37 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:05:28 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:04:42 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:04:26 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:57 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:45 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-01-15 15:03:34 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 15:03:33 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:29 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-01-15 15:03:28 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 15:03:26 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.073 |  |
| 2026-01-15 15:03:19 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:17 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:05 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:02:26 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:02:23 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:02:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:02:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-01-15 15:02:07 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -5.400 |  |
| 2026-01-15 15:01:47 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:01:42 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:01:38 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 15:01:32 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | -0.050 |  |
| 2026-01-15 15:01:31 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:01:15 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-15 15:00:43 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:00:29 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.025 |  |
| 2026-01-15 15:00:21 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.087 |  |
| 2026-01-15 15:00:07 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -5.400 |  |
| 2026-01-15 14:43:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-15 14:36:26 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.025 |  |
| 2026-01-15 14:22:27 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.073 |  |
| 2026-01-15 14:21:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 14:16:22 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 14:15:46 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 14:12:22 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 15:01:15 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-15 14:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-15 15:01:38 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-15 15:03:28 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 15:03:34 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-15 15:02:26 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:01:27 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:00:43 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:10 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:04:26 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:19 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:08:48 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:17 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:01:42 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:02:16 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:01:47 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:57 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:33 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:07:16 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:03:05 | Manampitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:05:28 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:05:57 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:02:23 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-01-15 15:04:42 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:06:39 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-01-15 14:00:19 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:05:37 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:01:31 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-15 15:07:03 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | -0.011 |  |
| 2026-01-15 15:03:29 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.012 |  |
| 2026-01-15 15:02:12 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-01-15 15:00:29 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.025 |  |
| 2026-01-15 15:05:38 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.028 |  |
| 2026-01-15 15:05:55 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-01-15 15:03:45 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.041 |  |
| 2026-01-15 15:01:32 | Weraganthota (Mahaweli Ganga) | -1.70 | 🟢 Normal | -0.050 |  |
| 2026-01-15 15:03:26 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.073 |  |
| 2026-01-15 15:00:21 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.087 |  |
| 2026-01-15 15:02:07 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -5.400 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)