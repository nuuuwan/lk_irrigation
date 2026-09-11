# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--11_19:04:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **258,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 19:04:45 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-09-11 19:04:02 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:03:28 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-09-11 19:03:16 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-11 19:02:45 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.010 |  |
| 2026-09-11 19:02:39 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:02:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:02:25 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.013 |  |
| 2026-09-11 19:02:03 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-09-11 19:01:56 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:53 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:10 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-11 19:01:04 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:00:56 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:00:41 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-11 19:02:03 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.351 | 🔺 Rising |
| 2026-09-11 19:03:16 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-11 18:03:43 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-11 18:08:01 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:02:39 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:00:41 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:01:32 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:02:16 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:00:56 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:02:30 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:01:43 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:56 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:08:53 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:04:02 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:04:25 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:03:00 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:09:51 | Holombuwa (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:04 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:02:32 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:07:30 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-11 19:01:53 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-11 18:00:24 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-11 19:01:10 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-11 18:03:23 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-09-11 18:06:57 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-11 19:02:45 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.010 |  |
| 2026-09-11 18:07:21 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-09-11 18:00:29 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.012 |  |
| 2026-09-11 19:02:25 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | -0.013 |  |
| 2026-09-11 19:03:28 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-09-11 18:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-09-11 18:02:39 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-09-11 19:04:45 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.029 |  |
| 2026-09-11 18:01:07 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.058 |  |
| 2026-09-11 18:05:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.131 |  |
| 2026-09-11 18:01:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)