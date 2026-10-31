# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_20:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 20:02:52 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:02:52 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-10-31 20:02:46 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.061 |  |
| 2026-10-31 20:02:43 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:36 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-31 20:02:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.148 |  |
| 2026-10-31 20:02:16 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-31 20:02:10 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-10-31 20:01:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:00:53 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-31 19:32:37 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 20:02:36 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-31 19:05:03 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-31 19:03:23 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-31 20:02:16 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-31 19:04:05 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 19:01:16 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-31 19:02:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 20:01:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:36 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:02:03 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:01:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:43 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-10-31 20:02:10 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:32:37 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-31 19:17:15 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.008 |  |
| 2026-10-31 19:03:56 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:00:53 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-31 19:08:47 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-10-31 19:06:10 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 19:05:37 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:02:52 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-31 20:02:52 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-31 19:13:57 | Magura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.017 |  |
| 2026-10-31 19:09:00 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.018 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-31 20:01:12 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.021 |  |
| 2026-10-31 19:01:36 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.031 |  |
| 2026-10-31 19:03:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.033 |  |
| 2026-10-31 19:05:16 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-10-31 19:03:07 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | -0.045 |  |
| 2026-10-31 19:05:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.37 | 🟢 Normal | -0.049 |  |
| 2026-10-31 19:03:16 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.059 |  |
| 2026-10-31 20:02:46 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.061 |  |
| 2026-10-31 18:59:17 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | -0.070 |  |
| 2026-10-31 19:08:05 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.072 |  |
| 2026-10-31 20:02:19 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)