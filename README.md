# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_06:35:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 06:35:49 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.004 |  |
| 2026-10-11 06:17:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:12:31 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-11 06:11:00 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.080 |  |
| 2026-10-11 06:10:43 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.019 |  |
| 2026-10-11 06:09:11 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:08:20 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:06:49 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 06:04:23 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.410 | 🔺 Rising |
| 2026-10-11 06:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-10-11 06:05:16 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.297 | 🔺 Rising |
| 2026-10-11 06:03:56 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-11 06:03:31 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-10-11 06:03:27 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-11 06:03:24 | Ellagawa (Kalu Ganga) | 6.58 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-11 06:02:47 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:02:36 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:06:33 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:00:24 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:04:53 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:17:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:08:20 | Nagalagam Street (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:05:38 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:09:11 | Dunamale (Aththanagalu Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:05:13 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:04:50 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:01:32 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:06:49 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 06:35:49 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.004 |  |
| 2026-10-11 06:01:42 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-10-11 06:04:51 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-11 06:12:31 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-11 06:00:48 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.016 |  |
| 2026-10-11 06:10:43 | Hanwella (Kelani Ganga) | 3.11 | 🟢 Normal | -0.019 |  |
| 2026-10-11 06:01:25 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-10-11 06:00:14 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-10-11 06:04:34 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.033 |  |
| 2026-10-11 06:01:27 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.052 |  |
| 2026-10-11 06:11:00 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | -0.080 |  |
| 2026-10-11 06:05:03 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.093 |  |
| 2026-10-11 06:03:47 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.113 |  |
| 2026-10-11 06:03:55 | Magura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.124 |  |
| 2026-10-11 06:03:03 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | -0.184 |  |
| 2026-10-11 06:04:54 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.252 |  |
| 2026-10-11 06:04:49 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)