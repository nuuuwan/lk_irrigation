# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_21:02:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 21:02:43 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:35 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:32 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-15 21:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:18 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:02:12 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.023 |  |
| 2026-11-15 21:02:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:02 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 21:02:01 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.022 |  |
| 2026-11-15 21:01:56 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-15 21:01:34 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:29 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:01:16 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:16 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 21:01:56 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-15 19:13:52 | Panadugama (Nilwala Ganga) | 5.69 | 🟡 Alert | 0.883 | 🔺 Rising |
| 2026-11-15 21:02:32 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-15 21:02:02 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:02:32 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:02:37 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:03:42 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:34 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:13:53 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:43 | Glencourse (Kelani Ganga) | 10.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:16 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:01:16 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:35 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:07:01 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:11 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:06:34 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-15 20:02:09 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 21:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:09:32 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-11-15 20:09:26 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-11-15 20:01:58 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-15 20:02:44 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:01:29 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.010 |  |
| 2026-11-15 20:04:25 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-11-15 20:03:23 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-15 21:02:18 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-15 20:06:09 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 20:05:52 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-11-15 20:01:20 | Thanamalwila (Kirindi Oya) | 1.54 | 🟢 Normal | -0.021 |  |
| 2026-11-15 21:02:01 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.022 |  |
| 2026-11-15 20:07:12 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.022 |  |
| 2026-11-15 21:02:12 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | -0.023 |  |
| 2026-11-15 20:06:11 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-11-15 20:03:01 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-11-15 20:04:33 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)