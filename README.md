# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_20:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,695 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 20:03:20 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:03:17 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-06 20:03:13 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:03:12 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-06 20:03:12 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-06 20:03:05 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-06 20:02:58 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:02:18 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 20:02:17 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-06 20:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-06 20:01:44 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:01:08 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-06 20:00:39 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:00:37 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:00:14 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.162 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 19:04:14 | Holombuwa (Kelani Ganga) | 3.20 | 🟡 Alert | 0.922 | 🔺 Rising |
| 2026-11-06 20:02:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-11-06 19:05:07 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-06 19:04:19 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-06 20:03:12 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-06 20:00:14 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-06 19:05:19 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-06 20:03:17 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-06 20:03:12 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-06 20:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-06 18:53:38 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-06 19:05:16 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-06 19:05:09 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-06 20:02:18 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 19:14:34 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-06 19:05:27 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:01:44 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:20 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-06 19:08:49 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:03:20 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 19:08:52 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:00:39 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-06 19:03:39 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-06 20:00:37 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-06 19:03:42 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-06 19:07:22 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-11-06 19:08:03 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:03:13 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:02:17 | Putupaula (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:04:24 | Urawa (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:02:37 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.010 |  |
| 2026-11-06 20:02:58 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2026-11-06 19:07:31 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-06 20:03:05 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | -0.021 |  |
| 2026-11-06 20:01:08 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-11-06 19:07:14 | Moragaswewa (Deduru Oya) | 2.39 | 🟢 Normal | -0.037 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)