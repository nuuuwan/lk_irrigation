# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_16:22:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,222 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 16:22:50 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:14:27 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 16:09:12 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:09:01 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-10-30 16:09:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.029 |  |
| 2026-10-30 16:08:38 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.027 |  |
| 2026-10-30 16:08:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-30 16:07:42 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 16:06:06 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:05:25 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:05:20 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.048 |  |
| 2026-10-30 16:04:56 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:04:46 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:04:26 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-30 16:04:16 | Putupaula (Kalu Ganga) | 3.24 | 🟡 Alert | -0.020 |  |
| 2026-10-30 16:03:52 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-30 16:03:38 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:03:17 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:03:05 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:02:48 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.032 |  |
| 2026-10-30 16:02:23 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:02:12 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:02:11 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 16:02:08 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-30 16:02:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:02:06 | Panadugama (Nilwala Ganga) | 5.24 | 🟡 Alert | -0.040 |  |
| 2026-10-30 16:01:47 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.026 |  |
| 2026-10-30 16:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:01:32 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.023 |  |
| 2026-10-30 16:01:24 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:01:04 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:01:00 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 16:01:00 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:00:26 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-30 16:00:23 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.005 |  |
| 2026-10-30 16:00:20 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-30 15:59:46 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 16:14:27 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 16:04:16 | Putupaula (Kalu Ganga) | 3.24 | 🟡 Alert | -0.020 |  |
| 2026-10-30 16:09:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.029 |  |
| 2026-10-30 16:02:06 | Panadugama (Nilwala Ganga) | 5.24 | 🟡 Alert | -0.040 |  |
| 2026-10-30 16:04:26 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-30 16:00:26 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-30 16:02:08 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-30 16:08:04 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-30 16:02:11 | Thanamalwila (Kirindi Oya) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 16:01:00 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-30 16:03:52 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-30 16:07:42 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 16:01:04 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:03:38 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:00:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:01:46 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:22:50 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:09:12 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:00:20 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:01:24 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:02:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:02:23 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:04:46 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:05:25 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:04:56 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-30 16:00:23 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.005 |  |
| 2026-10-30 16:09:01 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.009 |  |
| 2026-10-30 15:02:14 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:03:17 | Hanwella (Kelani Ganga) | 2.93 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:02:12 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:03:05 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:06:06 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:01:00 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-30 16:01:32 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.023 |  |
| 2026-10-30 16:01:47 | Baddegama (Gin Ganga) | 3.25 | 🟢 Normal | -0.026 |  |
| 2026-10-30 16:08:38 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.027 |  |
| 2026-10-30 16:02:48 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.032 |  |
| 2026-10-30 16:05:20 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)