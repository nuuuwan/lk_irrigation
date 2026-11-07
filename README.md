# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_18:24:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 18:24:38 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 18:24:37 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:17:00 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:13:56 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:09:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.058 |  |
| 2026-11-07 18:07:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.092 |  |
| 2026-11-07 18:06:28 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-11-07 18:06:09 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 18:05:51 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.011 |  |
| 2026-11-07 18:05:30 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:04:41 | Dunamale (Aththanagalu Oya) | 3.56 | 🟡 Alert | -0.019 |  |
| 2026-11-07 18:04:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.088 |  |
| 2026-11-07 18:04:07 | Urawa (Nilwala Ganga) | 2.35 | 🟢 Normal | 1.186 | 🔺 Rising |
| 2026-11-07 18:04:03 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:44 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-07 18:03:28 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:04 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.074 |  |
| 2026-11-07 18:03:01 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:02:53 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:02:52 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-07 18:02:46 | Wellawaya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-11-07 18:02:46 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-07 18:02:45 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:02:36 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | -0.050 |  |
| 2026-11-07 18:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.040 |  |
| 2026-11-07 18:02:19 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.012 |  |
| 2026-11-07 18:02:15 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-07 18:02:07 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:02:04 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-07 18:01:54 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:30 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.121 |  |
| 2026-11-07 18:01:18 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 18:01:16 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:00:56 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 18:04:41 | Dunamale (Aththanagalu Oya) | 3.56 | 🟡 Alert | -0.019 |  |
| 2026-11-07 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | -0.040 |  |
| 2026-11-07 18:04:07 | Urawa (Nilwala Ganga) | 2.35 | 🟢 Normal | 1.186 | 🔺 Rising |
| 2026-11-07 18:02:46 | Wellawaya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-11-07 18:02:46 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-07 18:03:28 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-07 18:03:44 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-07 18:02:52 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-11-07 18:02:15 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-07 18:06:09 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 18:24:38 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-07 18:01:18 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 18:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 18:01:54 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:04:03 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:17:00 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:24:37 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:02:07 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:00:56 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:13:56 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:30 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:03:01 | Ellagawa (Kalu Ganga) | 6.11 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:02:45 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:02:53 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:05:51 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.011 |  |
| 2026-11-07 18:02:19 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | -0.012 |  |
| 2026-11-07 18:05:30 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:01:16 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:02:04 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-07 18:06:28 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-11-07 18:02:36 | Putupaula (Kalu Ganga) | 1.48 | 🟢 Normal | -0.050 |  |
| 2026-11-07 18:09:15 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.058 |  |
| 2026-11-07 18:03:04 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | -0.074 |  |
| 2026-11-07 18:04:15 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.088 |  |
| 2026-11-07 18:07:35 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.092 |  |
| 2026-11-07 18:01:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.121 |  |

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)