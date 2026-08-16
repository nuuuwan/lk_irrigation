# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_15:10:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,132 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 15:10:40 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.061 |  |
| 2026-08-16 15:09:28 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:08:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:07:59 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-08-16 15:07:20 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.058 |  |
| 2026-08-16 15:07:00 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.132 |  |
| 2026-08-16 15:06:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.038 |  |
| 2026-08-16 15:06:19 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:06:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-16 15:04:33 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:04:12 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:04:04 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-16 15:04:03 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-16 15:03:41 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:40 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-16 15:03:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:27 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:16 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-16 15:03:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:12 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:55 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:37 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-16 15:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-16 15:02:27 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:22 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:10 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:05 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:40 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:26 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:16 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:09 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.042 |  |
| 2026-08-16 15:01:02 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:00:40 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:00:36 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:00:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 15:04:04 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-16 15:03:16 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-08-16 15:06:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-16 15:02:37 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-16 14:07:10 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-16 15:03:45 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-16 15:04:12 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:12 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:00:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:16 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:27 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:02 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:55 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:09:28 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:08:11 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:22 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:04:03 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:03:27 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:00:40 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:04:33 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:06:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:05 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:06:19 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:00:36 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:26 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:01:40 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:10 | Thanamalwila (Kirindi Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-16 15:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-08-16 15:07:59 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-08-16 15:03:40 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-08-16 15:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.038 |  |
| 2026-08-16 15:01:09 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.042 |  |
| 2026-08-16 15:07:20 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.058 |  |
| 2026-08-16 15:10:40 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.061 |  |
| 2026-08-16 15:07:00 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)