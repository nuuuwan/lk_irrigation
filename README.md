# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_14:03:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 14:03:12 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:02:56 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-11-03 14:02:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-11-03 14:02:51 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2026-11-03 14:02:46 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:02:41 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:02:16 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-03 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | -0.051 |  |
| 2026-11-03 14:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 14:01:35 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:01:33 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | -0.149 |  |
| 2026-11-03 14:01:20 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:01:13 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:00:36 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 14:02:16 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-11-03 14:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 13:06:31 | Moragaswewa (Deduru Oya) | 4.21 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-03 13:04:02 | Putupaula (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 13:07:31 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-03 13:01:49 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:06:11 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:11:50 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:14:29 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:01:13 | Manampitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:01:04 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:02:41 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 14:00:36 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-03 13:20:20 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.008 |  |
| 2026-11-03 14:01:20 | Thanamalwila (Kirindi Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:01:35 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:03:12 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-03 14:02:46 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-03 13:07:35 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.019 |  |
| 2026-11-03 13:06:26 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.019 |  |
| 2026-11-03 13:03:50 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.021 |  |
| 2026-11-03 13:12:13 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.022 |  |
| 2026-11-03 13:04:27 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.030 |  |
| 2026-11-03 13:03:15 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.030 |  |
| 2026-11-03 13:02:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-03 13:09:50 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.037 |  |
| 2026-11-03 14:02:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.039 |  |
| 2026-11-03 14:02:56 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-11-03 13:01:02 | Horowpothana (Yan Oya) | 2.60 | 🟢 Normal | -0.040 |  |
| 2026-11-03 13:06:34 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.046 |  |
| 2026-11-03 13:06:00 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | -0.047 |  |
| 2026-11-03 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.81 | 🟢 Normal | -0.051 |  |
| 2026-11-03 13:03:17 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.051 |  |
| 2026-11-03 14:02:51 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.059 |  |
| 2026-11-03 13:12:32 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | -0.090 |  |
| 2026-11-03 13:05:46 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.098 |  |
| 2026-11-03 13:05:16 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.104 |  |
| 2026-11-03 14:01:33 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | -0.149 |  |
| 2026-11-03 13:03:25 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)