# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_14:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,802 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 14:03:57 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.000 |  |
| 2026-10-13 14:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | -0.033 |  |
| 2026-10-13 14:02:36 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.039 |  |
| 2026-10-13 14:08:20 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-10-13 14:04:10 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-13 14:00:31 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 14:02:07 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 14:05:59 | Putupaula (Kalu Ganga) | 1.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 14:01:54 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 13:01:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-13 14:01:06 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-13 14:05:10 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-13 14:02:52 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-13 14:05:14 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-10-13 14:06:29 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-13 14:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-10-13 14:09:27 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-10-13 14:01:01 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-10-13 14:00:39 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-13 14:04:42 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2026-10-13 14:03:39 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-10-13 14:04:12 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-13 14:00:19 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-10-13 13:59:58 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.013 |  |
| 2026-10-13 14:06:19 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | -0.019 |  |
| 2026-10-13 14:04:46 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | -0.019 |  |
| 2026-10-13 14:04:19 | Glencourse (Kelani Ganga) | 10.96 | 🟢 Normal | -0.020 |  |
| 2026-10-13 14:02:18 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-10-13 14:09:39 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-10-13 14:01:40 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.021 |  |
| 2026-10-13 14:07:42 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-10-13 14:03:08 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2026-10-13 14:06:30 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.058 |  |
| 2026-10-13 14:02:09 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.071 |  |
| 2026-10-13 14:14:58 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.089 |  |
| 2026-10-13 14:02:40 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.094 |  |
| 2026-10-13 14:03:20 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.104 |  |
| 2026-10-13 14:07:28 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.108 |  |
| 2026-10-13 14:00:38 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | -0.748 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)