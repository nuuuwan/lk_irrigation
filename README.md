# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_16:20:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 16:20:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:17:35 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 16:11:45 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-21 16:09:02 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-06-21 16:08:46 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:08:29 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.066 |  |
| 2026-06-21 16:07:56 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.018 |  |
| 2026-06-21 16:07:49 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:07:48 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.018 |  |
| 2026-06-21 16:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:06:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-21 16:06:12 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.023 |  |
| 2026-06-21 16:06:02 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:27 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:05 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:04:58 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:04:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-21 16:04:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 16:04:08 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:04:07 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:03:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:03:17 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-06-21 16:02:58 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:02:47 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:02:24 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 3.018 | 🔺 Rising |
| 2026-06-21 16:02:14 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 16:02:00 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 16:01:42 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:27 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:25 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:15 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.212 |  |
| 2026-06-21 16:01:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-21 16:00:54 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-21 16:00:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:00:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 16:02:24 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 3.018 | 🔺 Rising |
| 2026-06-21 16:11:45 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-21 16:01:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-21 16:06:52 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-21 16:04:45 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-21 16:02:14 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 16:02:00 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 16:17:35 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 16:04:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 16:07:49 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:27 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:00:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:17 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:42 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:04:58 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:05 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:02:58 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:32 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:00:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:05:24 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:06:02 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:20:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:02:47 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:01:27 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:07:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-06-21 16:08:46 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:04:08 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:04:07 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:03:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-21 16:09:02 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.011 |  |
| 2026-06-21 16:07:48 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.018 |  |
| 2026-06-21 16:07:56 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.018 |  |
| 2026-06-21 16:00:54 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.020 |  |
| 2026-06-21 16:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-06-21 16:06:12 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.023 |  |
| 2026-06-21 16:03:17 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | -0.030 |  |
| 2026-06-21 16:08:29 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.066 |  |
| 2026-06-21 16:01:15 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)