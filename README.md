# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_06:10:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 06:10:19 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-11-20 06:09:32 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 06:08:46 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:07:10 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:07:01 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-11-20 06:05:04 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:05:03 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-20 06:05:00 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:04:49 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:04:24 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:04:13 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.020 |  |
| 2026-11-20 06:04:12 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-20 06:03:51 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-11-20 06:03:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-11-20 06:03:02 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:02:55 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.032 |  |
| 2026-11-20 06:02:42 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:27 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:02:19 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:07 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:01 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:01:51 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-20 06:01:35 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 06:01:17 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:01:16 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-20 06:01:11 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-11-20 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:01:07 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.081 |  |
| 2026-11-20 06:01:05 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.001 |  |
| 2026-11-20 06:01:02 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:00:56 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-20 06:00:36 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:00:35 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 05:50:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.13 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-20 05:41:14 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 06:05:03 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-11-20 06:01:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.16 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-20 06:04:12 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-20 06:00:35 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 06:01:35 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 06:01:16 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-20 06:09:32 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 06:01:05 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.001 |  |
| 2026-11-20 06:01:51 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:01 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:01:17 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:07:10 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:08:46 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:07 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:42 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:02:19 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:04:24 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:01:52 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:00:36 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 06:10:19 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-11-19 18:05:17 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-20 06:05:00 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:03:02 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:01:02 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:02:27 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:04:49 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:05:04 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.010 |  |
| 2026-11-20 06:03:51 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.011 |  |
| 2026-11-20 06:01:11 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-11-20 06:07:01 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-11-20 06:04:13 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.020 |  |
| 2026-11-20 06:00:56 | Moraketiya (Walawe Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-20 06:02:55 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.032 |  |
| 2026-11-20 06:03:10 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.060 |  |
| 2026-11-20 06:01:07 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.081 |  |
| 2026-11-20 05:22:26 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -1.125 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)