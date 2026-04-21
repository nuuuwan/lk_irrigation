# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_00:27:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,505 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 00:27:10 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-22 00:13:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-22 00:10:09 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-22 00:09:30 | Thanamalwila (Kirindi Oya) | 3.41 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-04-22 00:08:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:08:11 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-04-22 00:07:38 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-04-22 00:07:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:06:29 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.053 |  |
| 2026-04-22 00:05:38 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-22 00:05:33 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-04-22 00:04:45 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:04:31 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -684.000 |  |
| 2026-04-22 00:04:30 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -684.000 |  |
| 2026-04-22 00:04:26 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-22 00:04:19 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-22 00:04:03 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -2.483 |  |
| 2026-04-22 00:03:43 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-22 00:03:34 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -2.483 |  |
| 2026-04-22 00:03:33 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.039 |  |
| 2026-04-22 00:03:04 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-22 00:02:47 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:02:45 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-22 00:02:34 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 00:02:08 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.139 |  |
| 2026-04-22 00:02:08 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.103 |  |
| 2026-04-22 00:02:07 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.056 |  |
| 2026-04-22 00:01:56 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 00:01:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:01:36 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 00:01:32 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 00:01:15 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-04-22 00:00:45 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.066 |  |
| 2026-04-21 23:58:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:46:10 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 00:09:30 | Thanamalwila (Kirindi Oya) | 3.41 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-04-22 00:05:38 | Peradeniya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-22 00:04:26 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-22 00:01:32 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 00:13:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-04-22 00:02:45 | Moraketiya (Walawe Ganga) | 1.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-22 00:01:56 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-22 00:03:43 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-22 00:27:10 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-22 00:10:09 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 00:02:34 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 00:01:36 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 23:01:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 00:01:36 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:58:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:04:45 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:08:31 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:02:47 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:07:00 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 00:03:04 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-21 23:11:06 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-04-22 00:04:19 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-21 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-04-22 00:07:38 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-04-22 00:03:33 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.039 |  |
| 2026-04-22 00:06:29 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.053 |  |
| 2026-04-22 00:02:07 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | -0.056 |  |
| 2026-04-22 00:05:33 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-04-22 00:01:15 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-04-22 00:00:45 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.066 |  |
| 2026-04-22 00:08:11 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-04-22 00:02:08 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.103 |  |
| 2026-04-22 00:02:08 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.139 |  |
| 2026-04-21 23:01:20 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -2.043 |  |
| 2026-04-22 00:04:03 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -2.483 |  |
| 2026-04-22 00:04:31 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -684.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)