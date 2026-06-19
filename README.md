# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_07:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,376 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 07:10:15 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:09:32 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 07:08:49 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-19 07:08:14 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-19 07:07:45 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:07:42 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:06:17 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:06:02 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:05:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-06-19 07:05:52 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:05:19 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 07:04:50 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:04:34 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2026-06-19 07:04:24 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:04:04 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-06-19 07:03:55 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:03:43 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:03:43 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.042 |  |
| 2026-06-19 07:03:08 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:41 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:37 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:36 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-19 07:02:09 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:08 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:01:50 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:01:42 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 07:01:03 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:49 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:37 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:25 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 07:00:22 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:00:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:11 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 06:56:39 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 06:30:41 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 07:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-19 07:08:49 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-19 07:01:42 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 07:09:32 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 07:05:19 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-19 07:08:14 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-19 07:00:25 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 07:00:37 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:11 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:08 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:44 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 06:04:32 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:03:08 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:46 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:01:50 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:41 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:05:52 | Hanwella (Kelani Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:03:55 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:10:15 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:37 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:04:24 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:06:17 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:03:43 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:01:03 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:07:45 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:00:49 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:02:09 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-19 07:07:42 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:06:02 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:02:36 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:04:50 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:00:22 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-06-19 07:04:34 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2026-06-19 06:05:29 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-06-19 07:04:04 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.041 |  |
| 2026-06-19 07:03:43 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.042 |  |
| 2026-06-19 07:05:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-06-19 06:04:30 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)