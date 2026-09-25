# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_18:18:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,797 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 18:18:27 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:09:28 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 18:06:15 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:05:27 | Panadugama (Nilwala Ganga) | 6.37 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-25 18:05:20 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 18:05:13 | Glencourse (Kelani Ganga) | 13.63 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:05:06 | Nawalapitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-25 18:04:49 | Hanwella (Kelani Ganga) | 6.00 | 🟢 Normal | -0.049 |  |
| 2026-09-25 18:04:28 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 18:04:15 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.019 |  |
| 2026-09-25 18:04:03 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -1.019 |  |
| 2026-09-25 18:03:41 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 18:03:26 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-09-25 18:03:24 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:03:23 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-09-25 18:03:00 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-25 18:02:54 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:48 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 18:02:35 | Deraniyagala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-09-25 18:02:35 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.085 |  |
| 2026-09-25 18:02:32 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:24 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.022 |  |
| 2026-09-25 18:02:22 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:02:17 | Urawa (Nilwala Ganga) | 1.30 | 🟢 Normal | -1.019 |  |
| 2026-09-25 18:02:08 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 18:02:03 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:23 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:23 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:12 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.062 |  |
| 2026-09-25 18:01:09 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.042 |  |
| 2026-09-25 18:01:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:03 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:00:45 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-09-25 18:00:42 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 18:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.05 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 18:02:08 | Baddegama (Gin Ganga) | 4.75 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 18:04:28 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 18:05:27 | Panadugama (Nilwala Ganga) | 6.37 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-25 18:03:41 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.000 |  |
| 2026-09-25 18:04:15 | Rathnapura (Kalu Ganga) | 6.05 | 🟡 Alert | -0.019 |  |
| 2026-09-25 18:01:09 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.042 |  |
| 2026-09-25 18:05:06 | Nawalapitiya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-09-25 18:05:20 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 18:03:00 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-25 18:09:28 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-25 18:00:42 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:04 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:22 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:24 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:23 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:18:27 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:48 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:40 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:03:24 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:06:15 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:03 | Putupaula (Kalu Ganga) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:23 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:54 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:32 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:02:03 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-09-25 18:02:35 | Deraniyagala (Kelani Ganga) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:05:13 | Glencourse (Kelani Ganga) | 13.63 | 🟢 Normal | -0.020 |  |
| 2026-09-25 18:02:24 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.022 |  |
| 2026-09-25 18:00:45 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.025 |  |
| 2026-09-25 18:03:26 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-09-25 18:03:23 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.030 |  |
| 2026-09-25 18:04:49 | Hanwella (Kelani Ganga) | 6.00 | 🟢 Normal | -0.049 |  |
| 2026-09-25 18:01:12 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.062 |  |
| 2026-09-25 18:02:35 | Thawalama (Gin Ganga) | 3.50 | 🟢 Normal | -0.085 |  |
| 2026-09-25 18:04:03 | Urawa (Nilwala Ganga) | 1.27 | 🟢 Normal | -1.019 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)