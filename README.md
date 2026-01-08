# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_08:06:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 08:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-01-08 08:06:20 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:06:02 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 08:06:00 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:05:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.244 |  |
| 2026-01-08 08:04:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-08 08:04:25 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:23 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:18 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-01-08 08:03:52 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:03:50 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-08 08:03:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-08 08:03:44 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-01-08 08:03:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-08 08:03:25 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:53 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:46 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:02:46 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.120 |  |
| 2026-01-08 08:02:36 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 08:02:26 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:10 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:01:54 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:01:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-01-08 08:00:55 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-01-08 08:00:40 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-01-08 07:55:15 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.244 |  |
| 2026-01-08 07:45:49 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-01-08 07:22:12 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:21:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.007 |  |
| 2026-01-08 07:17:55 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:15:54 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.036 |  |
| 2026-01-08 07:15:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:11:58 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.012 |  |
| 2026-01-08 07:11:34 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-08 07:11:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-01-08 07:10:24 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 07:09:46 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:08:44 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 08:00:40 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-01-08 08:03:50 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-08 08:04:38 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-08 08:03:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-08 08:03:48 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-08 08:02:36 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 07:04:33 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 08:06:02 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 08:02:26 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:01:54 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:03:25 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:09 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:06:20 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:22:12 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:03:52 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:05:30 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:25 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:53 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:04:23 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 08:02:10 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:21:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.007 |  |
| 2026-01-08 08:06:00 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.009 |  |
| 2026-01-08 08:02:46 | Horowpothana (Yan Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:07:02 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:04:18 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:04:00 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-08 08:00:55 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-01-08 08:04:00 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.012 |  |
| 2026-01-08 07:09:46 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:15:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-01-08 08:03:44 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.020 |  |
| 2026-01-08 07:02:10 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.032 |  |
| 2026-01-08 07:15:54 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.036 |  |
| 2026-01-08 07:11:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-01-08 08:06:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-01-08 07:00:56 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.077 |  |
| 2026-01-08 08:01:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.094 |  |
| 2026-01-08 08:02:46 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.120 |  |
| 2026-01-08 08:05:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.244 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)