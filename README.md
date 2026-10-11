# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_05:36:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 05:36:00 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-11 05:32:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-11 05:25:14 | Magura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.256 |  |
| 2026-10-11 05:14:00 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-11 05:13:16 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-10-11 05:12:31 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2026-10-11 05:09:19 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.093 |  |
| 2026-10-11 05:08:57 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-11 05:08:35 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-11 05:07:48 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-11 05:07:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.130 |  |
| 2026-10-11 05:06:59 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 05:02:35 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-11 05:07:48 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-11 05:08:35 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-11 05:05:30 | Putupaula (Kalu Ganga) | 1.16 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-11 05:02:47 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-11 05:01:56 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 05:08:57 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-11 05:06:59 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-11 05:36:00 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-11 05:14:00 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-11 05:00:11 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 05:02:34 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 05:32:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.18 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-11 05:02:43 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:57 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:00:54 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:02:44 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:00:10 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:03:10 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:06:45 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 05:04:44 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-11 05:04:58 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 05:12:31 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.017 |  |
| 2026-10-11 05:01:16 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-10-11 04:06:31 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-11 04:02:49 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2026-10-11 05:03:14 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.048 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-11 05:03:20 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.059 |  |
| 2026-10-11 05:13:16 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.080 |  |
| 2026-10-11 05:01:05 | Peradeniya (Mahaweli Ganga) | 3.21 | 🟢 Normal | -0.081 |  |
| 2026-10-11 05:09:19 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.093 |  |
| 2026-10-11 05:03:24 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.123 |  |
| 2026-10-11 05:07:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.130 |  |
| 2026-10-11 05:00:43 | Thawalama (Gin Ganga) | 2.97 | 🟢 Normal | -0.253 |  |
| 2026-10-11 05:25:14 | Magura (Kalu Ganga) | 3.72 | 🟢 Normal | -0.256 |  |
| 2026-10-11 05:02:25 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.592 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)