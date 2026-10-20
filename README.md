# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_23:06:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,483 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 23:06:25 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:05:52 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-10-20 23:05:49 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:05:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:05:22 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-10-20 23:05:22 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 23:04:51 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-20 23:04:32 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 23:04:30 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:04:26 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-10-20 23:04:13 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:04:07 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:04:00 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 23:04:00 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-20 23:03:58 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.013 |  |
| 2026-10-20 23:03:51 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-20 23:03:35 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:03:23 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 23:03:05 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:02:58 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-10-20 23:02:46 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 23:02:36 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.048 |  |
| 2026-10-20 23:02:21 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-10-20 23:02:01 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:01:56 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-20 23:01:44 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.020 |  |
| 2026-10-20 23:01:33 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-20 23:01:29 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:01:28 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.642 |  |
| 2026-10-20 23:00:34 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:44:25 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:25:07 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 23:02:21 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-20 23:04:51 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-20 22:03:02 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-20 23:04:00 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-20 23:01:56 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-20 23:02:46 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 23:03:23 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-20 23:04:00 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 23:04:32 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 23:05:22 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-20 23:03:05 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:01:29 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:05:49 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:05:30 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:00:34 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:04:30 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:06:25 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:04:07 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-10-20 22:12:36 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:04:13 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:03:35 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:02:01 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-20 21:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-20 23:03:51 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-20 23:01:33 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-20 23:03:58 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.013 |  |
| 2026-10-20 23:05:52 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-10-20 23:01:44 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:02:40 | Panadugama (Nilwala Ganga) | 4.32 | 🟢 Normal | -0.020 |  |
| 2026-10-20 22:18:31 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | -0.028 |  |
| 2026-10-20 23:05:22 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.029 |  |
| 2026-10-20 23:04:26 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.030 |  |
| 2026-10-20 23:02:58 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.034 |  |
| 2026-10-20 23:02:36 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.048 |  |
| 2026-10-20 22:08:09 | Thaldena (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.221 |  |
| 2026-10-20 23:01:28 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | -0.642 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)