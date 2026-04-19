# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_05:10:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 05:10:51 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.045 |  |
| 2026-04-20 05:10:42 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-20 05:10:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-04-20 05:10:34 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-04-20 05:08:42 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-04-20 05:08:14 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:07:35 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:06:05 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:05:56 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-20 05:05:48 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:04:58 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.009 |  |
| 2026-04-20 05:04:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:04:27 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-20 05:03:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-20 05:03:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:02:45 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:02:42 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 05:02:11 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:01:57 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-20 05:01:52 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-04-20 05:01:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:01:36 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-04-20 05:01:05 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:00:37 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.113 |  |
| 2026-04-20 04:35:04 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-20 04:25:06 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:20:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 04:10:44 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-20 03:03:59 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-20 05:10:34 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-04-20 05:01:57 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-20 05:01:52 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-20 05:05:56 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-20 05:03:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-20 04:20:33 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 04:05:30 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-20 05:02:42 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-20 04:07:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-20 05:10:42 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-20 05:06:05 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:01:05 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:01:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:03:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:08:14 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:05:48 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:07:35 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:02:11 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:04:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 04:16:26 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:02:45 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-20 05:08:42 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.009 |  |
| 2026-04-20 05:04:58 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | -0.009 |  |
| 2026-04-20 05:04:27 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-20 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-04-20 04:00:48 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-04-20 05:10:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-04-20 04:01:21 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-04-20 05:10:51 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.045 |  |
| 2026-04-20 04:05:50 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.063 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-20 04:00:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | -0.084 |  |
| 2026-04-20 05:00:37 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.113 |  |
| 2026-04-20 04:08:32 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.357 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)