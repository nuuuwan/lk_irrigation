# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_19:20:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,829 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 19:20:59 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:20:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.062 |  |
| 2026-10-05 19:18:10 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.024 |  |
| 2026-10-05 19:15:37 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 19:15:20 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-05 19:11:46 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-05 19:11:45 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.072 |  |
| 2026-10-05 19:11:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:08:09 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.039 |  |
| 2026-10-05 19:06:22 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-10-05 19:05:57 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:05:51 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | 0.875 | 🔺 Rising |
| 2026-10-05 19:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:05:27 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-10-05 19:05:27 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-05 19:05:23 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-10-05 19:05:09 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-10-05 19:05:08 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-05 19:04:43 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.005 |  |
| 2026-10-05 19:04:00 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 19:03:32 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-05 19:03:18 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-05 19:03:11 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-05 19:03:08 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:03:00 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:02:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 19:02:30 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-05 19:02:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:02:20 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 19:02:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:02:08 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-10-05 19:01:53 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-05 19:01:48 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-05 19:01:24 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:01:12 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.289 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 19:05:51 | Holombuwa (Kelani Ganga) | 1.87 | 🟢 Normal | 0.875 | 🔺 Rising |
| 2026-10-05 19:05:23 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-10-05 19:05:09 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-10-05 19:02:08 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-10-05 19:05:27 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-05 19:03:18 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-05 19:02:30 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-05 19:15:37 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-05 19:11:46 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-05 19:03:11 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-05 19:02:32 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-05 19:15:20 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-05 19:04:00 | Deraniyagala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 19:05:08 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-05 19:02:20 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 19:02:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:03:00 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:01:24 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:20:59 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:04:08 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:11:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:05:48 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:05:57 | Siyambalanduwa (Heda Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:02:20 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:03:08 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-05 18:03:21 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:01:12 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-05 19:04:43 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.005 |  |
| 2026-10-05 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.010 |  |
| 2026-10-05 19:01:53 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-05 19:01:48 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-05 19:05:27 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-10-05 19:03:32 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-10-05 19:06:22 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-10-05 19:18:10 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.024 |  |
| 2026-10-05 19:08:09 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.039 |  |
| 2026-10-05 19:20:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.062 |  |
| 2026-10-05 19:11:45 | Ellagawa (Kalu Ganga) | 5.62 | 🟢 Normal | -0.072 |  |
| 2026-10-05 19:00:42 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -0.289 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)