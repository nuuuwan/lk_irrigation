# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_12:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,449 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 12:11:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 12:10:54 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-01-13 12:10:17 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-01-13 12:10:03 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:09:07 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-01-13 12:08:34 | Horowpothana (Yan Oya) | 3.79 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 12:08:21 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-13 12:06:33 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:06:16 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:06:04 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:05:03 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:04:42 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-01-13 12:04:17 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.043 |  |
| 2026-01-13 12:04:10 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:04:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:04:08 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 12:03:56 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-01-13 12:03:49 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-01-13 12:03:26 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:02:47 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 12:02:45 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 12:02:06 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:02:04 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:02:03 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.039 |  |
| 2026-01-13 12:01:52 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 12:01:32 | Weraganthota (Mahaweli Ganga) | -1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:01:32 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:28 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:22 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.158 |  |
| 2026-01-13 12:01:20 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:17 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:38 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:31 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:21 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:19 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:00:13 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 12:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-13 12:02:47 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 12:02:45 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-13 12:08:34 | Horowpothana (Yan Oya) | 3.79 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 12:11:50 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-13 12:01:17 | Thanthirimale (Malwathu Oya) | 2.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 12:01:52 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 12:04:08 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 12:02:06 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:02:04 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:04:10 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:24 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:32 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 11:04:13 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:06:04 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:06:16 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:38 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:13 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:21 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:01:20 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:10:03 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:03:26 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:00:31 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 12:10:54 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.008 |  |
| 2026-01-13 12:01:32 | Weraganthota (Mahaweli Ganga) | -1.44 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:05:03 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:01:28 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:06:33 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:00:19 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-13 12:09:07 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.019 |  |
| 2026-01-13 12:03:49 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-01-13 12:08:21 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-13 12:03:56 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.029 |  |
| 2026-01-13 12:04:42 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-01-13 12:10:17 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.031 |  |
| 2026-01-13 12:02:03 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.039 |  |
| 2026-01-13 12:04:17 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.043 |  |
| 2026-01-13 12:01:22 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)