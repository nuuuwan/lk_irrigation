# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_19:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,550 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 19:03:07 | Dunamale (Aththanagalu Oya) | 3.55 | 🟡 Alert | 0.000 |  |
| 2026-11-07 19:03:05 | Dunamale (Aththanagalu Oya) | 3.55 | 🟡 Alert | 0.000 |  |
| 2026-11-07 19:02:56 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:02:45 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:02:13 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 19:02:12 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-11-07 19:02:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:02:06 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:02:00 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 19:01:57 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:01:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-11-07 19:01:30 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-07 19:00:56 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:00:14 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:24:38 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 18:24:37 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 19:03:07 | Dunamale (Aththanagalu Oya) | 3.55 | 🟡 Alert | 0.000 |  |
| 2026-11-07 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.040 |  |
| 2026-11-07 18:04:07 | Urawa (Nilwala Ganga) | 2.35 | 🟢 Normal | 1.186 | 🔺 Rising |
| 2026-11-07 18:02:46 | Wellawaya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-11-07 18:02:46 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-07 18:03:28 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-07 19:01:30 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-07 18:02:52 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-07 19:02:00 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 18:02:15 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-07 19:02:13 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 18:06:09 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 18:24:38 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 18:01:18 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 18:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 19:02:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:04:03 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:17:00 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:24:37 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:02:07 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:13:56 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:02:06 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:01:57 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-07 19:02:45 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:02:45 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:00:14 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:02:56 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-07 19:00:56 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:05:51 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.011 |  |
| 2026-11-07 18:05:30 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:02:04 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-07 18:06:28 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-11-07 18:02:36 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | -0.050 |  |
| 2026-11-07 19:02:12 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.057 |  |
| 2026-11-07 19:01:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-11-07 18:07:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)