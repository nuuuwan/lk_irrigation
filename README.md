# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_16:28:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,740 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 16:28:19 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-20 16:22:03 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-20 16:18:13 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.025 |  |
| 2026-08-20 16:13:08 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.034 |  |
| 2026-08-20 16:12:08 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-08-20 16:09:39 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-08-20 16:06:26 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:06:25 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-08-20 16:06:22 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:06:07 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:05:57 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.076 |  |
| 2026-08-20 16:05:46 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:05:40 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:04:40 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-20 16:04:37 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 16:06:25 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-08-20 16:01:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-20 16:04:30 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-20 16:04:40 | Hanwella (Kelani Ganga) | 1.39 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-20 16:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-20 16:22:03 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-20 16:28:19 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-20 16:00:37 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 16:04:09 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 16:04:37 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:08:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:03:24 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:01:43 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:06:22 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:04:45 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:00:12 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:03:51 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:05:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:03:06 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:01:08 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:01:59 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:03:51 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:06:07 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:06:26 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:05:40 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:03:33 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:05:46 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:02:27 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-20 16:09:39 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-08-20 16:02:47 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-08-20 16:02:34 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-08-20 16:01:28 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-08-20 16:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-08-20 16:12:08 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.019 |  |
| 2026-08-20 16:01:52 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-08-20 16:18:13 | Magura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.025 |  |
| 2026-08-20 16:13:08 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.034 |  |
| 2026-08-20 16:05:57 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.076 |  |
| 2026-08-20 16:01:59 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)