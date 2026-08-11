# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--11_23:03:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,938 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 23:03:23 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.030 |  |
| 2026-08-11 23:03:16 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-08-11 23:02:54 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-08-11 23:02:50 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-11 23:02:26 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.042 |  |
| 2026-08-11 23:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:18 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:08 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:01:58 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 23:01:50 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.020 |  |
| 2026-08-11 23:01:40 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 23:01:01 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:00:49 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:00:49 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-11 22:05:16 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.489 | 🔺 Rising |
| 2026-08-11 22:06:02 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-11 23:02:50 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-11 22:04:27 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-11 22:07:02 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-11 23:01:58 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-11 23:01:40 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 23:00:49 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-11 23:00:49 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:03:48 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:03:36 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:01:01 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:11:53 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:03:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:08 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-11 23:02:18 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:05:35 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:05:23 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:03:39 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-11 21:10:07 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:09:41 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-11 22:06:26 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-08-11 23:02:54 | Hanwella (Kelani Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-08-11 22:04:08 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.011 |  |
| 2026-08-11 22:03:26 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.011 |  |
| 2026-08-11 22:01:37 | Peradeniya (Mahaweli Ganga) | 3.38 | 🟢 Normal | -0.011 |  |
| 2026-08-11 22:07:02 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.018 |  |
| 2026-08-11 23:01:50 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | -0.020 |  |
| 2026-08-11 23:03:16 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-08-11 23:03:23 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.030 |  |
| 2026-08-11 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.031 |  |
| 2026-08-11 23:02:26 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | -0.042 |  |
| 2026-08-11 22:11:02 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.049 |  |
| 2026-08-11 22:04:32 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)