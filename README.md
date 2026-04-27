# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_03:42:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,963 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 03:42:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-04-28 03:42:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-04-28 03:18:19 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -6.207 |  |
| 2026-04-28 03:17:50 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -6.207 |  |
| 2026-04-28 03:14:14 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-04-28 03:10:37 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-04-28 03:10:13 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-28 03:09:04 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-28 03:08:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:06:21 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-28 03:06:02 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-04-28 03:05:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.057 |  |
| 2026-04-28 03:05:33 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:05:22 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-04-28 03:04:52 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 03:04:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 03:04:20 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-28 03:04:19 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:04:05 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-04-28 03:03:55 | Kithulgala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:03:49 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:40 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:36 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:27 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:27 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-28 03:02:22 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -0.039 |  |
| 2026-04-28 03:02:20 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:02:10 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:20 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 03:01:12 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2026-04-28 03:01:08 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.123 |  |
| 2026-04-28 03:00:49 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 03:42:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-04-28 03:05:22 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.556 | 🔺 Rising |
| 2026-04-28 03:06:02 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.348 | 🔺 Rising |
| 2026-04-28 03:09:04 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-04-28 03:10:37 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-04-28 03:04:52 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-28 03:06:21 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-28 03:00:49 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-28 03:02:27 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-28 03:01:20 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-28 03:04:41 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 03:04:20 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 18:05:30 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:12 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:08:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:10 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:36 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:04:19 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:03:49 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:27 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:02:40 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-27 18:03:04 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-28 01:06:19 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-28 03:10:13 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.009 |  |
| 2026-04-28 02:05:46 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-28 02:02:20 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:05:33 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:02:20 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:03:55 | Kithulgala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-28 03:04:05 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-04-28 03:02:22 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | -0.039 |  |
| 2026-04-28 03:14:14 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.042 |  |
| 2026-04-28 03:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.043 |  |
| 2026-04-28 03:05:48 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.057 |  |
| 2026-04-28 01:03:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-04-28 03:01:08 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.123 |  |
| 2026-04-28 03:18:19 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -6.207 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)