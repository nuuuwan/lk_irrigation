# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_17:12:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,800 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 17:12:13 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:10:33 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-04 17:10:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.062 |  |
| 2026-11-04 17:08:30 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-04 17:08:23 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:08:02 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:07:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:06:51 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:06:32 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-04 17:06:31 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:06:31 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:06:27 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.021 |  |
| 2026-11-04 17:06:26 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-04 17:05:52 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 17:05:44 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.079 |  |
| 2026-11-04 17:05:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:05:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-11-04 17:05:23 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.077 |  |
| 2026-11-04 17:04:50 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-11-04 17:04:40 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.051 |  |
| 2026-11-04 17:04:21 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-11-04 17:03:59 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-04 17:03:54 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:28 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:26 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 17:03:08 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:08 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 17:02:38 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-04 17:02:36 | Moragaswewa (Deduru Oya) | 4.32 | 🟢 Normal | -0.022 |  |
| 2026-11-04 17:02:34 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.060 |  |
| 2026-11-04 17:02:33 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.212 |  |
| 2026-11-04 17:02:25 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-11-04 17:02:09 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-11-04 17:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 17:01:51 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.078 |  |
| 2026-11-04 17:01:24 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 17:00:55 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:00:40 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:00:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:59:28 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 17:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.05 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 17:06:26 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-11-04 17:02:38 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-04 17:10:33 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-04 17:08:30 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-04 17:01:24 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 17:05:52 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 17:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 17:03:08 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 17:00:55 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:28 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:08:23 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:54 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:07:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:05:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:06:31 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:08 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:08:02 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:00:40 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:12:13 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:26 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:06:31 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 17:03:59 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-11-04 17:06:32 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-04 17:02:25 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-11-04 17:00:10 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-11-04 17:04:50 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-11-04 17:05:27 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-11-04 17:02:09 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.020 |  |
| 2026-11-04 17:04:21 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | -0.021 |  |
| 2026-11-04 17:06:27 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.021 |  |
| 2026-11-04 17:02:36 | Moragaswewa (Deduru Oya) | 4.32 | 🟢 Normal | -0.022 |  |
| 2026-11-04 17:04:40 | Magura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.051 |  |
| 2026-11-04 17:02:34 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | -0.060 |  |
| 2026-11-04 17:10:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.062 |  |
| 2026-11-04 17:05:23 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | -0.077 |  |
| 2026-11-04 17:01:51 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | -0.078 |  |
| 2026-11-04 17:05:44 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.079 |  |
| 2026-11-04 17:02:33 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.212 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)