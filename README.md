# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_17:04:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,725 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 17:04:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-25 17:04:06 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-25 17:03:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:56 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:34 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:16 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-25 17:03:10 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:03:06 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-10-25 17:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-25 17:02:54 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:53 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-10-25 17:02:45 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:39 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:34 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:02:31 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-10-25 17:02:27 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-25 17:02:22 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.071 |  |
| 2026-10-25 17:02:17 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:02:03 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.070 |  |
| 2026-10-25 17:01:24 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:01:15 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-25 17:01:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 17:01:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.093 |  |
| 2026-10-25 17:01:03 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:00:54 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:00:29 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 17:03:06 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | 0.391 | 🔺 Rising |
| 2026-10-25 17:04:18 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-25 16:04:54 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-10-25 17:03:16 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-25 17:02:27 | Dunamale (Aththanagalu Oya) | 2.02 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-10-25 16:05:54 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-25 17:01:15 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-10-25 17:04:06 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-25 17:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-25 16:06:44 | Ellagawa (Kalu Ganga) | 6.87 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-25 16:04:19 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 17:01:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 16:05:48 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 16:01:03 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 16:03:50 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 16:03:03 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 16:02:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:34 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:02:34 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:56 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:37 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 16:08:09 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:01:24 | Manampitiya (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:01:03 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:02:17 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-25 17:03:10 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:45 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:54 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:00:54 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:39 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | -0.010 |  |
| 2026-10-25 17:02:31 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-10-25 16:06:30 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-10-25 17:02:53 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-10-25 16:05:30 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.019 |  |
| 2026-10-25 17:00:29 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-10-25 17:02:03 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.070 |  |
| 2026-10-25 17:02:22 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.071 |  |
| 2026-10-25 17:01:11 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)