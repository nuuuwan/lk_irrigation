# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_19:52:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,113 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 19:52:51 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:20:32 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.017 |  |
| 2026-10-12 19:19:52 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 19:06:25 | Norwood (Kelani Ganga) | 1.94 | 🟡 Alert | 0.318 | 🔺 Rising |
| 2026-10-12 19:05:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-10-12 18:54:58 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-10-12 19:09:04 | Thawalama (Gin Ganga) | 2.79 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-12 19:12:19 | Rathnapura (Kalu Ganga) | 2.50 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-10-12 19:01:56 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-12 19:04:26 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-12 19:02:10 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-12 19:02:11 | Peradeniya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-10-12 19:09:01 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-10-12 19:04:34 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-10-12 19:12:29 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-12 19:07:16 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-12 19:03:21 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 19:10:31 | Putupaula (Kalu Ganga) | 1.84 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-12 19:04:35 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:02:02 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:02:43 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:03:07 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:01:11 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:52:51 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:19:52 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:07:08 | Glencourse (Kelani Ganga) | 11.62 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:02:18 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:07:27 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:02:19 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-12 19:05:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-10-12 19:03:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-12 19:20:32 | Baddegama (Gin Ganga) | 2.52 | 🟢 Normal | -0.017 |  |
| 2026-10-12 19:01:47 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 19:03:09 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-10-12 19:03:42 | Badalgama (Maha Oya) | 3.17 | 🟢 Normal | -0.039 |  |
| 2026-10-12 19:03:08 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.049 |  |
| 2026-10-12 19:04:01 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.049 |  |
| 2026-10-12 19:01:44 | Ellagawa (Kalu Ganga) | 6.84 | 🟢 Normal | -0.063 |  |
| 2026-10-12 19:07:15 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)