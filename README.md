# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--12_22:22:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,216 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 22:22:23 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-12 22:13:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-12 22:08:53 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:08:39 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-12 22:08:36 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:08:15 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-09-12 22:08:07 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:07:17 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 22:07:13 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:06:08 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.019 |  |
| 2026-09-12 22:05:58 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-12 22:05:37 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.019 |  |
| 2026-09-12 22:05:30 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:05:28 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:05:05 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:04:59 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:04:17 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.030 |  |
| 2026-09-12 22:03:15 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:03:09 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:03:05 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:50 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.082 |  |
| 2026-09-12 22:02:47 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:37 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:22 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:14 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-12 22:02:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:01:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-09-12 22:01:47 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:01:41 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-12 22:01:41 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:01:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:00:58 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:00:10 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 21:58:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-12 22:01:41 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-12 21:58:58 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-12 22:13:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-12 22:05:58 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-12 22:22:23 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-12 22:07:17 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-12 22:08:39 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.57 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:00:10 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:01:41 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:47 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-12 21:04:29 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:01:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:05:28 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:00:58 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:03:01 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:05:05 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:03:09 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:37 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:08:53 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:05:30 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:03:05 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:10 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:08:07 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:51 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:03:15 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:08:36 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:04:59 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:07:13 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:45 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:22 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:01:47 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-12 22:02:14 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-12 22:08:15 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-09-12 22:06:08 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | -0.019 |  |
| 2026-09-12 22:05:37 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.019 |  |
| 2026-09-12 22:04:17 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.030 |  |
| 2026-09-12 22:01:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.040 |  |
| 2026-09-12 22:02:50 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)