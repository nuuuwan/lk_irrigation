# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_18:25:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,400 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 18:25:14 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:24:38 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:20:28 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.016 |  |
| 2026-05-08 18:18:04 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-08 18:13:01 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:09:52 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-05-08 18:08:16 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:07:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:07:01 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:06:03 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-08 18:05:43 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-05-08 18:05:41 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:05:40 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-08 18:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 18:04:15 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 18:04:07 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:03:27 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-05-08 18:03:16 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-08 18:03:14 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-08 18:03:01 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:02:56 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-08 18:02:50 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-08 18:02:42 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-05-08 18:02:40 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.090 |  |
| 2026-05-08 18:02:36 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:02:35 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-05-08 18:02:30 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.071 |  |
| 2026-05-08 18:02:28 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 18:02:25 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.058 |  |
| 2026-05-08 18:01:51 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-08 18:01:51 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.051 |  |
| 2026-05-08 18:01:47 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 18:01:22 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 18:01:18 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-05-08 18:01:16 | Wellawaya (Kirindi Oya) | 5.35 | 🟡 Alert | 3.919 | 🔺 Rising |
| 2026-05-08 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.183 |  |
| 2026-05-08 18:00:59 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-08 18:00:12 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.074 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 18:01:16 | Wellawaya (Kirindi Oya) | 5.35 | 🟡 Alert | 3.919 | 🔺 Rising |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-08 18:02:35 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-05-08 18:01:22 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-08 18:03:27 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-05-08 18:01:18 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-05-08 18:00:59 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-05-08 18:01:51 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-08 18:04:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.62 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-08 18:06:03 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-08 18:02:56 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-08 18:00:12 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-08 18:05:40 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-05-08 18:02:28 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 18:03:14 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-08 18:04:15 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-08 18:25:14 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:24:38 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:04:07 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:03:01 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:08:16 | Holombuwa (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:13:01 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-05-08 18:05:43 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-05-08 18:03:16 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-08 18:01:47 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-05-08 18:02:50 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-08 18:20:28 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.016 |  |
| 2026-05-08 18:02:42 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-05-08 18:18:04 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.023 |  |
| 2026-05-08 18:02:36 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:07:43 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-05-08 18:09:52 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.032 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-08 18:01:51 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.051 |  |
| 2026-05-08 18:02:25 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.058 |  |
| 2026-05-08 18:02:30 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.071 |  |
| 2026-05-08 18:02:40 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | -0.090 |  |
| 2026-05-08 18:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)