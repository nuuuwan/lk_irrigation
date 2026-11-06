# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_21:03:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,732 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 21:03:08 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:03:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 21:02:42 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 21:02:31 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 21:02:30 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-06 21:02:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.051 |  |
| 2026-11-06 21:02:06 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-06 21:02:05 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:01:45 | Holombuwa (Kelani Ganga) | 4.66 | 🟠 Minor Flood | 0.570 | 🔺 Rising |
| 2026-11-06 21:01:44 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-06 21:01:42 | Moragaswewa (Deduru Oya) | 2.31 | 🟢 Normal | -0.051 |  |
| 2026-11-06 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.313 |  |
| 2026-11-06 21:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.162 | 🔺 Rising |
| 2026-11-06 21:01:22 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 21:01:20 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-06 21:00:59 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:00:53 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.070 |  |
| 2026-11-06 21:00:41 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 21:01:45 | Holombuwa (Kelani Ganga) | 4.66 | 🟠 Minor Flood | 0.570 | 🔺 Rising |
| 2026-11-06 21:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | 0.162 | 🔺 Rising |
| 2026-11-06 21:01:20 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-06 20:03:17 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-06 20:03:12 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-06 20:03:41 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-06 20:16:00 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-11-06 18:53:38 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-06 20:05:38 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-06 20:07:13 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-06 20:05:29 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-06 21:02:30 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-06 21:02:31 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 21:00:41 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-06 21:02:42 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 21:01:22 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 21:03:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 21:00:59 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:03:08 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:10:44 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:06:28 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:16:41 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:03:52 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:08:48 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-11-06 20:02:17 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:06:20 | Hanwella (Kelani Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:02:37 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:02:58 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2026-11-06 21:02:06 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-06 20:03:05 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-06 20:01:08 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-06 21:01:44 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-06 21:02:22 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.051 |  |
| 2026-11-06 21:01:42 | Moragaswewa (Deduru Oya) | 2.31 | 🟢 Normal | -0.051 |  |
| 2026-11-06 21:00:53 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.070 |  |
| 2026-11-06 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.313 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)