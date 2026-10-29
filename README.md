# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_04:29:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 04:29:30 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:22:23 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-10-30 04:20:41 | Putupaula (Kalu Ganga) | 3.60 | 🟡 Alert | -0.009 |  |
| 2026-10-30 04:17:54 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.008 |  |
| 2026-10-30 04:12:58 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-30 04:12:25 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.070 |  |
| 2026-10-30 04:12:16 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-10-30 04:08:42 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-10-30 04:08:00 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:06:51 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.013 |  |
| 2026-10-30 04:06:07 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-30 04:05:55 | Ellagawa (Kalu Ganga) | 9.25 | 🟢 Normal | -0.160 |  |
| 2026-10-30 04:05:52 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-30 04:04:52 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.021 |  |
| 2026-10-30 04:03:37 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:03:27 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.029 |  |
| 2026-10-30 04:02:54 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:02:46 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:02:42 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:02:35 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-10-30 04:02:33 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:02:31 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:02:16 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 04:01:59 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.019 |  |
| 2026-10-30 04:01:46 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-30 04:00:29 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:00:28 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 04:00:25 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.021 |  |
| 2026-10-30 04:00:24 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 04:00:28 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 03:11:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.90 | 🟠 Minor Flood | -0.032 |  |
| 2026-10-30 04:20:41 | Putupaula (Kalu Ganga) | 3.60 | 🟡 Alert | -0.009 |  |
| 2026-10-30 04:06:51 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | -0.013 |  |
| 2026-10-30 03:09:51 | Baddegama (Gin Ganga) | 3.71 | 🟡 Alert | -0.027 |  |
| 2026-10-29 18:05:01 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-30 04:01:46 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-10-30 04:12:58 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-30 04:05:52 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-30 04:02:16 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 04:02:31 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:29:30 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:01:32 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 03:18:15 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:03:37 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:02:33 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:00:29 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-30 04:22:23 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-10-30 04:17:54 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.008 |  |
| 2026-10-30 04:02:46 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:02:54 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:02:42 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:08:00 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 04:12:16 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2026-10-30 04:00:24 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.011 |  |
| 2026-10-30 03:24:42 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.014 |  |
| 2026-10-30 03:07:22 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-10-30 04:06:07 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-30 04:01:59 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | -0.019 |  |
| 2026-10-30 04:04:52 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.021 |  |
| 2026-10-30 04:00:25 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.021 |  |
| 2026-10-30 04:08:42 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-10-30 04:03:27 | Glencourse (Kelani Ganga) | 10.99 | 🟢 Normal | -0.029 |  |
| 2026-10-30 04:02:35 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-30 04:12:25 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.070 |  |
| 2026-10-30 03:02:39 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.084 |  |
| 2026-10-30 04:05:55 | Ellagawa (Kalu Ganga) | 9.25 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)