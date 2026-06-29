# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_23:26:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 23:26:31 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 23:15:29 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-29 23:11:52 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-06-29 23:09:38 | Rathnapura (Kalu Ganga) | 5.50 | 🟡 Alert | -0.118 |  |
| 2026-06-29 23:07:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 23:06:29 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.042 |  |
| 2026-06-29 23:06:17 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.015 |  |
| 2026-06-29 23:06:10 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:05:42 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.138 |  |
| 2026-06-29 23:05:32 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:04:45 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:04:18 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.033 |  |
| 2026-06-29 23:03:49 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:03:33 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-29 23:03:30 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-06-29 23:03:05 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:02:55 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 23:02:43 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-29 23:02:34 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-06-29 23:02:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:02:22 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-06-29 23:02:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:02:16 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 23:02:09 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-06-29 23:02:02 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-29 23:01:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:20 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-29 23:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-06-29 23:01:06 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:00:46 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:00:44 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-06-29 23:00:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 23:09:38 | Rathnapura (Kalu Ganga) | 5.50 | 🟡 Alert | -0.118 |  |
| 2026-06-29 23:02:16 | Peradeniya (Mahaweli Ganga) | 3.28 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 23:02:55 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-29 23:01:20 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-29 23:03:33 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-29 23:02:43 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-29 23:07:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-29 23:26:31 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-29 23:15:29 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-29 23:03:49 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:03:53 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:02:23 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:00:44 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:06 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:00:46 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:04:05 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:03:05 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:04:45 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:00:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:02:16 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:05:32 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:01:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-29 18:02:06 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:06:10 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 23:11:52 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-06-29 23:02:02 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-29 23:01:14 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-06-29 23:06:17 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.015 |  |
| 2026-06-29 23:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-06-29 23:03:30 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-06-29 23:02:22 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-06-29 22:07:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-06-29 23:04:18 | Panadugama (Nilwala Ganga) | 4.28 | 🟢 Normal | -0.033 |  |
| 2026-06-29 23:06:29 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | -0.042 |  |
| 2026-06-29 23:02:34 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-06-29 23:02:09 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.069 |  |
| 2026-06-29 23:05:42 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)