# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_19:02:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 19:02:39 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:02:26 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-11-15 19:02:22 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-15 19:02:18 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-11-15 19:02:06 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.020 |  |
| 2026-11-15 19:02:05 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:01:43 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-11-15 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:01:13 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:01:06 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:00:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 19:00:06 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:26:00 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 18:10:23 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 19:02:22 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-15 18:07:18 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-15 18:05:02 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-15 19:00:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 18:01:13 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:01:06 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:02:05 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:04:19 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:02:39 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:26:00 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:03:15 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:02:54 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:04:01 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:02:08 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:07:25 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:00:37 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:04:21 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-15 19:01:13 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 18:02:26 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:06:38 | Panadugama (Nilwala Ganga) | 4.70 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:04:55 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-11-15 19:00:06 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:45 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-11-15 18:02:11 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:22 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:02:15 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.011 |  |
| 2026-11-15 18:01:29 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.017 |  |
| 2026-11-15 18:01:18 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-15 19:02:18 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-11-15 19:02:06 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.020 |  |
| 2026-11-15 18:04:00 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.029 |  |
| 2026-11-15 18:02:10 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-15 19:01:43 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.030 |  |
| 2026-11-15 19:02:26 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.050 |  |
| 2026-11-15 18:01:59 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.181 |  |
| 2026-11-15 18:01:35 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)