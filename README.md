# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_22:02:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 22:02:58 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-06 22:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-06 22:02:37 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.011 |  |
| 2026-11-06 22:02:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-06 22:02:07 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:01:38 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:00:53 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-11-06 22:00:30 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.592 | 🔺 Rising |
| 2026-11-06 21:29:42 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 21:01:45 | Holombuwa (Kelani Ganga) | 4.66 | 🟠 Minor Flood | 0.570 | 🔺 Rising |
| 2026-11-06 22:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-06 21:04:37 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-11-06 22:00:30 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.592 | 🔺 Rising |
| 2026-11-06 21:01:20 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-11-06 21:06:07 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-11-06 21:07:26 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-11-06 22:02:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-06 21:05:06 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-06 21:11:56 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-06 21:02:30 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-06 22:02:58 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-06 21:02:31 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 21:00:41 | Moraketiya (Walawe Ganga) | 1.82 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-06 21:02:42 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 21:04:42 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-06 21:01:22 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-06 21:03:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 22:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:03:08 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:07:16 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:06:14 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:01:38 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:06:09 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:03:26 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-06 22:02:07 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-06 21:08:34 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-11-06 21:06:00 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-06 22:02:37 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.011 |  |
| 2026-11-06 21:06:04 | Panadugama (Nilwala Ganga) | 3.81 | 🟢 Normal | -0.012 |  |
| 2026-11-06 21:02:06 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-06 22:00:53 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-11-06 21:03:25 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-06 21:01:44 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-11-06 21:01:42 | Moragaswewa (Deduru Oya) | 2.31 | 🟢 Normal | -0.051 |  |
| 2026-11-06 21:01:34 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.313 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)