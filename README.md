# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_16:18:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 16:18:19 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.017 |  |
| 2026-01-12 16:16:22 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:16:15 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:14:29 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-01-12 16:13:53 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.040 |  |
| 2026-01-12 16:12:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:09:34 | Yaka Wewa (Ma Oya) | 3.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-12 16:07:28 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.134 |  |
| 2026-01-12 16:06:47 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:06:30 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.029 |  |
| 2026-01-12 16:05:50 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:04:40 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:04:04 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:03:45 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-12 16:03:39 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 16:03:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:03:14 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.072 |  |
| 2026-01-12 16:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-01-12 16:03:06 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-01-12 16:03:01 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 16:02:48 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:45 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:33 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-12 16:02:21 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-01-12 16:02:15 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-12 16:01:55 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:01:54 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 16:01:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:01:45 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 16:01:18 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:01:17 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.053 |  |
| 2026-01-12 16:01:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:00:28 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:27 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:23 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:00:18 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 16:03:45 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-12 15:01:04 | Horowpothana (Yan Oya) | 2.69 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-12 16:09:34 | Yaka Wewa (Ma Oya) | 3.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-12 16:02:21 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 16:01:54 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 16:03:01 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 16:01:45 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 16:03:39 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 16:04:04 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:01:18 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:16:15 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:48 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:18 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:01:51 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:28 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:45 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:03:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:27 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:06:47 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 15:02:20 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:16:22 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:15 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:05:50 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:14:29 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-01-12 16:04:40 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:00:23 | Weraganthota (Mahaweli Ganga) | -1.46 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:01:08 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:12:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:03:06 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-01-12 16:18:19 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.017 |  |
| 2026-01-12 16:02:33 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-12 16:06:30 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.029 |  |
| 2026-01-12 16:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-01-12 16:13:53 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.040 |  |
| 2026-01-12 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-01-12 16:01:17 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.053 |  |
| 2026-01-12 16:03:14 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.072 |  |
| 2026-01-12 16:07:28 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)