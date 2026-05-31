# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_05:28:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,308 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 05:28:13 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.015 |  |
| 2026-05-31 05:21:37 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.189 |  |
| 2026-05-31 05:20:10 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:17:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2026-05-31 05:14:09 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:14:05 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.035 |  |
| 2026-05-31 05:12:06 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.189 |  |
| 2026-05-31 05:11:16 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-31 05:08:28 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.161 |  |
| 2026-05-31 05:08:01 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-31 05:07:37 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:06:13 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.005 |  |
| 2026-05-31 05:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.67 | 🟡 Alert | -0.168 |  |
| 2026-05-31 05:05:31 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:04:09 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:03:47 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:57 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:38 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-31 05:02:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:25 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 05:02:22 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -1.636 |  |
| 2026-05-31 05:02:19 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.039 |  |
| 2026-05-31 05:02:19 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-31 05:02:16 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.033 |  |
| 2026-05-31 05:02:07 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:00 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -1.636 |  |
| 2026-05-31 05:01:59 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 05:01:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:01:11 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:00:47 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:00:18 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:49:19 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.189 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 05:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.67 | 🟡 Alert | -0.168 |  |
| 2026-05-31 05:02:19 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-31 05:02:38 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-31 05:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-31 05:02:25 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 05:08:01 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-31 05:07:37 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:00:56 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:00:47 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:01:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:07 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:14:09 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:05:31 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:00:51 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-31 03:10:43 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:03:47 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:04:09 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:02:57 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-31 04:04:51 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:01:11 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:20:10 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 18:03:31 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:00:18 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-31 05:06:13 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.005 |  |
| 2026-05-31 05:11:16 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-31 05:28:13 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.015 |  |
| 2026-05-31 04:11:39 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | -0.018 |  |
| 2026-05-31 05:02:16 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.033 |  |
| 2026-05-31 05:14:05 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.035 |  |
| 2026-05-31 05:02:19 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.039 |  |
| 2026-05-31 04:01:24 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | -0.041 |  |
| 2026-05-31 05:17:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2026-05-31 04:03:40 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.052 |  |
| 2026-05-31 04:12:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.085 |  |
| 2026-05-31 05:08:28 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.161 |  |
| 2026-05-31 05:21:37 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.189 |  |
| 2026-05-31 05:02:22 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -1.636 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)