# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_05:05:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,647 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 05:05:30 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-11 05:04:58 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 05:04:44 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-11 05:03:24 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.123 |  |
| 2026-10-11 05:03:20 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.059 |  |
| 2026-10-11 05:03:14 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.048 |  |
| 2026-10-11 05:03:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:57 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:47 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 05:02:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:43 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:35 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-11 05:02:34 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 05:02:25 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.592 |  |
| 2026-10-11 05:01:56 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 05:01:16 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-10-11 05:01:05 | Peradeniya (Mahaweli Ganga) | 3.21 | 🟢 Normal | -0.081 |  |
| 2026-10-11 05:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:00:43 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.253 |  |
| 2026-10-11 05:00:11 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 05:00:10 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:37:59 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:35:03 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | -0.592 |  |
| 2026-10-11 04:32:03 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-11 04:25:02 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 05:02:35 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-11 04:04:45 | Badalgama (Maha Oya) | 4.04 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-11 04:02:45 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-11 04:04:15 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-11 05:05:30 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-11 05:02:47 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 03:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 04:05:52 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 05:01:56 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 04:16:17 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-11 04:25:02 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-11 04:06:10 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 05:00:11 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 05:02:34 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 05:02:43 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:57 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:00:10 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:03:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:37:59 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:04:44 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-11 05:04:58 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 05:01:16 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-10-11 04:04:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-10-11 04:06:31 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-11 04:02:49 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2026-10-11 05:03:14 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.048 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-11 04:11:33 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.057 |  |
| 2026-10-11 05:03:20 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.059 |  |
| 2026-10-11 04:06:09 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.073 |  |
| 2026-10-11 05:01:05 | Peradeniya (Mahaweli Ganga) | 3.21 | 🟢 Normal | -0.081 |  |
| 2026-10-11 04:11:25 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-10-11 05:03:24 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.123 |  |
| 2026-10-11 05:00:43 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.253 |  |
| 2026-10-11 05:02:25 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.592 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)