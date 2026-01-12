# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_15:07:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,676 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 15:07:16 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-01-12 15:07:12 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-01-12 15:06:22 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:06:17 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:05:21 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:04:58 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.068 |  |
| 2026-01-12 15:04:44 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.052 |  |
| 2026-01-12 15:04:01 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 15:03:57 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:55 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 15:03:45 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 15:03:36 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:31 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:29 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-12 15:03:23 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:22 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 15:03:07 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 15:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-01-12 15:02:57 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:52 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:49 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:41 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 15:02:35 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:20 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:01:57 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:01:53 | Yaka Wewa (Ma Oya) | 3.20 | 🟢 Normal | -0.053 |  |
| 2026-01-12 15:01:49 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:01:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 15:01:41 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-01-12 15:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-12 15:01:04 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 15:00:32 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.146 |  |
| 2026-01-12 15:00:20 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 14:15:06 | Horowpothana (Yan Oya) | 2.56 | 🟢 Normal | 0.170 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 15:01:04 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 15:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-12 15:03:45 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 15:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 15:03:07 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 15:01:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 15:03:22 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 15:02:41 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 15:03:55 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 15:04:01 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 15:03:23 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:49 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:52 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:01:49 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:57 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:01:57 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:06:22 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:00:20 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:31 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:36 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:05:21 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 14:08:11 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:57 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:06:17 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:20 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:35 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:03:29 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-01-12 15:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-01-12 15:07:16 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-01-12 14:04:23 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-01-12 13:56:47 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.012 |  |
| 2026-01-12 15:07:12 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-01-12 15:01:41 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2026-01-12 15:04:44 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.052 |  |
| 2026-01-12 15:01:53 | Yaka Wewa (Ma Oya) | 3.20 | 🟢 Normal | -0.053 |  |
| 2026-01-12 14:14:50 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | -0.065 |  |
| 2026-01-12 15:04:58 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | -0.068 |  |
| 2026-01-12 14:09:10 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.092 |  |
| 2026-01-12 15:00:32 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)