# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_15:33:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,843 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 15:33:32 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 15:07:04 | Norwood (Kelani Ganga) | 1.54 | 🟡 Alert | 0.347 | 🔺 Rising |
| 2026-10-13 15:02:50 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-13 15:04:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-10-13 15:08:21 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.037 |  |
| 2026-10-13 15:02:31 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-10-13 15:03:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-13 15:02:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-13 15:04:48 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 15:06:54 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 15:00:15 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:01:57 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:00:57 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:03:26 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:00:07 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:02:31 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:01:35 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:09:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:01:38 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:09:10 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:07:31 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:02:45 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:33:32 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:00:35 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:02:05 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-10-13 15:04:06 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-13 15:05:26 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-13 15:10:03 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2026-10-13 15:00:44 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-10-13 15:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-10-13 15:05:20 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | -0.011 |  |
| 2026-10-13 15:05:06 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-10-13 15:05:50 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.021 |  |
| 2026-10-13 15:02:54 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.021 |  |
| 2026-10-13 15:06:28 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.028 |  |
| 2026-10-13 15:02:17 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.032 |  |
| 2026-10-13 14:59:57 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.032 |  |
| 2026-10-13 15:02:50 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | -0.059 |  |
| 2026-10-13 15:07:59 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)