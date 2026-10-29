# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_09:04:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 09:04:53 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-29 09:04:53 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-29 09:04:43 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-29 09:04:23 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:03:57 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 09:03:38 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-10-29 09:03:22 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:03:12 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | -0.061 |  |
| 2026-10-29 09:03:05 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:02:48 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:02:37 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.039 |  |
| 2026-10-29 09:02:32 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:02:29 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.022 |  |
| 2026-10-29 09:02:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-10-29 09:01:47 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-29 09:01:47 | Ellagawa (Kalu Ganga) | 10.06 | 🟡 Alert | -0.040 |  |
| 2026-10-29 09:01:45 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:01:40 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | -0.010 |  |
| 2026-10-29 09:01:24 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 09:01:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-10-29 09:01:13 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.056 |  |
| 2026-10-29 09:01:04 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-10-29 09:00:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-29 09:00:14 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-29 09:00:08 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-29 08:47:07 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:47:05 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:47:03 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 08:07:17 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 08:18:36 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 08:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.40 | 🟠 Minor Flood | -0.048 |  |
| 2026-10-29 09:01:40 | Putupaula (Kalu Ganga) | 3.73 | 🟡 Alert | -0.010 |  |
| 2026-10-29 09:01:47 | Ellagawa (Kalu Ganga) | 10.06 | 🟡 Alert | -0.040 |  |
| 2026-10-29 08:05:11 | Panadugama (Nilwala Ganga) | 5.88 | 🟡 Alert | -0.044 |  |
| 2026-10-29 09:04:53 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-29 09:00:08 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-10-29 09:01:24 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-29 09:00:14 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-29 09:03:57 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 09:01:45 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:03:05 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:04:12 | Galgamuwa (Mee Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:09:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:02:48 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:04:23 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:06:29 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:03:22 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 08:05:54 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:02:32 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-29 09:04:43 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-29 09:00:49 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-29 09:04:53 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-29 08:05:45 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-10-29 09:01:47 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-29 09:02:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-10-29 09:03:38 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | -0.020 |  |
| 2026-10-29 09:02:29 | Thanthirimale (Malwathu Oya) | 1.66 | 🟢 Normal | -0.022 |  |
| 2026-10-29 09:01:19 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-10-29 09:02:37 | Moragaswewa (Deduru Oya) | 1.36 | 🟢 Normal | -0.039 |  |
| 2026-10-29 09:01:04 | Magura (Kalu Ganga) | 3.55 | 🟢 Normal | -0.050 |  |
| 2026-10-29 09:01:13 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.056 |  |
| 2026-10-29 09:03:12 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | -0.061 |  |
| 2026-10-29 08:07:05 | Glencourse (Kelani Ganga) | 11.23 | 🟢 Normal | -0.066 |  |
| 2026-10-29 08:04:50 | Rathnapura (Kalu Ganga) | 4.95 | 🟢 Normal | -0.076 |  |
| 2026-10-29 08:06:33 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.121 |  |
| 2026-10-29 08:07:35 | Pitabeddara (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.205 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)