# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_17:21:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,977 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 17:21:34 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-18 17:14:47 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:09:54 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:08:54 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:08:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:07:35 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.046 |  |
| 2026-08-18 17:07:06 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:07:03 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.039 |  |
| 2026-08-18 17:06:05 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-08-18 17:05:55 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 17:02:00 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-08-18 17:02:07 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-08-18 17:03:48 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-18 17:21:34 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-18 17:01:14 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:00:20 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:08:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:02:21 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:00:41 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:05:55 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:03:40 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:07:06 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:14:47 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:02:46 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:03:08 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:04:36 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:05:00 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:04:52 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:05:22 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:05:01 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:08:54 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:09:54 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 17:06:05 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-08-18 17:02:26 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-08-18 17:05:20 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-18 17:05:04 | Thanamalwila (Kirindi Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-08-18 17:02:32 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-18 17:03:58 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-08-18 17:00:09 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-18 17:04:16 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-08-18 17:02:20 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-08-18 17:05:43 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2026-08-18 16:22:55 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.023 |  |
| 2026-08-18 17:04:07 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-08-18 17:02:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-18 17:03:48 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.034 |  |
| 2026-08-18 17:07:03 | Glencourse (Kelani Ganga) | 9.71 | 🟢 Normal | -0.039 |  |
| 2026-08-18 17:07:35 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.046 |  |
| 2026-08-18 17:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)