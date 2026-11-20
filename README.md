# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_10:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 10:03:17 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:06 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 10:03:03 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:03 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:03:01 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-11-20 10:02:53 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 10:02:43 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:02:43 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:39 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-11-20 10:02:30 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:18 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-11-20 10:01:55 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-11-20 10:01:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:27 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:24 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:01:20 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:00:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-20 10:00:53 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:24:40 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 10:03:01 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-11-20 10:02:53 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 09:01:21 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-20 10:03:06 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-20 09:03:14 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 10:00:53 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:20 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:01:30 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:02:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:27 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:02:58 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:04:55 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:17 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:30 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:02:43 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:07:30 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:03:41 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:07 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:01:49 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:07:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:10:10 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 10:03:03 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:03:01 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:07:28 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:24:40 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-20 09:16:03 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-11-20 09:04:29 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:01:24 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-20 09:06:39 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:03:03 | Hanwella (Kelani Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-11-20 10:02:43 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-20 09:02:55 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.011 |  |
| 2026-11-20 10:02:18 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-11-20 09:04:23 | Glencourse (Kelani Ganga) | 9.54 | 🟢 Normal | -0.011 |  |
| 2026-11-20 10:00:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-11-20 10:01:55 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-11-20 09:05:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)