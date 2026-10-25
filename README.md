# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_11:22:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,499 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 11:22:11 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-25 11:13:34 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-25 11:11:19 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | 0.018 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 11:02:23 | Weraganthota (Mahaweli Ganga) | -2.54 | 🟢 Normal | 0.456 | 🔺 Rising |
| 2026-10-25 11:10:37 | Kithulgala (Kelani Ganga) | 2.21 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-25 11:03:03 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-25 11:01:56 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 11:02:24 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-25 11:01:14 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-10-25 11:13:34 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-25 11:02:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-25 11:03:50 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-25 11:06:34 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-25 11:08:50 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-25 11:08:55 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 11:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 11:11:19 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-25 11:22:11 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-25 11:02:01 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-25 11:05:45 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 11:02:27 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 11:03:25 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 11:00:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:02:20 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:03:34 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:03:10 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:02:28 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:02:33 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:01:02 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:06:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:04:17 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:02:47 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:03:43 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-25 10:01:39 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-25 11:03:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-25 11:04:23 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-25 11:05:11 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.019 |  |
| 2026-10-25 11:04:38 | Hanwella (Kelani Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-10-25 11:01:27 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-10-25 11:01:36 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-10-25 11:07:28 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.058 |  |
| 2026-10-25 11:03:27 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)