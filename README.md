# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_22:03:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 22:03:02 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.097 |  |
| 2026-11-21 22:03:01 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.043 |  |
| 2026-11-21 22:02:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:39 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-21 22:02:28 | Kuda Oya (Kirindi Oya) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-11-21 22:02:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:19 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:02:16 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 22:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2026-11-21 22:01:33 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:01:07 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 22:01:05 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.052 |  |
| 2026-11-21 22:00:20 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 22:02:39 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-21 21:06:38 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-21 21:05:24 | Peradeniya (Mahaweli Ganga) | 2.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-21 22:02:16 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-21 21:06:28 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-21 22:00:20 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 22:01:07 | Horowpothana (Yan Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 21:07:42 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 22:02:27 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:30 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:01:33 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:05:52 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:03:26 | Moraketiya (Walawe Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 22:02:55 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:03:25 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:05:52 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:02:19 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-21 21:03:43 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-11-21 22:01:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-21 21:08:50 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | -0.018 |  |
| 2026-11-21 21:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.020 |  |
| 2026-11-21 22:02:28 | Kuda Oya (Kirindi Oya) | 2.12 | 🟢 Normal | -0.029 |  |
| 2026-11-21 21:06:55 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | -0.038 |  |
| 2026-11-21 21:02:20 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-11-21 21:04:34 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.042 |  |
| 2026-11-21 22:03:01 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.043 |  |
| 2026-11-21 22:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2026-11-21 21:03:07 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.052 |  |
| 2026-11-21 22:01:05 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.052 |  |
| 2026-11-21 21:04:24 | Hanwella (Kelani Ganga) | 1.64 | 🟢 Normal | -0.060 |  |
| 2026-11-21 21:01:13 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.073 |  |
| 2026-11-21 22:03:02 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | -0.097 |  |
| 2026-11-21 21:03:11 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)