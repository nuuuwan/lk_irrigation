# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_20:15:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,347 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 20:15:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:11:19 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:09:23 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:08:32 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-09-30 20:08:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:07:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.112 |  |
| 2026-09-30 20:07:01 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:06:58 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:06:20 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:06:02 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:05:35 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.033 |  |
| 2026-09-30 20:05:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:44 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:29 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 20:04:19 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:18 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:13 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-09-30 20:04:02 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:00 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:03:55 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 20:03:32 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-09-30 20:03:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:03:00 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:02:50 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-30 20:02:33 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:02:26 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:02:26 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.040 |  |
| 2026-09-30 20:02:24 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-30 20:02:08 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:02:05 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:02:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.093 |  |
| 2026-09-30 20:01:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:57 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-09-30 20:01:55 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:35 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 20:01:57 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-30 20:02:24 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-30 20:02:50 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-30 20:04:29 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 20:03:55 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 20:02:26 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:19 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:11:19 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:07:01 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:44 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:58 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:06:20 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:06:02 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:08:23 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:00 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:02:05 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:05:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:02 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:04:18 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:15:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:01:55 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:02:33 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 20:03:18 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:09:23 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:03:00 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:06:58 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:01:35 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.010 |  |
| 2026-09-30 20:08:32 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-09-30 20:03:32 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-09-30 20:01:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.67 | 🟢 Normal | -0.021 |  |
| 2026-09-30 20:05:35 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | -0.033 |  |
| 2026-09-30 20:04:13 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.039 |  |
| 2026-09-30 20:02:26 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.040 |  |
| 2026-09-30 20:02:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.093 |  |
| 2026-09-30 20:07:42 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)