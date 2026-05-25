# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_12:13:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 12:13:31 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:11:46 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-25 12:09:39 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.095 |  |
| 2026-05-25 12:08:57 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-05-25 12:07:36 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:07:17 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-25 12:07:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:05:47 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:04:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 12:04:47 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.056 |  |
| 2026-05-25 12:04:45 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-25 12:04:44 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:04:13 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-05-25 12:04:05 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | -0.104 |  |
| 2026-05-25 12:03:46 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:03:27 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:03:25 | Hanwella (Kelani Ganga) | 4.85 | 🟢 Normal | -0.074 |  |
| 2026-05-25 12:03:00 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:02:55 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.058 |  |
| 2026-05-25 12:02:50 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:02:44 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:02:26 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:02:18 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | -0.040 |  |
| 2026-05-25 12:02:11 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-25 12:02:04 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:58 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:54 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:47 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:25 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:01:25 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:23 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | -0.020 |  |
| 2026-05-25 12:01:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:15 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:07 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 12:00:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:00:35 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:00:10 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-25 11:58:12 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 12:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | -0.040 |  |
| 2026-05-25 12:02:11 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-25 12:04:45 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-25 12:04:49 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 12:01:07 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-25 12:07:17 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-25 12:11:46 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-25 12:01:15 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:00:35 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:16 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:00:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:03:46 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:47 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:07:36 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:54 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:13:31 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:01:58 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:03:00 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:02:04 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:02:18 | Peradeniya (Mahaweli Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:04:44 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:05:47 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:02:50 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 12:07:13 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:03:27 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:01:25 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:02:44 | Putupaula (Kalu Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:00:10 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-25 12:02:26 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-05-25 11:58:12 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-05-25 12:01:23 | Ellagawa (Kalu Ganga) | 9.00 | 🟢 Normal | -0.020 |  |
| 2026-05-25 12:04:13 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.031 |  |
| 2026-05-25 12:08:57 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-05-25 12:04:47 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.056 |  |
| 2026-05-25 12:02:55 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.058 |  |
| 2026-05-25 12:03:25 | Hanwella (Kelani Ganga) | 4.85 | 🟢 Normal | -0.074 |  |
| 2026-05-25 12:09:39 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.095 |  |
| 2026-05-25 12:04:05 | Rathnapura (Kalu Ganga) | 4.08 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)