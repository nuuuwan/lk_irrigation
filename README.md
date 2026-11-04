# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_16:03:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 16:03:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:03:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-04 16:03:13 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-04 16:03:08 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-11-04 16:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.010 |  |
| 2026-11-04 16:02:48 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.061 |  |
| 2026-11-04 16:02:34 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:02:15 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.100 |  |
| 2026-11-04 16:02:11 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:02:08 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-04 16:01:48 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:01:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:00:57 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-04 16:00:55 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-04 16:00:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:00:15 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 16:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.02 | 🟡 Alert | -0.010 |  |
| 2026-11-04 15:04:18 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-11-04 16:03:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-11-04 15:11:02 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-11-04 15:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-04 15:05:32 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 16:00:57 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-04 16:00:15 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 16:03:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:00:46 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:01:11 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:05:10 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:01:07 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:01:00 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 16:02:08 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | -0.005 |  |
| 2026-11-04 15:02:38 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:02:34 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:01:45 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:01:09 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-04 16:01:48 | Thanamalwila (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:02:11 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.011 |  |
| 2026-11-04 15:02:56 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-04 16:00:55 | Horowpothana (Yan Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:02:27 | Moragaswewa (Deduru Oya) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 16:03:13 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-04 15:03:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.021 |  |
| 2026-11-04 16:03:08 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-11-04 15:03:14 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.039 |  |
| 2026-11-04 15:03:18 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-11-04 14:14:21 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.044 |  |
| 2026-11-04 15:03:13 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.049 |  |
| 2026-11-04 15:05:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-11-04 16:02:48 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.061 |  |
| 2026-11-04 15:08:19 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.082 |  |
| 2026-11-04 15:02:36 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.083 |  |
| 2026-11-04 15:13:25 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.088 |  |
| 2026-11-04 16:02:15 | Giriulla (Maha Oya) | 2.48 | 🟢 Normal | -0.100 |  |
| 2026-11-04 15:00:34 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.113 |  |
| 2026-11-04 15:07:07 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)