# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_16:24:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 16:24:18 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:10:34 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:08:33 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-11 16:08:31 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2025-12-11 16:08:30 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:08:16 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.009 |  |
| 2025-12-11 16:08:12 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-11 16:07:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 16:07:33 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:07:01 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 16:06:38 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:06:15 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:05:58 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:05:15 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:05:13 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 16:04:55 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:04:22 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:04:21 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 16:04:15 | Horowpothana (Yan Oya) | 4.43 | 🟢 Normal | -0.066 |  |
| 2025-12-11 16:04:05 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:04:00 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:03:54 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:03:03 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:02:44 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.040 |  |
| 2025-12-11 16:02:35 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:02:10 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-11 16:01:59 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-11 16:01:57 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:01:43 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:01:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2025-12-11 16:01:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-11 16:01:34 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:00:54 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-11 16:08:33 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-11 16:08:31 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2025-12-11 16:08:12 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-11 16:02:01 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2025-12-11 16:01:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-11 16:05:13 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 15:04:23 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 16:02:10 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-11 16:00:54 | Thanthirimale (Malwathu Oya) | 4.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-11 16:04:21 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 16:07:01 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 16:07:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 16:01:34 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:02:44 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-11 15:11:23 | Moragaswewa (Deduru Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:10:34 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:06:38 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:24:18 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:02:35 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:04:55 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:03:54 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:06:15 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:07:33 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:05:58 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:01:43 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-11 16:08:16 | Panadugama (Nilwala Ganga) | 2.92 | 🟢 Normal | -0.009 |  |
| 2025-12-11 16:08:30 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:05:15 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:04:00 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:01:57 | Yaka Wewa (Ma Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:03:03 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:04:22 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:04:05 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-11 16:01:59 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-11 16:01:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.032 |  |
| 2025-12-11 16:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.040 |  |
| 2025-12-11 16:04:15 | Horowpothana (Yan Oya) | 4.43 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)